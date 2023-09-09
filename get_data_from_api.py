from datetime import datetime, timedelta
import pandas as pd
import json
import requests

dict_stations = {
'mizpe_ramon': [69, 379, 265, 296],
'avdat': [271, 335],
'sede_boker': [98],
'arad': [29, 240],
'beer_sheva': [59, 293, 60, 411, 412]
}
start_date = [i for i in range(2000, 2022)]
for k, v in dict_stations.items():
    for year in start_date:
        flag = False
        for i in v:
            try:
                url = f"https://api.ims.gov.il/v1/envista/stations/{i}/data/?from={year}/09/01&to={year + 1}/06/01"
                headers = {'Authorization': 'ApiToken f058958a-d8bd-47cc-95d7-7ecf98610e47'}
                response = requests.get(url, headers=headers, verify=False)
                data = json.loads(response.text.encode('utf8'))
                flag = True
                break
            except Exception as e:
                continue
        if flag == False:
            continue
        data_list = []
        for entry in data['data']:
            datetime_str = entry['datetime']
            original_datetime = datetime.fromisoformat(datetime_str[:-6])  # Parse without timezone offset
            timezone_offset = timedelta(hours=int(datetime_str[-5:-3]), minutes=int(datetime_str[-2:]))

            # Check if the timezone offset is not +03:00 (adjust as needed)
            if timezone_offset != timedelta(hours=3):
                # Adjust the datetime by adding the timezone offset
                adjusted_datetime = original_datetime + (timedelta(hours=3) - timezone_offset)
            else:
                adjusted_datetime = original_datetime

            # Format the adjusted datetime as per your requirement
            formatted_datetime = adjusted_datetime.strftime('%d/%m/%Y %H:%M')
            data_list.append({
                'rain_station': k,
                'start_rain': formatted_datetime,
                'rain_amount': entry['channels'][0]['value'],
                'temperature': entry['channels'][6]['value'],
                'humidity': entry['channels'][7]['value']
            })
        df = pd.DataFrame(data_list)
        print(f"{k}_station_10min_rain_0109{year}_0106{year+1}.csv")
        df.to_csv(f"{k}_station_10min_rain_0109{year}_0106{year+1}.csv", index=False)
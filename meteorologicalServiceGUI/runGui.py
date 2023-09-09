import tkinter as tk
from tkinter import ttk
from PIL import Image
import pandas as pd
import joblib

# Function to handle the "Create" button click event
stations_dict = {
    'שדה בוקר': 'sede_boker',
    'פארן': 'faran',
    'מצפה רמון': 'mizpe_ramon',
    'עבדת': 'avdat',
    'ערד': 'arad',
    'באר שבע': 'beer_sheva'
}


def create_button_clicked():
    # Get the values from the text boxes and dropdown lists
    rain_amount_value = rain_amount_entry.get()
    humidity_value = humidity_entry.get()
    temperature_value = temperature_entry.get()
    rain_variance_value = rain_variance_entry.get()
    rain_amount_12h_value = rain_amount_12h_entry.get()
    rain_amount_3h_value = rain_amount_3h_entry.get()
    month_value = month_entry.get()
    station_name_value = station_name_dropdown.get()
    river_name_value = river_name_dropdown.get()
    station_name = stations_dict[station_name_value]
    try:
        print(f"Models/{station_name}_{river_name_value}_XGBoost.pkl")
        model = joblib.load(f"Models/{station_name}_{river_name_value}_XGBoost.pkl")
    except Exception as e:
        print(e)
        message_label.config(text=f"Flow will not occure in {river_name_value} river!", fg="red")
        return
    try:
        features_data = {
            'rain_amount': [float(rain_amount_value)],
            'humidity': [float(humidity_value)],
            'temperature': [float(temperature_value)],
            'rain_variance': [float(rain_variance_value)],
            'avg_of_rain_12h_before': [float(rain_amount_12h_value)],
            'avg_of_rain_3h_before': [float(rain_amount_3h_value)],
            'start_month': [int(month_value)]
        }
    except:
        message_label.config(text=f"All field must be filled by numbers!", fg="red")
        return

    input_df = pd.DataFrame(features_data)
    predictions = model.predict(input_df)
    # Create a label for displaying the message
    print(predictions[0])
    if predictions[0] == 0:
        message_label.config(text=f"Flow will not occure in {river_name_value} river!", fg="red")
    else:
        message_label.config(text=f"Flow will occure in {river_name_value} river!", fg="green")


# Create the main window
root = tk.Tk()
root.title("Meteorological Service GUI App")

# Create labels and text entry boxes on the left side
left_frame = ttk.Frame(root)
left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="n")

# Dropdown lists
station_name_label = ttk.Label(left_frame, text="Station Name")
station_name_label.grid(row=0, column=0, sticky="w")
station_name_dropdown = ttk.Combobox(left_frame, values=['באר שבע', 'ערד', 'עבדת', 'מצפה רמון', 'פארן', "שדה בוקר"])
station_name_dropdown.grid(row=1, column=0, padx=5, pady=5, sticky="w")
station_name_dropdown.set("שדה בוקר")

river_name_label = ttk.Label(left_frame, text="River Name")
river_name_label.grid(row=2, column=0, sticky="w")
river_name_dropdown = ttk.Combobox(left_frame, values=["ציחור", "פארן - כביש הערבה", "חיון - כביש 40", "ערוד",
                                                       "יעלון - קיבוץ יהל", "רמון", "נקרות - עליון", "צין עליון - עבדת",
                                                       "ערוד", "נקרות - כביש הערבה", "הערבה-עין יהב"
    , "צין עליון - עבדת", "צין - עבדת", "צין-במעלה מפל", "צין - מפל", "צין - משוש", "צין- כביש הערבה",
                                                       "בשור-כביש נצנה החדש",
                                                       "בשור - כביש ניצנה", "חימר - במורד המצוק", "רחף", "צאלים",
                                                       "באר שבע - חצרים", "בשור - רעים", "גרר - רעים"])
river_name_dropdown.grid(row=3, column=0, padx=5, pady=5, sticky="w")
river_name_dropdown.set("בשור-כביש נצנה החדש")
# Repeat for the other text boxes and labels...
rain_amount_label = ttk.Label(left_frame, text="Rain Amount")
rain_amount_label.grid(row=4, column=0, sticky="w")
rain_amount_entry = ttk.Entry(left_frame)
rain_amount_entry.grid(row=5, column=0, padx=5, pady=5, sticky="w")

# Repeat for the other text boxes and labels...
humidity_label = ttk.Label(left_frame, text="Humidity")
humidity_label.grid(row=6, column=0, sticky="w")
humidity_entry = ttk.Entry(left_frame)
humidity_entry.grid(row=7, column=0, padx=5, pady=5, sticky="w")

# Repeat for the other text boxes and labels...
temperature_label = ttk.Label(left_frame, text="Temperature")
temperature_label.grid(row=8, column=0, sticky="w")
temperature_entry = ttk.Entry(left_frame)
temperature_entry.grid(row=9, column=0, padx=5, pady=5, sticky="w")

# Repeat for the other text boxes and labels...
rain_variance_label = ttk.Label(left_frame, text="Rain Variance")
rain_variance_label.grid(row=10, column=0, sticky="w")
rain_variance_entry = ttk.Entry(left_frame)
rain_variance_entry.grid(row=11, column=0, padx=5, pady=5, sticky="w")

# Repeat for the other text boxes and labels...
rain_amount_12h_label = ttk.Label(left_frame, text="12h Rain Before Score")
rain_amount_12h_label.grid(row=12, column=0, sticky="w")
rain_amount_12h_entry = ttk.Entry(left_frame)
rain_amount_12h_entry.grid(row=13, column=0, padx=5, pady=5, sticky="w")

# Repeat for the other text boxes and labels...
rain_amount_3h_label = ttk.Label(left_frame, text="3h Rain Before Score")
rain_amount_3h_label.grid(row=14, column=0, sticky="w")
rain_amount_3h_entry = ttk.Entry(left_frame)
rain_amount_3h_entry.grid(row=15, column=0, padx=5, pady=5, sticky="w")

# Repeat for the other text boxes and labels...
month_label = ttk.Label(left_frame, text="Month")
month_label.grid(row=16, column=0, sticky="w")
month_entry = ttk.Entry(left_frame)
month_entry.grid(row=17, column=0, padx=5, pady=5, sticky="w")

image_frame = ttk.Frame(root)
image_frame.grid(row=0, column=1)
input_image_path = "Images\\all_new.png"
output_image_path = "Images\\all.gif"
image = Image.open(input_image_path)
image.save(output_image_path, "GIF")
image_path = "Images\\all.gif"
img = tk.PhotoImage(file=image_path)
img = tk.PhotoImage(file=image_path)
image_label = tk.Label(image_frame, image=img)
image_label.image = img
image_label.grid(row=0, column=0)

message_label = tk.Label(root, text="", font=("Arial", 12))
message_label.grid(row=1, column=1, pady=20)

# Create button on the right side
right_frame = ttk.Frame(root)
right_frame.grid(row=0, column=2, padx=10, pady=10)

create_button = ttk.Button(right_frame, text="Check Flow", command=create_button_clicked)
create_button.grid(row=0, column=0)

# Start the Tkinter main loop
root.mainloop()

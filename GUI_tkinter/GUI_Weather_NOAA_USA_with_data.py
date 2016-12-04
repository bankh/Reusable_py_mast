### Examples regarding the installation as well as test is from the following
# http://tkinter.unpythonic.net/wiki/How_to_install_Tkinter

#=======================
# Imports
#=======================

import Tkinter as tk        # Python 3: "t" lower-case and Python
from Tkinter import Menu
import ttk                  # Themed Tkinter

# ======
# Front-end Functions
# =======

def _quit():
    win.quit()      # win will exist when this function is called
    win.destroy()
    exit()

# ========================================================================================
#  Procedural Code
# ========================================================================================
# Create instance
win = tk.Tk()

# Add a title
win.title("Python Projects")

# ========================================================================================
# Creating a Menu Bar
# ========================================================================================

menuBar = Menu()
win.config(menu=menuBar)

# Add menu items
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=_quit)
menuBar.add_cascade(label="File", menu=fileMenu)

# Add another Menu to the Menu Bar an Item
helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About")
menuBar.add_cascade(label="Help", menu=helpMenu)

# ========================================================================================
# Tab Control/ Notebook introduced here 
# ========================================================================================

tabControl = ttk.Notebook(win)                                          # Create Tab Control

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab 1')

tab2 = ttk.Frame(tabControl)                                            # Add a second tab
tabControl.add(tab2, text='Tab 2')

tabControl.pack(expand=1, fill="both")                                  # Pack to make visible

# =========================================================================================

# Create a container frame to hold all other widgets
weather_cities_frame = ttk.Labelframe(tab1, text="Latest Observation for ")
# Using the tkinter grid layout manager
weather_cities_frame.grid(column=0, row=0, padx=8, pady=4)

#

# Adding a label
ttk.Label(weather_cities_frame, text="Location:              ").grid(column=0, row=0, sticky='W')

city = tk.StringVar()
citySelected = ttk.Combobox(weather_cities_frame, width=24, textvariable=city)
citySelected['values'] = ('Los Angeles', 'London', 'Rio de Janerio')
citySelected.grid(column=1, row=0)
citySelected.current(0)

# =========================================================================================
# Create a container frame to hold all other widgets
weather_conditions_frame = ttk.Labelframe(tab1, text="Current Weather Conditions")
# Using the tkinter grid layout manager
weather_conditions_frame.grid(column=0, row=1, padx=8, pady=4)

# Increase combobox width to longest string
max_width = max([len(x) for x in citySelected['values']])
new_width = max_width
new_width = new_width - 4                                   # adjust per taste of extra spacing
citySelected.config(width=new_width)

# Adding Label & Textbox Entry Widgets
ENTRY_WIDTH = new_width
#============
ttk.Label(weather_conditions_frame, text="Last Updated:").grid(column=0, row=1, sticky='W')
updated = tk.StringVar()
updatedEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=updated, state='readonly')
updatedEntry.grid(column=1, row=1, sticky='W')
#============
ttk.Label(weather_conditions_frame, text="Weather:").grid(column=0,row=2,sticky='W') # Increment row for each
weather = tk.StringVar()
weatherEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=weather, state='readonly')
weatherEntry.grid(column=1, row=2, sticky='W')
#=============
ttk.Label(weather_conditions_frame, text="Temperature:").grid(column=0, row=3, sticky='W')
temp = tk.StringVar()
tempEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=temp, state='readonly')
tempEntry.grid(column=1, row='3', sticky='W')
#=============
ttk.Label(weather_conditions_frame, text="DevPoint:").grid(column=0, row=4, sticky='W')
dev = tk.StringVar()
devEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=dev, state='readonly')
devEntry.grid(column=1, row=4, sticky='W')
#=============
ttk.Label(weather_conditions_frame, text="Relative Humidity:").grid(column=0, row=5, sticky='W')
rel_humi = tk.StringVar()
rel_humiEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH,textvariable=rel_humi, state='readonly')
rel_humiEntry.grid(column=1, row=5, sticky='W')
#=============
ttk.Label(weather_conditions_frame, text="Wind: ").grid(column=0, row=6, sticky='W')
wind = tk.StringVar()
windEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=wind, state='readonly')
windEntry.grid(column=1, row=6, sticky='W')
#=============
ttk.Label(weather_conditions_frame, text="Visibility: ").grid(column=0, row=7, sticky='W')
visi = tk.StringVar()
visiEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=visi, state='readonly')
visiEntry.grid(column=1, row=7, sticky='W')
#=============
ttk.Label(weather_conditions_frame, text="MSL Pressure: ").grid(column=0, row=8, sticky='W')
msl = tk.StringVar()
mslEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=msl, state='readonly')
mslEntry.grid(column=1, row=8, sticky='W')
#=============
ttk.Label(weather_conditions_frame, text="Altimeter: ").grid(column=0, row=9, sticky='W')
alti = tk.StringVar()
altiEntry = ttk.Entry(weather_conditions_frame, width=ENTRY_WIDTH, textvariable=alti, state='readonly')
altiEntry.grid(column=1, row=9, sticky='W')

for child in weather_conditions_frame.winfo_children():
    # child.grid_configure(padx=6, pady=6)
    # child.grid_configure(padx=6, pady=3)
    child.grid_configure(padx=4, pady=2) # Adjust per visual spacing around the widgets

# NOAA DATA (National Oceanic and Atmospheric Administration) section starts here
# dict data below is a result from websearch
weather_data = {
    'devpoint_c': '16.7',
    'devpoint_f': '62.1',
    'icon_url_base': 'http://forecast.weather.gov.image/vtf/small',
    'devpoint_string': '62.1 F (16.7 C)',
    'icon_url_name': 'nect.png',
    'latitude': '33.92806',
    'location': 'Los Angeles, Los Angeles International Airport, CA',
    'longtitude': '-118.38889',
    'ob_url': 'http://www.weather.gov./data/METAR/KLAX.1.txt',
    'observation_time': 'Last Updated on Aug 7 2016, 9:53 pm PDT',
    'observation_time_rfc822': 'Sun, 07 Aug 2016 21:53:00 -0700',
    'pressure_in': '29.81',
    'pressure_mb': '1009.1',
    'pressure_string': '1009.1 mb',
    'relative_humidity': '84',
    'station_id': 'KLAX',
    'suggested_pickup': '15 minutes after the hour',
    'suggested_pickup_period': '60',
    'temp_c': '19.4',
    'temp_f': '67.0',
    'temperature_string': '67.0 F (19.4 C)',
    'two_day_history_url': 'http://www.weather.gov.data/obhistory/KLAX.html',
    'visibility_mi': '9.0',
    'weather': 'Partly Cloudy',
    'wind_degrees':'250',
    'wind_dir':'West',
    'wind_mpg':'6.9',
    'wind_string':'West at 6.9 MPH (6 KT)'
}

# We want to populate our GUI and we start by using dictionary
updated_data = weather_data['observation_time'].replace('Last Updated on ','')
# Next update the Entry widget with this data
updated.set(updated_data)

# Continue to do so for all other entry data
weather.set(weather_data['weather'])
temp.set('{} \xb0F ({} \b0C)'.format(weather_data['temp_f'], weather_data['temp_c']))
dev.set('{} \xb0F ({} \cb0C)'.format(weather_data['devpoint_f'], weather_data['devpoint_c']))
rel_humi.set(weather_data['relative_humidity'] + ' %')
wind.set(weather_data['wind_string'])
visi.set(weather_data['visibility_mi']+' miles')
msl.set(weather_data['pressure_string'])
alti.set(weather_data['pressure_in']+' in Hg')

# Start GUI
win.mainloop()
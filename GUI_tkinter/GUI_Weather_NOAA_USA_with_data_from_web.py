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
station_id_combo = ttk.Combobox(weather_cities_frame, width=24, textvariable=city)
station_id_combo['values'] = ('Los Angeles', 'London', 'Rio de Janerio')
station_id_combo.grid(column=1, row=0)
station_id_combo.current(0)

# =========================================================================================
# Create a container frame to hold all other widgets
weather_conditions_frame = ttk.Labelframe(tab1, text="Current Weather Conditions")
# Using the tkinter grid layout manager
weather_conditions_frame.grid(column=0, row=1, padx=8, pady=4)

# Increase combobox width to longest string
max_width = max([len(x) for x in station_id_combo['values']])
new_width = max_width
new_width = new_width - 4                                   # adjust per taste of extra spacing
station_id_combo.config(width=new_width)

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

##############################################################################################
#   TAB 2
# Creating a container frame to hold all other widgets
weather_states_frame = ttk.LabelFrame(tab2, text=' Weather Station IDs')
weather_states_frame.grid(columng=0, row=0, padx=8, pady=4)

# Adding a Label
ttk.Label(weather_states_frame, text="Select a state: ").grid(column=0, row=0) # Empty space for alignment

state = tk.StringVar()
state_combo = ttk.Combobox(weather_states_frame, width=5, textvariable=state)
state_combo['values'] = ('AL','AK', 'AK', 'CA', 'CO', 'CT', 'DE','','MI',
                         ''
                        )
state_combo.grid(column=1, row=0)
state_combo.current(0)

# Backend to initiate the extraction
def _get_station():
    station = station_id_combo.get()
    get_weather_data(station)
    populate_gui_from_dict()

get_weather_btn = ttk.Button(weather_cities_frame, text='Get Weather', command=_get_station).grid(column=2, row=0)

for child in weather_conditions_frame.winfo_children():
    # child.grid_configure(padx=6, pady=6)
    # child.grid_configure(padx=6, pady=3)
    child.grid_configure(padx=4, pady=2) # Adjust per visual spacing around the widgets

# NOAA DATA (National Oceanic and Atmospheric Administration) section starts here
# dict data below is a result from websearch
weather_data_tags_dict = {
    'observation_time': '',
    'weather': '',
    'temp_c': '',
    'temp_f': '',
    'devpoint_c': '',
    'devpoint_f': '',
    'relative_humidity': '',
    'wind_string':'',
    'visibility_mi': '',
    'pressure_string': '',
    'pressure_in': '',
    'location': ''
}

# Include online data
import urllib2

def get_weather_data(station_id='KLAX'):
    url_general = 'http://www.weather.gov/xml/current_obs/{}.xml'
    url = url_general.format(station_id)
    print(url)
    request = urllib2.urlopen(url)
    content = request.read().decode()

    # Using ElementTree to retrieve specific tags from the xml
    import xml.etree.ElementTree as ET 
    xml_root = ET.fromstring(content)
    print('xml_root: {}\n'.format(xml_root.tag))

    for data_point in weather_data_tags_dict.keys():
        weather_data_tags_dict[data_point] = xml_root.find(data_point).text

# We want to populate our GUI and we start by using dictionary
updated_data = weather_data_tags_dict['observation_time'].replace('Last Updated on ','')
# Next update the Entry widget with this data
updated.set(updated_data)

# Continue to do so for all other entry data
weather.set(weather_data_tags_dict['weather'])
temp.set('{} \xb0F ({} \b0C)'.format(weather_data_tags_dict['temp_f'], weather_data_tags_dict['temp_c']))
dev.set('{} \xb0F ({} \cb0C)'.format(weather_data_tags_dict['devpoint_f'], weather_data_tags_dict['devpoint_c']))
rel_humi.set(weather_data_tags_dict['relative_humidity'] + ' %')
wind.set(weather_data_tags_dict['wind_string'])
visi.set(weather_data_tags_dict['visibility_mi']+' miles')
msl.set(weather_data_tags_dict['pressure_string'])
alti.set(weather_data_tags_dict['pressure_in']+' in Hg')

# Start GUI
win.mainloop()

from guizero import App, Slider, Drawing, Text


def update_gauge(slider_value):

    # Convert the slider value from string to integer
    temp = int(float(slider_value))

    # Decide which range the temperature is in
    if temp == 0:
        status = "Engine Off"
        color = "black"
    elif 1 <= temp <= 194:
        status = "Engine Warming/Cooling"
        color = "blue"
    elif 195 <= temp <= 220:
        status = "Engine Temp Normal"
        color = "green"
    else:  # 221–300
        status = "Engine Overheated"
        color = "red"

    # Redraw the circle using the current temperature color
    led.clear()
    led.oval(10, 10, 150, 150, color=color)

    # Update the message text and text color
    message.value = f"{temp}°F : {status}"
    message.text_color = color

# Create the main application window
app = App(
    title="Engine Coolant Gauge",
    width=300,
    height=400,
    layout="grid"
)

# Title text at the top (row 0, centered across 2 columns)
title = Text(
    app,
    text="Coolant Temperature",
    grid=[0, 0, 2, 1],   # column, row, colspan, rowspan
    size=14,
    color="black"
)

# Vertical slider on the left (row 1)
slider = Slider(
    app,
    start=0,
    end=300,
    command=update_gauge,
    horizontal=False,    # make the slider vertical
    grid=[0, 1],
    height=300
)


# Drawing area for the circular indicator
led = Drawing(
    app,
    width=160,
    height=160,
    grid=[1, 1]
)


# Status message at the bottom (row 2, across 2 columns)
message = Text(
    app,
    text="0°F : Engine Off",
    grid=[0, 2, 2, 1],
    size=12,
    color="black"
)

# Make the grid fill the window width
app.tk.grid_columnconfigure(0, minsize=50)
app.tk.grid_columnconfigure(1, weight=1)

# Center the title across the window
title.tk.configure(width=1, anchor="center")
title.tk.grid(sticky="ew")

# Center the status text and wrap longer messages
message.tk.configure(
    width=1,
    wraplength=280,
    anchor="center",
    justify="center"
)
message.tk.grid(sticky="ew")

# Initialize the display for temperature 0
update_gauge("0")

# Start the GUI event loop
app.display()

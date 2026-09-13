# Engine Coolant Gauge

A Python coursework simulation built with guizero. Move a temperature slider to update a circular color indicator and a centered status message.

## Features

- Vertical slider from 0°F to 300°F.
- Circle and status text change color with the temperature.
- Centered text with wrapping for longer messages.
- Starts at 0°F with an Engine Off status.

## Temperature Ranges

| Temperature | Color | Status |
|---|---|---|
| 0°F | Black | Engine Off |
| 1–194°F | Blue | Engine Warming/Cooling |
| 195–220°F | Green | Engine Temp Normal |
| 221–300°F | Red | Engine Overheated |

These ranges follow the coursework logic. This application does not read engine sensors or provide vehicle diagnostic advice.

## Requirements

- Python 3 with Tkinter support
- guizero

Tested with Python 3.13 on Windows using PyCharm.

## How to Run

Open a terminal in the project folder.

Install the required package:

```text
python -m pip install -r requirements.txt
```

Start the application:

```text
python engine_coolant_gauge.py
```

Move the slider to change the simulated temperature.

## Project Files

- `engine_coolant_gauge.py` — application code.
- `requirements.txt` — required Python package.
- `.gitignore` — excludes local environment and editor files.

## Skills Practiced

- GUI development with guizero
- Slider callbacks and event handling
- Conditional logic and temperature ranges
- Drawing and updating shapes
- Text formatting and grid layout

## Improvements

Replaced the original grid of colored squares with a solid circular indicator. Adjusted the layout to keep the title and status message centered as the temperature changes.

## Checks Performed

- Launched the application from the terminal.
- Checked colors at 0, 1, 194, 195, 220, 221, and 300°F.
- Checked text alignment while moving the slider.
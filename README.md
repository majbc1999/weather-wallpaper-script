# Desktop background on Windows 10, based on current weather and time
A python script that changes your computer's desktop background based on current weather and time of the day. The weather is obtained from `https://openweathermap.org/` API.

## Steps
1. Register to `https://openweathermap.org/` for free and generate your free API key. The default one should look something like: `93aa1ae52d8df6151ee049fid863a3q0`. Then copy paste your API key to the `api_key ` variable.
2. Save the photos you want for each weather and time of the day in any folder you want (just make sure to remember absolute path to your map and save it to `path_to_photos` variable). Make sure that photos have names: `thunderstorm.jpg` if the weather is thunderstorms, `rain.jpg` for rainy weather, `snow.jpg` if it snows, `fog.jpg` for foggy weather, `clear.jpg` for clear sky, `clear_night.jpg` for clear sky at night and `clouds.jpg` for cloudy weather.
3. Convert `main.py` file to `main.exe` file and put it in your StartUp folder that the program will run everytime you start your computer:
    - [converting from `.py` to `.exe` using `auto-py-to-exe` tool](https://pypi.org/project/auto-py-to-exe/)
    - [automatic run on computer start up](https://www.computroon.co.uk/2020/11/12/how-to-autorun-programs-on-startup-in-windows-10/)
    - if you want your wallpaper to update every some time (for example every half hour), you can do that with [Task scheduler](https://www.windowscentral.com/how-create-automated-task-using-task-scheduler-windows-10).
4. Done

## Results
Background image based on weather and time of the day:
| weather, time | day | night |
| :---        |    :----:   |          :---: |
| clear      | `clear.jpg` | `clear_night.jpg`  |
| cloudy   | `clouds.jpg` | `clouds.jpg` |
| rainy      | `rain.jpg` | `rain.jpg` |
| thunderstorm   | `thunderstorm.jpg`        | `thunderstorm.jpg`     |
| snowy      | `snow.jpg` | `snow.jpg` |
| foggy | `fog.jpg` | `fog.jpg` |

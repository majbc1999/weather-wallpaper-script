# Desktop background on Windows 10, based on current weather and time
A python script that changes our background based on current weather and time of the day. The weather is obtained from `https://openweathermap.org/` API.

## Steps
1. Register to `https://openweathermap.org/` for free and generate your free API key. The default one should look something like: `93aa1ae52d8df6151ee049fid863a3q0`. Then copy paste your API key to the `api_key ` variable.
2. Save the photos you want for each season, time of the day and weather in any map you want (just make sure to remember absolute path to your map and save it to `path_to_photos` variable). Make sure that map with photos is organized as noted below:     
    - photos
        - autumn
            - day
                - snowy.jpg
                - clear.jpg
                - rainy.jpg
                - cloudy.jpg
            - night
                - snowy.jpg
                - clear.jpg
                - rainy.jpg
                - cloudy.jpg
        - spring
        - summer
        - winter
3. Convert `main.py` file to `main.exe` file and put it in your StartUp folder that the program will run everytime you start your computer:
    - [converting from `.py` to `.exe` using `auto-py-to-exe` tool](https://pypi.org/project/auto-py-to-exe/)
    - [automatic run on computer start up](https://www.computroon.co.uk/2020/11/12/how-to-autorun-programs-on-startup-in-windows-10/)
4. Done. You can manually change photos whenever you want.

# Facebook Pages Or Groups Checker
This is a simple Python script that allows you to check if a list of Facebook Pages or Groups is active or not. It uses the Selenium WebDriver to open each page and check if the page title contains the word "Facebook". The results are displayed in a table using the Tkinter library.

The script also includes a GUI that displays the results in a table, with the URL of each page and a Yes/No flag indicating if the page is active or not.

## Requirements
To run this script, you will need:

* Python 3.6 or later
* Selenium WebDriver for Chrome
* Tkinter library
* Pandas library
You can install the required libraries using pip:
pip install selenium pandas
## Usage
1. Clone this repository to your local machine or download the ***`main.py`*** file.
2. Install the required libraries as mentioned above.
3. Download and install the Selenium WebDriver for Chrome from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads/ "Selenium WebDriver for Chrome").
4. Open the command prompt or terminal and navigate to the directory where the script is saved.
5. Run the script using the this command: ***`python main.py`***
6. This will launch the GUI, where you can enter the number of Facebook pages to check, and click the "Start" button to begin the process.
7. The results will be displayed in a table.
## Stop the Process
You can stop the process at any time by clicking on the "Stop" button in the GUI.
## Limitations
The script relies on the Facebook page title to determine if a page or group is active or not, so it may not be accurate for pages with custom titles. Additionally, it does not take into account pages that are active but inaccessible (e.g., due to age restrictions or location-based access controls).
## Credits
This script was created by ***`Zain Ali`***, and is made available under the MIT License. Feel free to use it for any purpose, commercial or non-commercial. If you have any questions or issues, please contact ***`zainali68598@gmail.com`***.

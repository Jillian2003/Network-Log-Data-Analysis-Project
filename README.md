# Data Analytics for Network Security

## Project Overview
The purpose of the project is to collect network log data from Cisco Firepower Management Center, convert those logs from PDF to CSV using Excel, clean and organize the data, sort IP addresses into public and private categories and then map the public IP addresses to geolocations using Python scripts.

## Features
- **Data Extraction**: Extracts data from PDF reports using Excel.
- **Data Cleaning**: Cleans and organizes the extracted data into a usable format.
- **IP Sorting**: Uses the `ipaddress` module to sort IP addresses into public and private categories.
- **Geolocation Mapping**: Maps public IP addresses to their geographical locations and visualizes them in an HTML file using Folium.

## Project Structure
- `script.py`: The main script that processes and maps the data.
- `README.md`: Project documentation (this file).
- `requirements.txt`: List of Python dependencies required for the project.
- `.gitignore`: Specifies files and directories to be ignored by Git.

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- pip (Python package installer)
- Microsoft Excel (or any tool that can convert PDF to CSV)

## Installation
1. **Clone the repository**:
   ```sh
   git clone https://github.com/Jillian2003/Volusia-County-Data-Security-.git
   cd Volusia-County-Data-Security-
   
2. **Install the required Python packages**:
   pip install -r requirements.txt

## Usage
1. Convert the PDF report from Cisco Firepower FMC to CSV using Excel:
   - Open the PDF report in Excel.
   - Save the file as a CSV (e.g., Logs.csv).
2. Place the CSV file in the project directory.
3. Run the script:
   python script.py

4. View the output:
   The script will generate a cleaned CSV file ('Blockedi_geolocations.csv').
   It will also create an HTML file ('Blocked_map.html') with a map showing the geolocations of the public IP addresses.

## Dependencies
- pandas: Data manipulation and analysis library.
- folium: Library for generating interactive maps.
- ipinfo: Library for IP address geolocation.
- ipaddress: Library for handling and manipulating IP addresses.

You can install these dependencies using:
pip install pandas folium ipinfo ipaddress

## Contributing 
If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.



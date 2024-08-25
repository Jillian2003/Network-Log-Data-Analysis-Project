# Data Analytics for Network Security at Company A

## Project Overview
The goal of this project is to analyze network log data to identify and map public IP addresses that have been blocked by Company A's Server. The logs are first extracted, cleaned, and organized, followed by categorization of IP addresses using Python scripts. The Logs are then loaded into a compelling Power BI dashboard that encompases the data?? 

## Features
- **Data Extraction**: Converts network log data from PDF reports to CSV format using Excel.
- **Data Cleaning** : Processes and organizes the extracted data for further analysis.
- **IP Sorting**: Categorizes IP addresses into public and private using the ipaddress module.
- **Visualization**:
  
## Tools and Technologies Used
- **Python**: The primary programming language used for data processing and analysis.
   - pandas: A powerful data manipulation and analysis library used to clean and organize the data.
   - ipaddress: A module used to differentiate between public and private IP addresses.
   - ipinfo: A library that fetches geolocation information for IP addresses.
   - folium: A library used to generate interactive maps for geolocation visualization.
- **Excel**: Used to convert PDF network logs into CSV format for processing.
- **Jupyter Notebook** : For interactive data exploration and analysis during development.
- **Power BI** : Used for creating advanced visualizations and dashboards, helping to convey insights from the processed data effectively.

## Project Structure
- `script.py`: The main script that processes and maps the data.
- `README.md`: Project documentation (this file).
- `requirements.txt`: List of Python dependencies required for the project.
- `.gitignore`: Specifies files and directories to be ignored by Git.
- ' power bi

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- pip (Python package installer)
- Microsoft Excel (or any tool that can convert PDF to CSV)
- power bi 

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



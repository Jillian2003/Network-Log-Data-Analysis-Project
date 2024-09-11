# Network Log Data Analysis Project

## Project Overview

The objective of this project is to analyze network log data to identify and visualize public IP addresses that have been blocked within an organization's network. The data is extracted, cleaned, and organized, followed by categorization of IP addresses using custom scripts. The processed data is then presented in a structured HTML file, providing a clear and accessible overview of the findings.

## Features

- **Data Extraction**: Converts network log data from various formats (such as PDF reports) to CSV format for analysis.
- **Data Cleaning**: Processes and organizes the extracted data to ensure it is suitable for analysis.
- **IP Address Categorization**: Differentiates between public and private IP addresses using Python modules.
- **Geolocation Visualization**: Maps the geolocation of identified IP addresses to provide visual insights.

## Tools and Technologies Used

- **Python**: Used for data processing and analysis.
  - `pandas`: For data manipulation and cleaning.
  - `ipaddress`: To differentiate between public and private IP addresses.
  - `ipinfo`: To fetch geolocation information for IP addresses.
  - `folium`: To generate interactive maps for geolocation visualization.
- **Excel**: Used for converting network logs from PDF to CSV format.
- **Jupyter Notebook**: For interactive data exploration and analysis during development.

## Project Structure

- `script.py`: The main script that processes network log data and generates visualizations.
- `README.md`: Project documentation (this file).
- `requirements.txt`: List of Python dependencies required for the project.
- `.gitignore`: Specifies files and directories to be ignored by Git.

## Prerequisites

Ensure you have the following installed:

- Python 3.x
- pip (Python package installer)
- A tool to convert PDF to CSV (e.g., Microsoft Excel)

## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/Jillian2003/Network-Log-Data-Analysis.git
   cd Network-Log-Data-Analysis
   ```

2. **Install the required Python packages**:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Convert the network log report to CSV using a suitable tool (e.g., Microsoft Excel):
   - Open the report in the tool.
   - Save the file as a CSV (e.g., `Logs.csv`).
   
2. Place the CSV file in the project directory.

3. Run the script:
   ```sh
   python script.py
   ```

4. View the output:
   - The script will generate a cleaned CSV file (`Blocked_IP_geolocations.csv`).
   - It will also create an HTML file (`Blocked_map.html`) with a map showing the geolocations of the public IP addresses.

## Dependencies

- `pandas`: Data manipulation and analysis library.
- `folium`: Library for generating interactive maps.
- `ipinfo`: Library for IP address geolocation.
- `ipaddress`: Library for handling and manipulating IP addresses.

Install these dependencies using:

```sh
pip install pandas folium ipinfo ipaddress
```

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.





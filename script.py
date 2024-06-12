'''
Make a dataframe that has the columns : 
Initiator Ips, Responder Ips and responder ports of
users that were allowed and those who were blocked
'''

#----------------> Import the csv file and split the columns Source Port / ICMP Type and Destination Port/ ICMP Code for easier translation <------------

pip install pandas ipinfo folium

import pandas as pd

df = pd.read_csv('Logs2.csv')

# Split the 'Source Port / ICMP Type' column
df[['Source Port', 'ICMP Type']] = df['Source Port / ICMP Type'].str.split(' / ', expand=True)

# Split the 'Destination Port / ICMP Code' column
df[['Destination Port', 'ICMP Code']] = df['Destination Port / ICMP Code'].str.split(' / ', expand=True)

# Drop the original columns
df.drop(columns=['Source Port / ICMP Type', 'Destination Port / ICMP Code'], inplace=True)

# Convert 'Source Port' and 'Destination Port' to numeric if needed
df['Source Port'] = pd.to_numeric(df['Source Port'], errors='coerce')
df['Destination Port'] = pd.to_numeric(df['Destination Port'], errors='coerce')

# Display the DataFrame
print(df)

# -------------> Clean the data to only get Ips from users who were blocked and only keep the ones that are public in a new file <---------
import ipaddress

block = df[df["Action"] == "Block"]
subset_df = block[['Initiator IP', 'Responder IP', 'ICMP Type', 'Destination Port', 'ICMP Code']]

def is_private_ip(ip):
    return ipaddress.ip_address(ip).is_private

# Apply the function to both columns
subset_df['Initiator IP Is Private'] = subset_df['Initiator IP'].apply(is_private_ip)
subset_df['Responder IP Is Private'] = subset_df['Responder IP'].apply(is_private_ip)

# Filter out rows with private IPs in either column
public_ips_df = subset_df[(subset_df['Initiator IP Is Private'] == False) & (subset_df['Responder IP Is Private'] == False)]

# Drop the helper columns
public_ips_df = public_ips_df.drop(columns=['Initiator IP Is Private', 'Responder IP Is Private'])

# Save the result to a new CSV file
public_ips_df.to_csv('Blocked Ips with ports.csv', index=False)

print("Public IP addresses have been exported to Blocked Ips with ports.csv")

#-------------------> Convert the Ip addresses to longitude and latitude formats for easy mapping <---------------------

import ipinfo
import folium

# Load your DataFrame from the CSV containing both initiator and responder IPs
df = pd.read_csv('Blocked Ips with ports.csv')

# Print the column names to verify
print(df.columns)

# Initialize ipinfo handler with your access token
access_token = 'your_access_token'
handler = ipinfo.getHandler(access_token)

# Function to get geolocation for an IP address
def get_geolocation(ip):
    details = handler.getDetails(ip)
    latitude = details.latitude
    longitude = details.longitude
    return latitude, longitude

# Create lists to store geolocations
initiator_latitudes = []
initiator_longitudes = []
responder_latitudes = []
responder_longitudes = []

# Loop through the IP addresses and get geolocations for both initiator and responder IPs
for index, row in df.iterrows():
    # Process Initiator IP
    initiator_ip = row['Initiator IP']
    try:
        lat, lon = get_geolocation(initiator_ip)
        initiator_latitudes.append(float(lat))
        initiator_longitudes.append(float(lon))
    except Exception as e:
        print(f"Could not retrieve geolocation for Initiator IP {initiator_ip}: {e}")
        initiator_latitudes.append(None)
        initiator_longitudes.append(None)
    
    # Process Responder IP
    responder_ip = row['Responder IP']
    try:
        lat, lon = get_geolocation(responder_ip)
        responder_latitudes.append(float(lat))
        responder_longitudes.append(float(lon))
    except Exception as e:
        print(f"Could not retrieve geolocation for Responder IP {responder_ip}: {e}")
        responder_latitudes.append(None)
        responder_longitudes.append(None)

# Add geolocations to DataFrame
df['Initiator Latitude'] = initiator_latitudes
df['Initiator Longitude'] = initiator_longitudes
df['Responder Latitude'] = responder_latitudes
df['Responder Longitude'] = responder_longitudes

# Save the result to a new CSV file
df.to_csv('Blockedi_geolocations.csv', index=False)
print("done")

#-------------> Map the ips and save to a html file >-----------------------

import pandas as pd
import folium

# Read the CSV files into DataFrames
df = pd.read_csv('Blockedi_geolocations.csv')

# Merge the DataFrames on a common column (assuming 'Initiator IP')
#merged_df = pd.merge(df, logs_df[['Initiator IP', 'First Packet']], on='Initiator IP', how='left')

# Initialize the map
m = folium.Map(location=[0, 0], zoom_start=2)

# Define colors for initiator and responder IPs
initiator_color = 'blue'
responder_color = 'red'

# Check if 'Last Packet' column exists in the DataFrame
#has_last_packet = 'Last Packet' in merged_df.columns

# Add markers for each row in the DataFrame
for index, row in df.iterrows():
    # Add marker for initiator IP
    initiator_popup = (f"Initiator IP: {row['Initiator IP']}<br>"
                    #   f"First Packet: {row['First Packet']}<br>"
                      # f"{'Last Packet: ' + str(row['Last Packet']) + '<br>' if has_last_packet else ''}"
                       f"ICMP Type: {row['ICMP Type']}<br>"
                       f"Destination Port: {row['Destination Port']}")
    folium.Marker([row['Initiator Latitude'], row['Initiator Longitude']], 
                  icon=folium.Icon(color=initiator_color),
                  popup=initiator_popup).add_to(m)
    
    # Add marker for responder IP
    responder_popup = (f"Responder IP: {row['Responder IP']}<br>"
                   #    f"First Packet: {row['First Packet']}<br>"
                      # f"{'Last Packet: ' + str(row['Last Packet']) + '<br>' if has_last_packet else ''}"
                       f"ICMP Type: {row['ICMP Type']}<br>"
                       f"Destination Port: {row['Destination Port']}")
    folium.Marker([row['Responder Latitude'], row['Responder Longitude']], 
                  icon=folium.Icon(color=responder_color),
                  popup=responder_popup).add_to(m)

# Save the map to an HTML file
m.save('Blocked_map.html')









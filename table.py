import json
import pandas as pd
import openpyxl

def load_data(file_path):
    # Reading the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def extract_rssi_values_to_dataframe(data):
    # Initialize a dictionary to hold lists of RSSI values by MAC address
    rssi_values_by_mac = {}

    # Extracting RSSI values
    for item in data:
        wifi_fingerprint = item["INSTANCE"]["mWiFiFingerprint"]
        for mac, rssi in wifi_fingerprint.items():
            if mac not in rssi_values_by_mac:
                rssi_values_by_mac[mac] = []
            rssi_values_by_mac[mac].append(rssi)

    # Convert dictionary to DataFrame for easier manipulation and display
    # Using pd.DataFrame directly to handle varying lengths of lists
    df_rssi = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in rssi_values_by_mac.items()]))
    return df_rssi

def generate_statistics(df_rssi):
    # Calculate descriptive statistics for each MAC address column
    stats = df_rssi.describe().transpose()  # transpose to have MAC addresses as rows
    return stats

def main():
    # Path to the JSON file
    file_path = 'single_fingerprint.json'

    # Load and process data
    data = load_data(file_path)
    df_rssi_values = extract_rssi_values_to_dataframe(data)
    stats = generate_statistics(df_rssi_values)

    # Save the statistics to an Excel file
    output_file_path = 'RSSI_Statistics.xlsx'
    with pd.ExcelWriter(output_file_path, engine='openpyxl') as writer:
        stats.to_excel(writer, sheet_name='RSSI Data')

    print(f"RSSI data has been saved to {output_file_path}")

if __name__ == "__main__":
    main()

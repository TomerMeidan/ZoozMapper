import json
import pandas as pd

def load_data(file_path):
    # Load JSON data from a file
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def find_common_mac_addresses(data):
    # Identify common MAC addresses across all fingerprints
    common_macs = None
    for entry in data:
        current_macs = set(entry["INSTANCE"]["mWiFiFingerprint"].keys())
        if common_macs is None:
            common_macs = current_macs
        else:
            common_macs &= current_macs
    return common_macs

def process_data(data, common_macs):
    # Organize data for DataFrame with OBJECT INDEX as columns and MAC addresses as rows
    object_index_dict = {}
    for entry in data:
        object_index = entry["OBJECT INDEX"]
        for mac in common_macs:
            rssi = entry["INSTANCE"]["mWiFiFingerprint"][mac]
            if mac not in object_index_dict:
                object_index_dict[mac] = {}
            object_index_dict[mac][object_index] = rssi

    # Convert dictionary to DataFrame
    df = pd.DataFrame(object_index_dict).T
    df.index.name = 'MAC Address'
    df.columns.name = 'OBJECT INDEX'
    return df

def save_to_excel(df, filename='Common_Fingerprint_Data.xlsx'):
    # Save DataFrame to an Excel file
    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Common WiFi Fingerprint')

def main():
    file_path = 'test.json'  # Set the path to your JSON file
    data = load_data(file_path)
    common_macs = find_common_mac_addresses(data)
    df = process_data(data, common_macs)
    save_to_excel(df)

if __name__ == "__main__":
    main()

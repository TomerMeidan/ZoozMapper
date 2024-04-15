# single.py

import json
import matplotlib.pyplot as plt

def load_data(file_path):
    # Reading the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def extract_rssi_values(data):
    # Dictionary to hold RSSI values by MAC address
    rssi_values_by_mac = {}
    # Extracting RSSI values
    for item in data:
        wifi_fingerprint = item["INSTANCE"]["mWiFiFingerprint"]
        for mac, rssi in wifi_fingerprint.items():
            if mac not in rssi_values_by_mac:
                rssi_values_by_mac[mac] = []
            rssi_values_by_mac[mac].append(rssi)
    return rssi_values_by_mac

def filter_mac_addresses(rssi_values_by_mac, threshold=10):
    # Filter out MAC addresses with fewer than 'threshold' tests
    filtered_rssi_values = {mac: rssi for mac, rssi in rssi_values_by_mac.items() if len(rssi) >= threshold}
    return filtered_rssi_values

def create_line_plot(rssi_values_by_mac):
    # Prepare data for plotting
    plt.figure(figsize=(14, 7))
    for mac, rssi_values in rssi_values_by_mac.items():
        # Plot each MAC address RSSI values across tests with markers
        plt.plot(rssi_values, marker='o', label=mac)

    plt.title('RSSI Values Stability Over Multiple Tests at a Single Location')
    plt.xlabel('Test Number')
    plt.ylabel('RSSI Value')
    plt.grid(True)
    plt.legend(title='MAC Addresses', loc='upper right', bbox_to_anchor=(1.15, 1))
    plt.tight_layout()
    plt.show()

def main():
    # Path to the JSON file
    file_path = 'single_fingerprint.json'

    # Load and process data
    data = load_data(file_path)
    rssi_values_by_mac = extract_rssi_values(data)
    filtered_rssi_values = filter_mac_addresses(rssi_values_by_mac)
    create_line_plot(filtered_rssi_values)

if __name__ == "__main__":
    main()

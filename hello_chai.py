# print('Chai aur Python')

# def chai(num):
#     print(num)
   

# chai(10)
# chai(20)

# Data Types In Python

# 1. Number
# 2. String
# 3. Boolean
# 4. List -> [1,2,3]
# 5. Tuple -> (1,2,3)
# 6. Dictionaries = {'key1':1,'key'2:2,'key3':3}
#7. Sets -> only stores unique values -> {'a','b','c'}
# 8. File -> open('file.txt')
# 9. None : None
# 10. Functions
# 11. Modules
# 12. Classes
# 13. Advance Types -> Generators,Decorators,Iterators,Comprehensions,MetaProgramming







import subprocess
import platform
import sys
import ctypes

def run_command(command):
    """Run a system command and return the output."""
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        return None

def check_existing_profiles(ssid):
   
    command = ["netsh", "wlan", "show", "profiles"]
    output = run_command(command)
    
    if output and ssid in output:
        return True  
    return False  

def create_wifi_profile(ssid, password):
    """Create a new Wi-Fi profile for the network (Windows)."""
    profile_xml = f"""<?xml version="1.0"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    <name>{ssid}</name>
    <SSIDConfig>
        <SSID>
            <name>{ssid}</name>
        </SSID>
    </SSIDConfig>
    <connectionType>ESS</connectionType>
    <connectionMode>auto</connectionMode>
    <MSM>
        <security>
            <authEncryption>
                <authentication>WPA2PSK</authentication>
                <encryption>AES</encryption>
                <useOneX>false</useOneX>
            </authEncryption>
            <sharedKey>
                <keyType>passPhrase</keyType>
                <protected>false</protected>
                <keyMaterial>{password}</keyMaterial>
            </sharedKey>
        </security>
    </MSM>
</WLANProfile>"""

    profile_path = f"{ssid}.xml"
    with open(profile_path, "w") as file:
        file.write(profile_xml)

   
    command = ["netsh", "wlan", "add", "profile", f"filename={profile_path}"]
    run_command(command)

def connect_wifi(ssid, password):
    """Attempt to connect to a Wi-Fi network, creating a new profile if needed."""
    os_name = platform.system()
    
    if os_name == "Windows":
       
        if not check_existing_profiles(ssid):
            print(f"Profile for {ssid} not found. Creating new profile...")
            create_wifi_profile(ssid, password)

       
        command = ["netsh", "wlan", "connect", f"name={ssid}"]
    elif os_name == "Linux":
       
        command = ["nmcli", "d", "wifi", "connect", ssid, "password", password]
    else:
        print("Unsupported OS")
        return False

    output = run_command(command)
    if output:
        print(output)
        return True
    else:
        print("Connection attempt failed.")
        return False

def main():
    os_name = platform.system()

    if os_name == "Windows":
        command = ["netsh", "wlan", "show", "networks", "mode=Bssid"]
        if not ctypes.windll.shell32.IsUserAnAdmin():
            print("This script requires administrative privileges. Please run as an administrator.")
            sys.exit(1)
    elif os_name == "Linux":
        command = ["nmcli", "device", "wifi", "list"]
    else:
        print("Unsupported OS")
        sys.exit(1)

    output = run_command(command)
    if output:
        print(output)

  
    ssids = []
    lines = output.splitlines()
    for line in lines:
        if "SSID" in line and ":" in line:
            parts = line.split(":")
            if len(parts) > 1:
                ssid = parts[1].strip()
                if ssid:  
                    ssids.append(ssid)

  
    print("\nAvailable SSIDs:")
    for i, ssid in enumerate(ssids):
        print(f"{i+1}. {ssid}")

    choice = input("\nEnter the number of the SSID you want to connect to: ")
    try:
        choice = int(choice)
        if choice < 1 or choice > len(ssids):
            print("Invalid choice.")
            return
    except ValueError:
        print("Invalid input.")
        return

    selected_ssid = ssids[choice - 1]
    password = input("Enter the password for the selected SSID: ")

   
    if connect_wifi(selected_ssid, password):
        print(f"Connected to {selected_ssid} successfully.")
    else:
        print(f"Failed to connect to {selected_ssid}.")

if __name__ == "__main__":
    main()


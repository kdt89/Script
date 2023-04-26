import wmi
import subprocess

NETWORK_NAME = 'ADWLAN-OA'
SUBNETMASK = u'255.255.255.0'
MAX_RETRY_CONNECT = 5


# function to check if specific network is connected
def is_connected(networkname: str) -> bool:

    retVal = False

    try:
        # Execute the netsh command to check the Wi-Fi network status
        result = subprocess.run("netsh wlan show interfaces", capture_output=True, text=True)

        # Check if the specified Wi-Fi network is connected
        if networkname in result.stdout: #and "State       : connected" in result.stdout:
            print(f"Successfully connected to {networkname}")
            retVal = True
        else:
            print(f"Failed to connect to {networkname}")
            retVal = False
    except:
        print("Failed to check current network name")
        retVal = False

    return retVal


# Unfilter network list using Windows command
subprocess.run(f'netsh wlan delete filter permission=denyall networktype=infrastructure', shell=True)

# Obtain network adaptors configurations
nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)

# First network adaptor
nic = nic_configs[0]

# Note: EnableStatic() and SetGateways() methods require *lists* of values to be passed
# nic.EnableStatic(IPAddress=[IP],SubnetMask=[SUBNETMASK])
# nic.SetGateways(DefaultIPGateway=[GATEWAY])

# Enable DHCP
nic.EnableDHCP()

print("Set IP to Dynamic IP successfully")

# Loop to connect Wifi to specific network using the netsh command on Windows
retry = 0

while (not is_connected(NETWORK_NAME)) and (retry <= MAX_RETRY_CONNECT):

    try:
        print(f"Try {retry}/{MAX_RETRY_CONNECT}...")
        subprocess.run(f'netsh wlan connect name="{NETWORK_NAME}"', shell=True)
    except: 
        print("Failed to set system connect to network" + NETWORK_NAME)
    
    retry += 1


print("Exiting...") 
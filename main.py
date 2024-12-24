import bluetooth

n = 0

# Replace with your HC-05 MAC address
hc05_mac_address = '20:16:11:21:87:80'  # Example: '00:11:22:33:44:55'
port = 1  # Common port for RFCOMM

# Create a socket to connect to the HC-05 module
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

try:
    sock.connect((hc05_mac_address, port))
    print("Connected to HC-05")

    while True:
        data = sock.recv(1)  # Receive a single byte from the Bluetooth device
        if data == b'\x01':  # Check if the received byte is 1 (vibration detected)
            n += 1 
            print(f"Vibration detected! Count: {n}")  # Print message when vibration is detected
        elif data == b'\x00':  # Check if the received byte is 0 (no vibration)
            print("No vibration detected.")

except bluetooth.btcommon.BluetoothError as e:
    print(f"Bluetooth error: {e}")

finally:
    sock.close()

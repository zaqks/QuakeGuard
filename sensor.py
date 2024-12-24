import bluetooth


MAC, PORT = '20:16:11:21:87:80', 1


sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

try:
    sock.connect((MAC, PORT))
    print("Connected to HC-05")

    while True:
        data = sock.recv(1)
        if data == b'\x01':            
            with open("sensor", "w")as f:
                f.write("1")
        # elif data == b'\x00':
        #     print("No vibration detected.")

except bluetooth.btcommon.BluetoothError as e:
    print(f"Bluetooth error: {e}")

finally:
    sock.close()

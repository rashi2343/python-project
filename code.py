import serial

def send_data_to_com_port(bin_file_path, port_name, baud_rate):
    # Open the COM port
    ser = serial.Serial(port=port_name, baudrate=baud_rate)
    
    try:
        # Send 3 bytes of data (b'\x00\x00\x00') to the COM port
        ser.write(b'\x00\x00\x00')
        
        # Wait for a reply
        reply = ser.read(1)
        
        # Check if the reply is '00'
        if reply == b'\x00':
            print("Communication successful!")
            
            # Send the checksum output
            checksum = calculate_checksum(bin_file_path)
            ser.write(checksum.to_bytes(2, 'big'))
            print("Checksum sent successfully!")
        else:
            print("Communication failed!")
    
    finally:
        # Close the COM port
        ser.close()

def calculate_checksum(bin_file_path):
    # Calculate the checksum of the binary file (example implementation)
    with open(bin_file_path, 'rb') as file:
        data = file.read()
        checksum = sum(data) & 0xFFFF  # Example checksum calculation
    return checksum

# Prompt the user for inputs
bin_file_path = input("Enter the absolute path of the binary file: ")
port_name = input("Enter the COM port name: ")
baud_rate = int(input("Enter the baud rate: "))

# Call the function to send data to the COM port
send_data_to_com_port(bin_file_path, port_name, baud_rate)

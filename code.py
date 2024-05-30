import board
import busio
import digitalio

# For most CircuitPython boards:
buzzer = digitalio.DigitalInOut(board.GP11)
buzzer.switch_to_output()

uart = busio.UART(board.GP8, board.GP9, baudrate=115200)

distance = 0

while True:
    data = uart.readline()  # read one line

    if data is not None:

        # convert bytearray to string
        data_string = ''.join([chr(b) for b in data])
        # print(data_string)
        if data_string.startswith("Distance") :
            print(data_string[11:19])
            distance = float(data_string[11:19])
        else:
            print(data_string)
        if distance > 6.5:
            buzzer.value = True
        else:
            buzzer.value = False

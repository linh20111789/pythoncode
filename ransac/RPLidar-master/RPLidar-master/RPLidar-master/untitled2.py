import serial.tools.list_ports as port_list
import serial
ports = list(port_list.comports())
for p in ports:
    print (p)
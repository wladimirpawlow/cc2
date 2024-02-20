from mod.modBusTCP import mbRead
from mod.modBusRTU import mbRTURead
import serial.tools.list_ports

print('start EW')
# ports = serial.tools.list_ports.comports()
# for port, desc, hwid in sorted(ports):
#     print("{}: {} [{}]".format(port, desc, hwid))


mbRTURead()




print('all tasks are done')
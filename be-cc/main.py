# import serial.tools.list_ports
from mb_work.mod_bus_tcp import mbTCPRead
from mb_work.mod_bus_rtu import mbRTURead

print('start EW')
# ports = serial.tools.list_ports.comports()
# for port, desc, hwid in sorted(ports):
#     print("{}: {} [{}]".format(port, desc, hwid))

mbTCPRead()
mbRTURead()




print('all tasks are done')
from pymodbus.client import ModbusSerialClient
from pymodbus.transaction import ModbusRtuFramer as ModbusFramer

client = ModbusSerialClient(
            port='COM2',
            framer=ModbusFramer,
            # framer=framer,
            timeout=100,
            # retries=3,
            # retry_on_empty=False,
            # strict=True,
            method='rtu',
            baudrate=9600,
            bytesize=8,
            parity="N",
            stopbits=1,
            # handle_local_echo=False,
        )

def mbRTURead():
    try:
        client.connect()
        while 1:
            result = client.read_holding_registers(0, 5, slave=1)
            print(result.registers)

    except Exception:
        print('something unknown happened')
    finally:
        client.close()
        print('connection closed')
import sys
import telnetlib
import time

HOST = "192.168.0.1"
password = "SPOTLIGHT-2907-HK!"
port = 23

try:
    print('Opening Telnet Connection to Router.')
    with telnetlib.Telnet(HOST, port, timeout=10) as tn:
        tn.read_until(b'password:', 10)
        print('Sending password to Router.')
        tn.write((password + '\r\n').encode('ascii'))
        time.sleep(1)
        tn.read_until(b'(conf)#', 10)
        print('Rebooting the Router!!!')
        tn.write(('dev reboot' + '\r\n').encode('ascii'))
        time.sleep(5)

except EOFError:
    print("Unexpected response from router")
except ConnectionRefusedError:
    print("Connection refused by router. Telnet enabled?")
except:
    print("Error")

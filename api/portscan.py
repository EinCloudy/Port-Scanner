import socket
import sys


class PortUtil:
    def scanOpenPorts(target, r):
        openPorts = []
        try:
            scanned = 0
            for port in r:
								
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(0.01)
                scanned = scanned+1
                
                result = s.connect_ex((target, port))
                
                if result ==0:
                    print("| {}		OPEN".format(port))
                    openPorts.append(port)
                s.close()
            print("Scanned (", scanned, ") | Open Ports: ", openPorts)
                
        except KeyboardInterrupt:
                print("\n Exiting Program !!!!")
                sys.exit()
        except socket.gaierror:
                print("\n Hostname Could Not Be Resolved !!!!")
                sys.exit()
        except socket.error:
                print("\ Server not responding !!!!")
                sys.exit()
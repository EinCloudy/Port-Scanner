import socket
import argparse as arg
from IPy import IP

COMMA = ','
DASH = '-'

def get_arguments():
    """Get arguments from the command line"""
    parser = arg.ArgumentParser()
    parser.add_argument('-t', '--target', dest='target', help='The target/s IP or Hostname (split multiple targets with ,)')
    parser.add_argument('-tm', '--timeout', dest='timeout', help='Timeout for the port connection. Lower the timeout, lower the accuracy of the scan. Use "None" for unlimited time (default: 0.5)', default=0.5)
    parser.add_argument('-p', '--ports', dest='ports', help='Port/s to scan. Use "-" to separate range of ports. Use "None" for all ports (default: 1-100)', default='1-100')
    options = parser.parse_args()
    if not options.target:
        options = None
    return options


def check_ip(ip):
    """Check if the given ip is valid or if it is an hostname. If it is an hostname, it will be resolved to an ip."""       
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)

def split_ports(ports):
    if ports != 'None':
        if DASH in ports:
            firstport = int(ports.split(DASH)[0].strip())
            lastport = int(ports.split(DASH)[1].strip())
            return [firstport, lastport]
        else:
            singleport = int(ports.strip())
            return [singleport, singleport]
    else:
        return [1, 65535]

def get_banner(sock):
    return sock.recv(1024) # Number of byte to receive

def scan_port(ip_address, port, timeout):
    """Verify if the given port of the given ipaddress is opened or closed"""
    try:
        sock = socket.socket()
        if timeout == 'None':
            sock.settimeout(None)
        else:
            sock.settimeout(float(timeout)) # Lower the timeout lower the accuracy of the scan 
        sock.connect((ip_address, port))
        try:
            banner = get_banner(sock).decode().strip('\n')
            print(f'\t[+] Port {port} is Open : {banner}')
        except:
            print(f'\t[+] Port {port} is Open')
    except:
        pass

def scan(target, ports, timeout):
    target_ip = check_ip(target)
    firstport, lastport = split_ports(ports)
    print(f'\n[*] Scanning {target}')
    for port in range(firstport, lastport + 1):       
        scan_port(target_ip, port, timeout)  

def main(targets, ports='1-100', timeout=0.5):
    if COMMA in targets:
        for ip in targets.split(COMMA):
            scan(ip.strip(), ports, timeout)
    else:
        scan(targets, ports, timeout)

if __name__ == '__main__':
    optionsValues = get_arguments()
    if optionsValues:
        main(optionsValues.target, optionsValues.ports, optionsValues.timeout)
    else:
        targets = input('\n[>] Enter Target/s To Scan (split multiple targets with ,): ')
        main(targets)
     
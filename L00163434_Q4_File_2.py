# File          : L00163434_Q4_File_2
# Author        : K. Snehal
# Version       : v1.0.0
# Licencing     : (C) 2021 Snehal Khairnar, LYIT
#                 Available under GNU Public License (GPL)
# Description   : Port scan in remote host
# -------------------------------------------------------

import socket
import subprocess
import sys
from datetime import datetime


def port_scan():
    """
    """
    # Clear the screen  #use clear if running in  *nix
    subprocess.call("cls", shell=True)

    # Ask for input
    remoteServer = "192.168.147.128"
    remoteServerIP = socket.gethostbyname(remoteServer)

    # Print a nice banner with information on which host we are about to scan
    print("-" * 60)
    print("Please wait, scanning remote host", remoteServerIP)
    print("-" * 60)

    # Using the range function to specify ports (here it will scans all ports between 1 and 1024)
    # We also put in some error handling for catching errors

    try:
        # try 1, 1025 if you have time
        for port in range(1, 81):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                if port == 22:
                    print("SSH : 	 Open")  # Print port 22 as SSH is open
                elif port == 80:
                    print("HTTP :   Open")  # Print port 80 as HTTP is open
            sock.close()
    except KeyboardInterrupt:
        print("You pressed Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        sys.exit()

    except socket.error:
        print("Couldn't connect to server")
        sys.exit()


if __name__ == "__main__":
    '''
             Main method of application 
             Open port in the remote host
             Parameters:
              none
             Returns:
              none
          '''
    port_scan()

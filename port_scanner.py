#!/usr/local/bin/python3
import socket
import click

#----------------------------------------------
# Get ip and Hi/Low port for range using CLICK
#----------------------------------------------
@click.command()
@click.option('--ip',       default="", help='IP Address')
@click.option('--low_port', default=1,  help='Low Port for Range')
@click.option('--hi_port',  default=1,  help='High Port for Range')

#------------------------------------
# Func: get_res
#------------------------------------
def get_res(ip, low_port, hi_port):
    while low_port <= hi_port:
        if check_port(ip, low_port) == 0:
            print("Port " + str(low_port) + " is open")
        else:
            print("Port " + str(low_port) + " is not open")
        low_port += 1

#-----------------------
# Func: check_port
#-----------------------
def check_port(ip, port_num):
    sckt     = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sckt.settimeout(1)
    conn_res = sckt.connect_ex((ip, port_num))
    return conn_res

#------------------------------------
#   Exec Get Result Func
#------------------------------------
get_res()

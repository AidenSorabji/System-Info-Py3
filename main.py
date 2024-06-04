# System info

# Created by SpaceN64
# 2022, V1.0

vrs = "1.1"
year = "2022"

# Import's
import time as t
import platform
import psutil
from datetime import datetime

# Classifing
net = ["Network name", "network name", "network Name", "Net", "net"]
sys = ["Sys", "sys", "System", "system"]
plat = ["Platform", "platform", "Plat", "plat"]
mach = ["Machine", "machine"]
cpu = ["CPU", "Cpu", "cpu", "Processor", "processor"]
win_ed = ["Win Edition", "Win edition", "win_edition", "Win_Edition", "Win-edition", "win_ed", "Win_Ed"]
ex = ["Exit", "exit", "Exit()", "exit()"]
commands = ["Commands", "commands", "com", "Com", "Cm", "cm", "Cmd", "cmd", "Cmds", "cmds"]
gpu = ["GPU", "Gpu", "gpu"]
info = ["Info", "info"]
boot = ["Boot", "boot"]
cores = ["Cores", "cores", "Core", "core"]
rams = ["Ram", "ram", "Memory", "memory"]
usages = ["Usage", "usage"]
IPs = ["IP", "ip", "iP", "Ip"]
ios = ["IO", "io", "Io", "io"]

def cmds():
    print("""Here is a list of all the commands you can use in this program:

cmds (duh...)

sys

net

ip

platform

machine

cpu

win_ed

info

ram

core

boot

usage

exit() / exit
""")
    t.sleep(2.3)
    restart()

# Definitions
def core():
    print("Physical cores:", psutil.cpu_count(logical=False))
    print("Total cores:", psutil.cpu_count(logical=True))
    # CPU usage
    print("CPU Usage Per Core:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"Core {i}: {percentage}%")
    print(f"Total CPU Usage: {psutil.cpu_percent()}%")

def usage():
    print("CPU Usage Per Core:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"Core {i}: {percentage}%")
    print(f"Total CPU Usage: {psutil.cpu_percent()}%")

def ip():
    if_addrs = psutil.net_if_addrs()
    for interface_name, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            if str(address.family) == 'AddressFamily.AF_INET':
                print(f"  IP Address: {address.address}")

def io():
    net_io = psutil.net_io_counters()

# Main Code
print("Booting up...")
t.sleep(2)

print("")

print("Version: " + vrs)
print("Year: " + year)

print("""
 S)ssss                    t)                         I)iiii          f)FFF         
S)    ss                 t)tTTT                         I)           f)             
 S)ss    y)   YY  s)SSSS   t)   e)EEEEE  m)MM MMM       I)   n)NNNN  f)FFF   o)OOO  
     S)  y)   YY s)SSSS    t)   e)EEEE  m)  MM  MM      I)   n)   NN f)     o)   OO 
S)    ss y)   YY      s)   t)   e)      m)  MM  MM      I)   n)   NN f)     o)   OO 
 S)ssss   y)YYYY s)SSSS    t)T   e)EEEE m)      MM    I)iiii n)   NN f)      o)OOO  
              y)                                                                    
         y)YYYY                                                                     

""")
t.sleep(1.5)

print("""

Welcome to System Info! This python program can tell the system
you are on, its specs, and many more!

For help, please go the the repo to find some commands, or to get help.

You can also get commands by using the "cmds" command!
""")

def restart():
    print("")
    prompt = input(">>> ")

    if prompt in sys:
        platform.system()
        print(platform.system())
    elif prompt in commands:
        cmds()
    elif prompt in IPs:
        ip()
    elif prompt in ios:
        io()
    elif prompt in boot:
        boot_time_timestamp = psutil.boot_time()
        bt = datetime.fromtimestamp(boot_time_timestamp)
        print(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")

    elif prompt in net:
        platform.node()
        if_addrs = psutil.net_if_addrs()
        for interface_name, interface_addresses in if_addrs.items():
            for address in interface_addresses:
                print(f"=== Interface: {interface_name} ===")
                if str(address.family) == 'AddressFamily.AF_INET':
                    print(f"  IP Address: {address.address}")
                    print(f"  Netmask: {address.netmask}")
                    print(f"  Broadcast IP: {address.broadcast}")
                elif str(address.family) == 'AddressFamily.AF_PACKET':
                    print(f"  MAC Address: {address.address}")
                    print(f"  Netmask: {address.netmask}")
                    print(f"  Broadcast MAC: {address.broadcast}")

        print(platform.node())
    elif prompt in usages:
            usage()
    elif prompt in plat:
        platform.platform(aliased=0, terse=0)
        print(platform.platform(aliased=0, terse=0))
    elif prompt in cores:
        core()
    elif prompt in rams:
        print("Yeah.. this doesn't work right now no matter how i tried, but ehhhhhhhh ill get it to work some time soon")
        t.sleep(1)
    elif prompt in mach:
        platform.machine()
        print(platform.machine())
    elif prompt in cpu:
        platform.processor()
        print(platform.processor())
    elif prompt in win_ed:
        platform.win32_edition()
        print(platform.win32_edition())
    elif prompt in gpu:
        print("This command and other commands will be coming soon!")
        t.sleep(1)
    elif prompt in info:
        print("="*40, "System Information", "="*40)
        uname = platform.uname()
        print(f"System: {uname.system}")
        print(f"Node Name: {uname.node}")
        print(f"Release: {uname.release}")
        print(f"Version: {uname.version}")
        print(f"Machine: {uname.machine}")
        print(f"Processor: {uname.processor}")

        # Boot Time
        print("="*40, "Boot Time", "="*40)
        boot_time_timestamp = psutil.boot_time()
        bt = datetime.fromtimestamp(boot_time_timestamp)
        print(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")

        # CPU information
        print("="*40, "CPU Info", "="*40)
        # number of cores
        print("Physical cores:", psutil.cpu_count(logical=False))
        print("Total cores:", psutil.cpu_count(logical=True))
        # CPU frequencies
        cpufreq = psutil.cpu_freq()
        print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
        print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
        print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
        # CPU usage
        print("CPU Usage Per Core:")
        for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
            print(f"Core {i}: {percentage}%")
        print(f"Total CPU Usage: {psutil.cpu_percent()}%")

        # Network information
        print("="*40, "Network Information", "="*40)
        # Network interfaces (virtual and physical)
        if_addrs = psutil.net_if_addrs()
        for interface_name, interface_addresses in if_addrs.items():
            for address in interface_addresses:
                print(f"=== Interface: {interface_name} ===")
                if str(address.family) == 'AddressFamily.AF_INET':
                    print(f"  IP Address: {address.address}")
                    print(f"  Netmask: {address.netmask}")
                    print(f"  Broadcast IP: {address.broadcast}")
                elif str(address.family) == 'AddressFamily.AF_PACKET':
                    print(f"  MAC Address: {address.address}")
                    print(f"  Netmask: {address.netmask}")
                    print(f"  Broadcast MAC: {address.broadcast}")
        # IO statistics since boot
        net_io = psutil.net_io_counters()
    elif prompt in ex:
        print("""
Goodbye!""")
        t.sleep(1)
        exit()
    else:
        print("""
That is not a valid command!""")
        t.sleep(1.5)
        restart()
    
        
    t.sleep(0.2)
    restart()

restart()

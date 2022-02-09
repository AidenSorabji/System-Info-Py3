# System info

# Created by SpaceN64
# 2022, V1.0

vrs = "1.0"
year = "2022"

# Import's
import time as t
import platform

# Classifing
net = ["Network name", "network name", "network Name", "Net", "net"]
sys = ["Sys", "sys", "System", "system"]
plat = ["Platform", "platform", "Plat", "plat"]
mach = ["Machine", "machine"]
cpu = ["CPU", "Cpu", "cpu", "Processor", "processor"]
mac = ["Mac", "mac", "Macintosh", "macintosh"]
win_ver = ["Win Ver", "win ver", "Win ver", "win_ver", "Win_Ver"]
win_ed = ["Win Edition", "Win edition", "win_edition", "Win_Edition", "Win-edition", "win_ed", "Win_Ed"]

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
t.sleep(2)

print("""

Welcome to System Info! This python program can tell the system
you are on, its specs, and many more!

For help, please go the the repo to find some commands, or to get help.
""")
def restart():
    print("")
    prompt = input(">>> ")

    if prompt in sys:
        platform.system()
        print(platform.system())
    elif prompt in net:
        platform.node()
        print(platform.node())
    elif prompt in plat:
        platform.platform(aliased=0, terse=0)
        print(platform.platform(aliased=0, terse=0))
    elif prompt in mach:
        platform.machine()
        print(platform.machine())
    elif prompt in cpu:
        platform.processor()
        print(platform.processor())
    elif prompt in win_ed:
        platform.win32_edition()
        print(platform.win32_edition())
    else:
        print("""
Goodbye!""")
        t.sleep(1)
        exit()
        
    t.sleep(0.2)
    restart()

restart()

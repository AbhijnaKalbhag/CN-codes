# 3. Running a Simple Web Server and Client:
#  - Set up a simple network in Mininet with one host acting as a web server and another as a client. 
# Configure the web server to host a basic HTML page and write a script to retrieve this page using the client, demonstrating successful communication.

#!/usr/bin/python

import os
from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink

def setup_network():
    "Create a network."
    net = Mininet(controller=Controller, link=TCLink)

info("* Adding controller\n")
net.addController('c0')

info("* Adding hosts\n")
    h1 = net.addHost('h1', ip='10.0.0.1')
    h2 = net.addHost('h2', ip='10.0.0.2')

info("* Adding switch\n")
    s1 = net.addSwitch('s1')

info("* Creating links\n")
net.addLink(h1, s1)
net.addLink(h2, s1)

info("* Starting network\n")
net.start()
 
info("* Configuring web server on h1\n")
h1.cmd('mkdir -p /tmp/www')
os.system('cp index.html /tmp/www')
h1.cmd('cd /tmp/www && python3 -m http.server 80 &')

info("* Running CLI\n")
CLI(net)

info("* Stopping network\n")
net.stop()

if _name_ == '_main_':
setLogLevel('info')
setup_network()

# index.html:
# <!DOCTYPE html>
# <html>
# <head>
# <title>Mininet Web Server</title>
# </head>
# <body>
# <h1>Hello from Mininet!</h1>
# </body>
# </html>

# Mininet> h2 wgethttp://10.0.0.1
# Mininet> h2 cat index.html

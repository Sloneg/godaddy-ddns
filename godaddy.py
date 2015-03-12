#!/usr/bin/python

import urllib2
import sys
from pygodaddy import GoDaddyClient

username = "username"
password = "password"

if len(sys.argv) <= 1:
    print("Usage: " + sys.argv[0] + "hostname [ip]")
    sys.exit(1);

hostname = sys.argv[1]

print(hostname)
if len(sys.argv) == 2:
    sys.stdout.write("Get IP...\n")
    sys.stdout.flush()
    ip = urllib2.urlopen('http://ip.42.pl/raw').read()
if len(sys.argv) == 3:
    ip = sys.argv[2]

oldip = socket.gethostbyname(hostname)

print("Was: " + oldip + " and we want: " + ip + "\n")

if oldip != ip:
    print ('Updating')
    client = GoDaddyClient()

    print("Logging into GoDaddy...")
    if client.login(username, password):
        print("Updating IP...")
        if client.update_dns_record(hostname, ip):
                print("Update OK!")
        else:
                print("Update fail!")
else:
    print('Nothing to do\n')

#!/usr/bin/env python3

import getpass
import socket

print ("Benutzer:", getpass.getuser())
print ("Hostname:", socket.gethostname())

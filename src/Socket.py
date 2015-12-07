# Open socket with Settings/MainSettings.py
# Fairly generic
#
import socket
from MainSettings import HOST, PORT, CHANNEL
from OAuthSettings import OAUTH, NICK

def openSocket():
    sock = socket.socket()
    sock.connect((HOST, PORT))
    sock.send("PASS " + OAUTH + "\r\n") # PASSWORD
    sock.send("NICK " + NICK + "\r\n") # USERNAME
    sock.send("JOIN #" + CHANNEL + "\r\n") # USERNAME
    return sock

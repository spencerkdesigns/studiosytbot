# Open socket with Settings/MainSettings.py
# Fairly generic
#
import socket
from Settings/MainSettings import HOST, PORT, CHANNEL
from Settings/OAuthSettings import OAUTH, NICK

def openSocket():
    sock = socket.socket
    sock.connect((HOST, PORT))
    sock.send("PASS " + PASS + "\r\n") # PASSWORD
    sock.send("NICK " + NICK + "\r\n") # USERNAME
    sock.send("JOIN #" + CHANNEL + "\r\n") # USERNAME
    return sock

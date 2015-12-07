import string
from Read import getUser, getMessage
from Socket import openSocket, sendMessage
from Initialize import joinRoom

s = openSocket()
joinRoom(s)
readbuffer = ""

while True:
		readbuffer = readbuffer + s.recv(1024)
		temp = string.split(readbuffer, "\n")
		readbuffer = temp.pop()
		
		for line in temp:
			user = getUser(line)
			message = getMessage(line)
			print user + " typed :" + message
			if "You Suck" in message:
				sendMessage(s, "No, you suck!")
				break
				print(line)
			if "!Join" in message:
				sendMessage(s, "Here is where you apply https://www.freedom.tm/dashboard#/total")
				break
				print(line)
			if "PING" in line:
				s.send(line.replace("PING", "PONG"))
				break

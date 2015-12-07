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
				sendMessage(s, "Here is where you apply https://freedom.tm/auth/creatorstudios+apply")
				break
				print(line)
			if "!Twitter" in message:
				sendMessage(s, "Follow us here: https://twitter.com/creatorstudios_")
				break
				print(line)
			if "https://" or ".com" in message:
				sendMessage(s, "No links allowed")
				break
				print(line)
			if "PING" in line:
				s.send(line.replace("PING", "PONG"))
				break

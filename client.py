from curses import wrapper,echo,noecho,KEY_BACKSPACE
from queue import Queue
import asyncio,threading,socket,os

messages = Queue()
ip = input("Enter IP: ")
port = int(input("Enter port: "))

text = ""
line = 0
word = ""

def setup(stdscr):
    os.write(1, b"\x1b[2J")     #stdscr.clear()
    noecho()
    stdscr.keypad(True)
    stdscr.timeout(20)
    stdscr.refresh()


def newmessage(stdscr,message):
    stdscr.nodelay(True)
    global line
    if message != "":
        height, width = stdscr.getmaxyx()
        stdscr.addstr(line,0,message)
        line += 1
        stdscr.move(height-1,14)
        stdscr.refresh()


def getinput(stdscr):
    global word
    key = stdscr.getch()

    if key in (127,8,KEY_BACKSPACE):
        word = word[:-1]

    elif key in (10,13):
        s.sendall(word.encode())
        word = ""
    
    elif 32 <= key <= 126:
        word += chr(key)

    height, width = stdscr.getmaxyx()
    stdscr.move(height-1,0)
    stdscr.clrtoeol()
    stdscr.addstr(height-1,0,"Type message: " + word)


def recieve_message():
    while True:
        text = s.recv(1024).decode()
        messages.put(text)

def main(stdscr):
    setup(stdscr)

    while True:
        while not messages.empty():
            newmessage(stdscr,messages.get())
        getinput(stdscr)
        stdscr.refresh()


s = socket.socket()
s.connect((ip,port))


input_thread = threading.Thread(target=recieve_message, daemon = True)
input_thread.start()

wrapper(main)
#while True:
    #wrapper(getinput)
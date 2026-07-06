from curses import wrapper,echo,noecho,KEY_BACKSPACE
from queue import Queue
import asyncio,threading,socket,os

messages = Queue()
ip = input("Enter IP: ")
port = int(input("Enter port: "))

text = ""
word = ""
history = []

def setup(stdscr):
    os.write(1, b"\x1b[2J")     #stdscr.clear()
    noecho()
    stdscr.keypad(True)
    stdscr.timeout(20)
    stdscr.refresh()


def newmessage(stdscr,message):
    stdscr.clear()
    stdscr.nodelay(True)

    if message != "":
        history.append(message)
        height, width = stdscr.getmaxyx()
        while len(history) > height - 2:
            history.remove(history[0])
        for text in range(len(history)):
            stdscr.addstr(text,0,history[text])

        stdscr.move(height-1,14)


def getinput(stdscr):
    global word,history
    key = stdscr.getch()

    if key in (127,8,KEY_BACKSPACE):
        word = word[:-1]

    elif key in (10,13):
        if word == "!clear":
            stdscr.clear()            
        else:
            s.sendall(word.encode())
        word = ""
    
    elif 32 <= key <= 126:
        if word.split() == "!clear":
            history = []
            stdscr.clear()
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
    stdscr.scrollok(True)

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

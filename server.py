import socket,sys,asyncio,threading

ip = "127.0.0.1"
users = []
userid = 0

class client:    
    def __init__(self,c,addr):
        self.conn = c
        self.addr = addr
        self.username = "User_" + str(userid)
        
def addtext(stdscr,y,x):
    stdscr.addstr(y,x,"Server successfully hosted")
    stdscr.refresh()


def handle_client(cli):
    while True:
        try:
            msgraw = cli.conn.recv(1024).decode()
            msg = cli.username + ": " + msgraw
        except:
            continue

        if msgraw.startswith("!changeusername"):
            old = cli.username
            cli.username = msgraw[len("!changeusername "):].strip()
            print(old + " changed their username to " + cli.username)

            for user in users:
                try:
                    user.conn.send((old + " changed their username to " + cli.username).encode())
                except:
                    continue

            continue

        print(msg)
        for user in users:
            try:
                user.conn.send(msg.encode())
            except:
                continue


s = socket.socket()
port = 12345


try:
    s.bind(("",port))

except:
    print("Connection unsuccesful")

s.listen(5)

while True:
    conn,addr = s.accept()
    userid += 1
    c = client(conn,addr)
    users.append(c) 
    client_t = threading.Thread(target=handle_client, args=(c, )) 
    client_t.start()
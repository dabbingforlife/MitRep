import socket,threading,random
from json import loads,dumps

port = eval(input("Enter port: "))
users = []
userid = 0
greetings = (
    "Welcome aboard!",
    "Glad you're here!",
    "Nice to see you!",
    "Welcome!",
    "Hey there!",
    "Have fun chatting!",
    "Enjoy your stay!",
    "Happy chatting!",
    "Make yourself at home.",
    "Great to have you!",
    "Hope you're doing well!",
    "Say hello!",
    "Join the conversation!",
    "Good to have you here.",
    "Welcome to the chat!",
    "Hope you enjoy your time here.",
    "The chat just got better!",
    "It's great to have you with us.",
    "Wishing you a great day!",
    "Have an awesome time!",
    "Let's get chatting!",
    "Feel free to jump in!",
    "Don't be shy!",
    "Everyone, say hi!",
    "Make some new friends!",
    "Stay awhile!",
    "Hope you have a good time.",
    "Glad you made it!",
    "Time to chat!",
    "Chat away!",
    "You're just in time!",
    "Good vibes only!",
    "Let's have a great conversation.",
    "Enjoy the community!",
    "Thanks for joining!",
    "Have a fantastic day!",
    "New faces are always welcome!",
    "Welcome, and have fun!",
    "The conversation awaits!",
    "Ready to mingle?",
    "Hope you're having a great day!",
    "It's nice to meet you!",
    "Cheers!",
    "Welcome to the party!",
    "Make yourself comfortable!",
    "We're happy you're here!",
    "Dive right in!",
    "The fun starts now!",
    "Let the chatting begin!",
    "Hello and welcome!",
)


class client:   # Class containing all client information
    def __init__(self,c,addr):
        self.conn = c
        self.addr = addr
        self.username = "User_" + str(userid)
        
def greet(connection) -> str:   # Returns a string that greets a specific user
    server_dict: dict = {}
    server_dict["type"] = "announcement"
    server_dict["msg"] = connection.username + " joined in! " + random.choice(greetings)
    return server_dict

def broadcast(message) -> None:    # Sends a message to all users

    msg_dict = loads(message)   # Loads json into a dictionary to print message in server log

    print(msg_dict.get("username") + ":" + msg_dict.get("msg"))    # Prints the message
    for user in users:
            try:
                user.conn.send(message.encode())
            except:
                user.conn.close()


def handle_client(cli) -> None:
    while True:
        try:
            msg_dict = loads(cli.conn.recv(1024).decode())   # Recieves message from client and converts it into a dictionary

            server_dict:dict = {}   # Dictionary used to send messages to client

        except:
            continue
        
        if msg_dict["type"] == "command":

            if msg_dict["msg"].startswith("!changeusername"):    # Changes username of client

                old = cli.username
                cli.username = msg_dict["msg"].lstrip("!changeusername").strip()

                server_dict["type"] = "announcement"
                server_dict["msg"] = old + " changed their username to " + cli.username

            elif msg_dict["msg"] == "!wave":    # Client waves

                server_dict["type"] = "announcement"
                broadcast(dumps({"type":"announcement","msg":""}))  # Sends an empty message, resulting in a blank line above and below the wave in client terminal
                server_dict["msg"] =  cli.username + " waves" 
                broadcast(dumps({"type":"announcement","msg":""}))

            else:
                continue
            
        elif msg_dict["type"] == "text":    # Prepares server_dict with data required to send to clients
            server_dict["type"] = "text"
            server_dict["username"] = cli.username
            server_dict["msg"] = msg_dict["msg"]

        broadcast(dumps(server_dict))   # Sends server_dict to all clients





s = socket.socket()


try:
    s.bind(("",port))   # Binds server to a specified port

except:
    print("Connection unsuccesful")

s.listen()    # Allows server to allow connections

while True:
    conn,addr = s.accept()  # Accepts connection 
    userid += 1
    c = client(conn,addr)   # Creates an object that acts as the client
    users.append(c)
    broadcast(dumps(greet(c)))  # Greets newly joined user
 
    client_t = threading.Thread(target=handle_client, args=(c, ))   # Creates a thread to receive messages from clients
    client_t.start()
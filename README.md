# 💬 MitRep

> A lightweight, multi-client terminal chat application built with Python, TCP sockets, and curses.

MitRep is a real-time messaging application that runs entirely in your terminal. Designed as a networking and systems programming project, it demonstrates socket programming, multithreading, and terminal UI development using Python's standard library.

---

## ✨ Features

* ⚡ Real-time messaging
* 👥 Multiple clients supported
* 🖥️ Interactive terminal interface powered by `curses`
* 📜 Scrollable message history
* 🧵 Multi-threaded server architecture
* 🔔 Join notifications
* 🚀 Lightweight and fast
* 📦 Minimal dependencies

---

## 📸 Preview

<img width="1482" height="762" alt="image" src="https://github.com/user-attachments/assets/13c9ed57-02a8-425e-9cb8-a5b7a64b0e08" />

<img width="1482" height="762" alt="image" src="https://github.com/user-attachments/assets/36cea398-e36d-43a1-b1b6-293036351136" />





---

## 🛠️ Tech Stack

* **Language:** Python 3
* **Networking:** TCP Sockets
* **UI:** curses
* **Concurrency:** threading
* **Communication:** JSON
* **Message Handling:** queue

---

## 📂 Project Structure

```text
MitRep/
├── client.py          # Client application
├── client.bat         # Runs client.py in a terminal
├── server.py          # Server application
├── server.bat         # Runs server.py in a terminal
├── README.md
└── LICENSE

```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/palofc/MitRep.git
cd MitRep
```

### Windows

Install curses support:

```bash
pip install windows-curses
```

### Linux / macOS

No additional packages are required.

---

## ▶️ Usage

### Start the server

```bash
python server.py
```

### Start a client

```bash
python client.py
```

Enter the server's IP address and port when prompted.

---

## 🏗️ How It Works

1. The server listens for incoming TCP connections.
2. Each connected client is handled in its own thread.
3. Messages are broadcast to every connected client.
4. The client uses a terminal-based interface built with `curses`, keeping the bottom line reserved for typing while messages update above it.

---

## 📈 Planned Features

* [ ] User authentication
* [ ] Emoji support
* [ ] Message timestamps
* [ ] Colored usernames
* [ ] Desktop notifications
* [ ] End-to-end encryption
* [ ] Configuration file

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve MitRep, feel free to fork the repository, make your changes, and open a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**pals**

GitHub: https://github.com/palofc


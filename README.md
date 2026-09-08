# Semester-2-Project
# 🏆 GITAM Treasure Hunt

A fun and interactive **campus-themed treasure hunt game** built using **Python Turtle Graphics**.

Players solve series of riddles based on locations around the GITAM campus. Each correct answer reveals the next location and moves the player across the map. The game includes **30-second timer for each attempt, hints, file-based leaderboard, and a final treasure reveal**.


## 🎮 Features

* 🧩 **9 campus-based riddles**
* ⏱️ **30-second timer** for every attempt
* 💡 **Two hints** available after incorrect attempts
* ❤️ **Up to 3 attempts** for each riddle
* 🗺️ **Interactive campus map**
* 🔴 Player marker moves between locations
* 📍 Locations are revealed after solving riddles
* 🏆 **Treasure reveal animation**
* 📊 **Leaderboard system**
* 💾 Leaderboard data stored using text file
* 👤 Player name input
* 🎨 Interactive graphical interface using Turtle

---

## 📍 Locations Included

The game takes the player through several GITAM campus locations:

1. 📚 Library
2. ☕ CC
3. 🐾 Pet Care
4. 🛍️ Bheemas
5. 🗿 Shivaji Statue
6. 🥤 Vending Machine
7. 🏦 Bank
8. 🚪 D206
9. 🎬 Veeksha Hall — **Treasure Location**

---

## 🛠️ Technologies Used

* **Python 3**
* **Turtle Graphics** — game interface and map
* **Time Module** — timer and game duration
* **Textwrap Module** — formatting clues
* **File Handling** — leaderboard storage

---

## 📂 Project Structure

```text
GITAM-Treasure-Hunt/
│
├── treasure_hunt.py
├── leaderboard.txt
└── README.md
```

> `leaderboard.txt` is automatically created when the game saves the first score.

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/GITAM-Treasure-Hunt.git
```

### 2. Open the project folder

```bash
cd GITAM-Treasure-Hunt
```

### 3. Run the game

```bash
python treasure_hunt.py
```

### 4. Enter your name

The game will ask:

```text
Enter your name:
```

Enter your name and press **Enter**.

---

## 🎯 How to Play

1. Enter your name.
2. Read the first clue displayed on the screen.
3. Type your answer using the keyboard.
4. Press **Enter** to submit.
5. You have **30 seconds** to answer each attempt.
6. If your answer is incorrect, a hint will be displayed.
7. You get a maximum of **3 attempts** for each riddle.
8. Solve the riddles to move around the campus map.
9. Reach **Veeksha Hall** to discover the treasure! 🏆
10. Your final time is recorded on leaderboard.

---

## 🧩 Example Riddle

### Clue

> This place is usually the quietest area on campus. People come here when they need information.

### Hint 1

> Students study here

### Hint 2

> It is full of books

### Answer

```text
library
```

---

## ⏱️ Timer System

Each riddle gives the player **30 seconds per attempt**.

The timer resets whenever a new attempt begins.

If the player fails all three attempts, the correct answer is displayed before the game continues to the next location.

---

## 🗺️ Map System

The game contains a simple graphical map created using Turtle.

A **red dot** represents the player.

When a riddle is solved:

* The location is revealed with a blue marker.
* The player marker moves toward the location.
* The location name is displayed on the map.

---

## 🏆 Leaderboard

The game stores player scores in:

```text
leaderboard.txt
```

Each record is stored in the format:

```text
PlayerName,Time
```

Example:

```text
Laxmi,82.45
Rahul,95.21
Ananya,110.37
```

The leaderboard is sorted by **lowest completion time**, and the top 5 players are displayed.

---

## 💻 Concepts Demonstrated

This project demonstrates several important Python programming concepts:

* Variables and data types
* User input
* Functions
* Loops
* Conditional statements
* Lists and tuples
* String manipulation
* File handling
* Exception handling
* Lambda functions
* Sorting
* Global variables
* Turtle graphics
* Keyboard event handling
* Basic game logic
* Time-based programming

---

## 🔮 Future Improvements

Possible improvements for future versions:

* 🗺️ Add a more accurate GITAM campus map
* 🔊 Add sound effects and background music
* 🖼️ Add images for different campus locations
* 🎯 Add difficulty levels
* 🏅 Add achievement badges
* 💾 Use JSON or SQLite instead of a text leaderboard
* 🌐 Create a web-based version
* 👥 Add multiplayer support
* 📱 Create a mobile-friendly version
* 🔐 Add a login/profile system
* 🎲 Randomize riddles and locations
* 📈 Add detailed player statistics

---

## 👩‍💻 Author

**Laxmi Biradar**

B.Tech — Computer Science & Engineering (AI & ML)
GITAM Deemed to be University

---

## ⭐ Project

If you enjoyed this project, consider giving the repository a ⭐ on GitHub!

---

### 🏆 Can You Solve All 9 Riddles Before Time Runs Out?

**Enter the campus. Solve the clues. Find the treasure! 🗺️🔎🏆**

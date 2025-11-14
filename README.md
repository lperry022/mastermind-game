# 🎮 Mastermind Game (Python)

This is a simple console-based implementation of the classic **Mastermind** game.  
The player must guess a **4-colour secret code** within **10 attempts**.  
After each guess, the game provides feedback on:

- ✅ **Correct Positions** — right colour in the right spot  
- 🔄 **Incorrect Positions** — right colour but in the wrong spot  

This project was built for learning purposes and includes detailed comments explaining each part of the code.

---

## 🧩 How the Game Works

- The computer randomly generates a secret code using 6 possible colours: RED, BLUE, GREEN, YELLOW, PURPLE, ORANGE
- The player enters four colours per guess  
  Example:
red blue green yellow
- Input is case-insensitive  
- The game ends when:
- the player cracks the code 🎉  
- or runs out of tries ❌  

---

## 📂 Project Structure

mastermind-game/
│
├── game.py # Main Python file containing the full game logic
└── README.md # Project documentation

---

## 🚀 How to Run the Game

1. Make sure Python is installed  
2. Clone or download this repository  
3. Run the game with:

python game.py

4. Follow the on-screen instructions

---

## 🧠 What I Learned

This project helped reinforce key Python concepts:

### ✔ Functions  
Reusable blocks of code used to organise the program (e.g., `generate_code()`, `guess_code()`).

### ✔ Lists  
Used to store the colour options and the randomly generated code.

### ✔ Dictionaries  
Used in `check_code()` to count how many times each colour appears in the code.

### ✔ Loops  
`for` loops compare guess values, while `while` loops handle user input validation.

### ✔ Input validation  
Ensures the player always enters 4 valid colours before continuing.

---

## 🎥 Tutorial Reference

This project was inspired by and built using the following tutorial:

**Tech With Tim – Python Mastermind Game Tutorial**  
https://youtu.be/sP-gFDreaQ4

The tutorial helped guide the main game logic, and I expanded it further with additional comments and learning notes.

---

## 📝 Possible Future Improvements

- Add difficulty levels  
- Add emojis or coloured terminal output  
- Add automated tests  
- Add a GUI version (Tkinter, Pygame)  
- Allow “play again” without restarting the script  

---

## 📜 License

This project is for educational purposes — feel free to use, share, and modify it.


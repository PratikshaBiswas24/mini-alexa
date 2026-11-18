#  Virtual AI Assistant (Mini Alexa)

## Project Information

| Field | Details |
|---|---|
| Project Name | Virtual AI Assistant (Mini Alexa) |
| Project Code | AI-INT-P1-VAA |
| Organization | Nexbridge Technologies |
| Internship Program | AI Internship Program |
| Version | 1.0 |
| Programming Language | Python |

---

## 1. Project Overview

Mini Alexa is a beginner-level, terminal-based virtual AI assistant developed using Python.

It interacts with users through text commands and performs various tasks such as displaying the current date and time, performing mathematical calculations, providing motivational quotes, telling jokes, sharing interesting facts, and playing a number guessing game.

The project also demonstrates basic Artificial Intelligence concepts through rule-based decision-making and a simplified perceptron calculation.

---

## 2. Project Objectives

- Develop an interactive virtual assistant using Python.
- Understand functions, loops, conditional statements and exception handling.
- Implement command-based user interaction.
- Demonstrate basic Artificial Intelligence concepts.
- Understand the fundamentals of a simplified perceptron.
- Improve Python programming and problem-solving skills.

---

## 3. Features

The Mini Alexa assistant provides the following features:

1. **Greeting and Name Capture:** Greets the user and remembers their name during the session.
2. **Date Display:** Displays the current date.
3. **Time Display:** Displays the current time.
4. **Basic Calculator:** Performs addition, subtraction, multiplication and division.
5. **Motivational Quotes:** Displays randomly selected motivational quotes.
6. **Jokes:** Tells random programming and general jokes.
7. **Interesting Facts:** Shares random facts.
8. **Number Guessing Game:** Allows users to guess a randomly generated number.
9. **Rule-Based Recommendation:** Suggests activities based on the current time.
10. **Simplified Perceptron:** Demonstrates weighted inputs, bias and binary output.
11. **Help Menu:** Displays all available commands.
12. **Graceful Exit:** Allows users to exit the application safely.
13. **Unknown Command Handling:** Provides friendly responses to unsupported commands.

---

## 4. Technologies Used

- **Programming Language:** Python
- **Modules:** datetime, random
- **IDE:** Visual Studio Code
- **Interface:** Command Line / Terminal

Only Python's standard library is used.

---

## 5. Project Structure

```text
Mini-Alexa/
│
├── main.py
│
└── README.md
```

---

## 6. Installation and Execution

### Prerequisites

- Python 3 installed on your system.
- Visual Studio Code or any Python-supported editor.

### Steps to Run

1. Download or clone the project.
2. Open the project folder in Visual Studio Code.
3. Open the integrated terminal.
4. Run the following command:

```bash
python main.py
```

5. Enter your name when prompted.
6. Type `help` to view all available commands.

---

## 7. Available Commands

| Command | Description |
|---|---|
| `date` | Displays the current date |
| `time` | Displays the current time |
| `calculate 12 + 8` | Performs mathematical calculations |
| `quote` | Displays a motivational quote |
| `joke` | Tells a random joke |
| `fact` | Displays an interesting fact |
| `game` | Starts the number guessing game |
| `recommend` | Suggests an activity based on the current time |
| `perceptron` | Runs the simplified perceptron demonstration |
| `help` | Displays the help menu |
| `exit` / `quit` / `bye` | Exits the assistant |

---

## 8. AI Concepts Demonstrated

### 8.1 Rule-Based System

The assistant uses predefined conditions to recommend activities based on the current hour.

For example:
- Morning: Have breakfast and start the day.
- Afternoon: Go for a walk or exercise.
- Evening: Relax and enjoy the evening.
- Night: Get some rest.

### 8.2 Simplified Perceptron

The perceptron demonstration calculates a weighted sum using two inputs, their respective weights and a bias.

**Formula:**

Z = (X1 × W1) + (X2 × W2) + b

Where:

- X1 and X2 represent input values.
- W1 and W2 represent weights.
- b represents bias.
- Z represents the weighted sum.

The output is determined using a simple threshold:

- If Z > 0, output = 1.
- Otherwise, output = 0.

**Note:** This project demonstrates a simplified perceptron calculation. It does not perform actual machine learning training or deep learning.

---

## 9. Error Handling

The application handles the following situations:

- Invalid numerical inputs.
- Division by zero.
- Invalid guessing game inputs.
- Unsupported commands.
- Empty user names.

Python exception handling is used to prevent the application from terminating unexpectedly during these operations.

---

## 10. Testing

Manual testing is performed using different valid and invalid inputs to verify the application's functionality.

The testing process covers:

- Greeting and name capture.
- Date and time commands.
- Calculator operations.
- Invalid calculator inputs.
- Random quotes, jokes and facts.
- Number guessing game.
- Rule-based recommendations.
- Perceptron calculations.
- Help menu.
- Graceful exit and unknown commands.

A minimum of 20 test cases is included in the manual testing plan.

---

## 11. Project Limitations

- The application operates through a terminal only.
- It does not support voice interaction.
- It does not use external APIs or online services.
- It does not use databases.
- It does not train real machine learning models.
- User information is remembered only during the current session.

---

## 12. Conclusion

Mini Alexa demonstrates the fundamentals of Python programming and introductory Artificial Intelligence concepts through a simple interactive virtual assistant.

The project provides practical experience with functions, conditional statements, loops, exception handling, randomization and basic mathematical computation.

It also introduces rule-based decision-making and simplified perceptron calculations without requiring external libraries or machine learning training.

---

##  Project Credits

**Developed as part of the AI Internship Program at Nexbridge Technologies.**

**Project:** Virtual AI Assistant (Mini Alexa)  
**Project Code:** AI-INT-P1-VAA

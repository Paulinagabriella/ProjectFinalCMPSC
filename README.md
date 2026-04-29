# Thought Organizer

## Project Description

Thought Organizer is a Python-based cognitive accessibility tool designed to help users organize overwhelming or complex thoughts into clearer decisions and actionable next steps.

The application allows users to input multiple thoughts, assign categories, rate urgency and importance, and receive structured recommendations through a recursive decision tree. The program then ranks thoughts by priority and generates a personalized report.

This project focuses on **cognitive accessibility**, helping users who may struggle with decision-making, prioritization, or processing multiple thoughts at once.

---

## Features

- Graphical User Interface (GUI) built with Tkinter
- Add and organize multiple thoughts
- Assign categories to thoughts
- Rate urgency and importance (1–5)
- Automatic priority score calculation
- Manual sorting of thoughts by priority
- Recursive decision tree for personalized suggestions
- Higher-order function usage with `map()`
- Save generated reports to a text file
- Full input validation and error handling

---

## Technical Concepts Demonstrated

This project incorporates several CMPSC 132 concepts:

### Object-Oriented Programming
- `Thought`
- `ThoughtNode`
- `ThoughtOrganizer`
- `ThoughtOrganizerGUI`

### Data Structures
- Lists for storing thoughts
- Tree-based linked node structure for decision tree

### Algorithms / Concepts
- Recursion for tree traversal
- Selection-sort style algorithm for priority ranking
- Higher-order functions using `map()`
- File I/O for saving reports

---

## How to Run

1. Ensure Python 3 is installed.
2. Clone or download this repository.
3. Open the project folder.
4. Run the program:

```bash
python thought_organizer.py
```

or if needed:

```bash
python3 thought_organizer.py
```

---

## Example Workflow

1. Enter one or more thoughts
2. Assign categories
3. Rate urgency and importance
4. Answer decision tree questions
5. Click **Organize Thoughts**
6. Review ranked thoughts and recommendations
7. Save report to file if desired

---

## File Structure

```text
ThoughtOrganizer/
│
├── thought_organizer.py
├── thought_organizer_report.txt
└── README.md
```

---

## Author

Paulina Chavez

---

## Course

CMPSC 132 – Spring 2026  
Custom Final Project Submission
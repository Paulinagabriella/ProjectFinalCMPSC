# Thought Organizer

## Project Description

Thought Organizer is a Python-based cognitive accessibility tool designed to help users structure overwhelming or complex thoughts into clearer decisions. The program guides users through a recursive decision tree of yes/no questions and provides organized suggestions based on their responses.

This project focuses on cognitive accessibility by supporting users who may struggle with organizing information, processing multiple thoughts, or making decisions.

## Features

- Object-Oriented Programming using custom classes
- Tree-based data structure for decision making
- Recursive traversal of decision tree
- Input validation for all user responses
- Error handling for invalid inputs
- Summary report of all responses
- Structured suggestion generation

## Data Structures and Concepts Used

This project demonstrates several CMPSC 132 concepts:

- **Classes / OOP**
  - `ThoughtNode`
  - `ThoughtOrganizer`

- **Tree Data Structure**
  - Decision tree implemented with linked node references

- **Recursion**
  - Recursive traversal of the decision tree

- **Lists**
  - Stores user responses for summary output

- **Input Validation / Error Handling**
  - Ensures only valid yes/no responses are accepted

## How to Run

1. Ensure Python 3 is installed.
2. Clone or download this repository.
3. Open the project directory.
4. Run:

```bash
python thought_organizer.py
```

If needed:

```bash
python3 thought_organizer.py
```

## Example Interaction

```text
Welcome to Thought Organizer!

Are you trying to make a decision? (yes/no): yes
Do you already know your options? (yes/no): no

Suggested next step:
Start by listing all possible options, even if they are not perfect. Then narrow them down.
```

## File Structure

```text
ThoughtOrganizer/
│
├── thought_organizer.py
└── README.md
```

## Author

Paulina Chavez

## Course

CMPSC 132 – Spring 2026  
Custom Final Project Submission
import tkinter as tk
from tkinter import messagebox


class Thought:
    def __init__(self, text, category, urgency, importance):
        self.text = text
        self.category = category
        self.urgency = urgency
        self.importance = importance
        self.priority_score = urgency + importance

    def get_priority_level(self):
        if self.priority_score >= 8:
            return "High Priority"
        elif self.priority_score >= 5:
            return "Medium Priority"
        else:
            return "Low Priority"

    def __str__(self):
        return (
            self.text +
            " | Category: " + self.category +
            " | Urgency: " + str(self.urgency) +
            " | Importance: " + str(self.importance) +
            " | Score: " + str(self.priority_score)
        )


class ThoughtNode:
    def __init__(self, question=None, yes_branch=None, no_branch=None, suggestion=None):
        self.question = question
        self.yes_branch = yes_branch
        self.no_branch = no_branch
        self.suggestion = suggestion


class ThoughtOrganizer:
    def __init__(self):
        self.thoughts = []
        self.root = self.build_decision_tree()

    def build_decision_tree(self):
        return ThoughtNode(
            "Are you trying to make a decision?",
            yes_branch=ThoughtNode(
                "Do you already know your options?",
                yes_branch=ThoughtNode(
                    "Are you worried about choosing the wrong option?",
                    yes_branch=ThoughtNode(
                        suggestion="Compare your options using pros, cons, risks, and long-term benefits."
                    ),
                    no_branch=ThoughtNode(
                        suggestion="Choose the option that best matches your values and current goal."
                    )
                ),
                no_branch=ThoughtNode(
                    suggestion="Start by listing at least three possible options before choosing."
                )
            ),
            no_branch=ThoughtNode(
                "Are you feeling overwhelmed by too many thoughts?",
                yes_branch=ThoughtNode(
                    "Can you identify the main problem?",
                    yes_branch=ThoughtNode(
                        suggestion="Focus on the main problem first and break it into smaller steps."
                    ),
                    no_branch=ThoughtNode(
                        suggestion="Do a brain dump, then group similar thoughts into categories."
                    )
                ),
                no_branch=ThoughtNode(
                    suggestion="Take a short break, then write one clear sentence describing what you need."
                )
            )
        )

    def add_thought(self, thought):
        self.thoughts.append(thought)

    def sort_thoughts_by_priority(self):
        for i in range(len(self.thoughts)):
            max_index = i

            for j in range(i + 1, len(self.thoughts)):
                if self.thoughts[j].priority_score > self.thoughts[max_index].priority_score:
                    max_index = j

            temp = self.thoughts[i]
            self.thoughts[i] = self.thoughts[max_index]
            self.thoughts[max_index] = temp

    def apply_to_scores(self, function):
        return list(map(function, self.thoughts))

    def recursive_tree_result(self, node, answers, index=0):
        if node.suggestion is not None:
            return node.suggestion

        if index >= len(answers):
            return "More information is needed to complete the decision path."

        if answers[index] == "yes":
            return self.recursive_tree_result(node.yes_branch, answers, index + 1)
        else:
            return self.recursive_tree_result(node.no_branch, answers, index + 1)

    def create_report(self, answers):
        self.sort_thoughts_by_priority()

        report = "THOUGHT ORGANIZER REPORT\n"
        report += "========================\n\n"

        report += "Ranked Thoughts:\n"

        for i in range(len(self.thoughts)):
            thought = self.thoughts[i]
            report += "\n" + str(i + 1) + ". " + thought.text + "\n"
            report += "Category: " + thought.category + "\n"
            report += "Urgency: " + str(thought.urgency) + "\n"
            report += "Importance: " + str(thought.importance) + "\n"
            report += "Priority Score: " + str(thought.priority_score) + "\n"
            report += "Priority Level: " + thought.get_priority_level() + "\n"

        report += "\nPriority Scores Using map():\n"
        scores = self.apply_to_scores(lambda thought: thought.priority_score)
        report += str(scores) + "\n"

        suggestion = self.recursive_tree_result(self.root, answers)

        report += "\nDecision Tree Suggestion:\n"
        report += suggestion + "\n"

        if len(self.thoughts) > 0:
            highest = self.thoughts[0]
            report += "\nRecommended First Step:\n"
            report += "Start with: " + highest.text + "\n"

            if highest.priority_score >= 8:
                report += "Action: Handle this soon and break it into small steps.\n"
            elif highest.priority_score >= 5:
                report += "Action: Schedule time to work on this.\n"
            else:
                report += "Action: Keep this in mind, but focus on higher priorities first.\n"

        return report


class ThoughtOrganizerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Thought Organizer")
        self.root.geometry("750x700")

        self.organizer = ThoughtOrganizer()

        self.title_label = tk.Label(
            root,
            text="Thought Organizer",
            font=("Arial", 22, "bold")
        )
        self.title_label.pack(pady=10)

        self.description_label = tk.Label(
            root,
            text="A cognitive accessibility tool that organizes overwhelming thoughts into clearer decisions.",
            font=("Arial", 11)
        )
        self.description_label.pack(pady=5)

        self.thought_label = tk.Label(root, text="Enter a thought:")
        self.thought_label.pack()

        self.thought_entry = tk.Entry(root, width=70)
        self.thought_entry.pack(pady=5)

        self.category_label = tk.Label(root, text="Choose a category:")
        self.category_label.pack()

        self.category_var = tk.StringVar()
        self.category_var.set("School")

        self.category_menu = tk.OptionMenu(
            root,
            self.category_var,
            "School",
            "Personal",
            "Family",
            "Friends/Relationships",
            "Future/Goals",
            "Other"
        )
        self.category_menu.pack(pady=5)

        self.urgency_label = tk.Label(root, text="Urgency from 1-5:")
        self.urgency_label.pack()

        self.urgency_entry = tk.Entry(root, width=10)
        self.urgency_entry.pack(pady=5)

        self.importance_label = tk.Label(root, text="Importance from 1-5:")
        self.importance_label.pack()

        self.importance_entry = tk.Entry(root, width=10)
        self.importance_entry.pack(pady=5)

        self.add_button = tk.Button(
            root,
            text="Add Thought",
            command=self.add_thought
        )
        self.add_button.pack(pady=8)

        self.tree_label = tk.Label(
            root,
            text="Decision Tree Questions",
            font=("Arial", 13, "bold")
        )
        self.tree_label.pack(pady=5)

        self.answer1 = tk.StringVar()
        self.answer1.set("yes")

        self.answer2 = tk.StringVar()
        self.answer2.set("yes")

        self.answer3 = tk.StringVar()
        self.answer3.set("yes")

        self.create_question("Are you trying to make a decision?", self.answer1)
        self.create_question("Do you already know your options OR are you overwhelmed?", self.answer2)
        self.create_question("Are you worried about the choice OR can you identify the main problem?", self.answer3)

        self.organize_button = tk.Button(
            root,
            text="Organize Thoughts",
            command=self.organize_thoughts
        )
        self.organize_button.pack(pady=8)

        self.save_button = tk.Button(
            root,
            text="Save Report",
            command=self.save_report
        )
        self.save_button.pack(pady=8)

        self.output_box = tk.Text(root, width=85, height=18)
        self.output_box.pack(pady=10)

    def create_question(self, text, variable):
        frame = tk.Frame(self.root)
        frame.pack()

        label = tk.Label(frame, text=text)
        label.pack(side=tk.LEFT)

        yes_button = tk.Radiobutton(frame, text="Yes", variable=variable, value="yes")
        yes_button.pack(side=tk.LEFT)

        no_button = tk.Radiobutton(frame, text="No", variable=variable, value="no")
        no_button.pack(side=tk.LEFT)

    def validate_number(self, value):
        try:
            number = int(value)

            if number >= 1 and number <= 5:
                return number
            else:
                return None

        except:
            return None

    def add_thought(self):
        text = self.thought_entry.get().strip()
        category = self.category_var.get()
        urgency = self.validate_number(self.urgency_entry.get())
        importance = self.validate_number(self.importance_entry.get())

        if text == "":
            messagebox.showerror("Error", "Please enter a thought.")
            return

        if urgency is None:
            messagebox.showerror("Error", "Urgency must be a number from 1 to 5.")
            return

        if importance is None:
            messagebox.showerror("Error", "Importance must be a number from 1 to 5.")
            return

        thought = Thought(text, category, urgency, importance)
        self.organizer.add_thought(thought)

        messagebox.showinfo("Success", "Thought added successfully.")

        self.thought_entry.delete(0, tk.END)
        self.urgency_entry.delete(0, tk.END)
        self.importance_entry.delete(0, tk.END)

    def organize_thoughts(self):
        if len(self.organizer.thoughts) == 0:
            messagebox.showerror("Error", "Please add at least one thought first.")
            return

        answers = [
            self.answer1.get(),
            self.answer2.get(),
            self.answer3.get()
        ]

        report = self.organizer.create_report(answers)

        self.output_box.delete("1.0", tk.END)
        self.output_box.insert(tk.END, report)

    def save_report(self):
        report = self.output_box.get("1.0", tk.END).strip()

        if report == "":
            messagebox.showerror("Error", "Please organize your thoughts before saving.")
            return

        try:
            file = open("thought_organizer_report.txt", "w")
            file.write(report)
            file.close()

            messagebox.showinfo("Saved", "Report saved as thought_organizer_report.txt")

        except:
            messagebox.showerror("Error", "The report could not be saved.")


def main():
    root = tk.Tk()
    app = ThoughtOrganizerGUI(root)
    root.mainloop()


main()
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


class ThoughtOrganizerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Thought Organizer")
        self.root.geometry("650x600")

        self.thoughts = []

        self.title_label = tk.Label(
            root,
            text="Thought Organizer",
            font=("Arial", 22, "bold")
        )
        self.title_label.pack(pady=10)

        self.description_label = tk.Label(
            root,
            text="Organize overwhelming thoughts into clearer decisions.",
            font=("Arial", 12)
        )
        self.description_label.pack(pady=5)

        self.thought_label = tk.Label(root, text="Enter your thought:")
        self.thought_label.pack()

        self.thought_entry = tk.Entry(root, width=60)
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

        self.urgency_label = tk.Label(root, text="Urgency (1-5):")
        self.urgency_label.pack()

        self.urgency_entry = tk.Entry(root, width=10)
        self.urgency_entry.pack(pady=5)

        self.importance_label = tk.Label(root, text="Importance (1-5):")
        self.importance_label.pack()

        self.importance_entry = tk.Entry(root, width=10)
        self.importance_entry.pack(pady=5)

        self.add_button = tk.Button(
            root,
            text="Add Thought",
            command=self.add_thought
        )
        self.add_button.pack(pady=10)

        self.organize_button = tk.Button(
            root,
            text="Organize Thoughts",
            command=self.organize_thoughts
        )
        self.organize_button.pack(pady=10)

        self.save_button = tk.Button(
            root,
            text="Save Report",
            command=self.save_report
        )
        self.save_button.pack(pady=10)

        self.output_box = tk.Text(root, width=75, height=18)
        self.output_box.pack(pady=10)

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
        self.thoughts.append(thought)

        messagebox.showinfo("Success", "Thought added successfully!")

        self.thought_entry.delete(0, tk.END)
        self.urgency_entry.delete(0, tk.END)
        self.importance_entry.delete(0, tk.END)

    def sort_thoughts_by_priority(self):
        for i in range(len(self.thoughts)):
            max_index = i

            for j in range(i + 1, len(self.thoughts)):
                if self.thoughts[j].priority_score > self.thoughts[max_index].priority_score:
                    max_index = j

            temp = self.thoughts[i]
            self.thoughts[i] = self.thoughts[max_index]
            self.thoughts[max_index] = temp

    def get_suggestion(self, thought):
        if thought.priority_score >= 8:
            return "Handle this soon. Break it into small steps and ask for support if needed."
        elif thought.priority_score >= 5:
            return "Schedule time to work on this after higher-priority tasks."
        else:
            return "Keep this in mind, but do not let it distract you from more urgent thoughts."

    def organize_thoughts(self):
        if len(self.thoughts) == 0:
            messagebox.showerror("Error", "Please add at least one thought first.")
            return

        self.sort_thoughts_by_priority()

        self.output_box.delete("1.0", tk.END)

        self.output_box.insert(tk.END, "THOUGHT ORGANIZER REPORT\n")
        self.output_box.insert(tk.END, "========================\n\n")

        for i in range(len(self.thoughts)):
            thought = self.thoughts[i]

            self.output_box.insert(tk.END, str(i + 1) + ". " + thought.text + "\n")
            self.output_box.insert(tk.END, "Category: " + thought.category + "\n")
            self.output_box.insert(tk.END, "Urgency: " + str(thought.urgency) + "\n")
            self.output_box.insert(tk.END, "Importance: " + str(thought.importance) + "\n")
            self.output_box.insert(tk.END, "Priority Score: " + str(thought.priority_score) + "\n")
            self.output_box.insert(tk.END, "Priority Level: " + thought.get_priority_level() + "\n")
            self.output_box.insert(tk.END, "Suggestion: " + self.get_suggestion(thought) + "\n\n")

        self.output_box.insert(tk.END, "Highest Priority Thought:\n")
        self.output_box.insert(tk.END, self.thoughts[0].text + "\n\n")
        self.output_box.insert(tk.END, "Recommended First Step:\n")
        self.output_box.insert(tk.END, self.get_suggestion(self.thoughts[0]))

    def save_report(self):
        report = self.output_box.get("1.0", tk.END).strip()

        if report == "":
            messagebox.showerror("Error", "Please organize thoughts before saving.")
            return

        try:
            file = open("thought_organizer_gui_report.txt", "w")
            file.write(report)
            file.close()

            messagebox.showinfo(
                "Saved",
                "Report saved as thought_organizer_gui_report.txt"
            )
        except:
            messagebox.showerror("Error", "The report could not be saved.")


def main():
    root = tk.Tk()
    app = ThoughtOrganizerGUI(root)
    root.mainloop()


main()
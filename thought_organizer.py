class ThoughtNode:
    def __init__(self, question=None, yes_branch=None, no_branch=None, suggestion=None):
        self.question = question
        self.yes_branch = yes_branch
        self.no_branch = no_branch
        self.suggestion = suggestion


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


class ThoughtOrganizer:
    def __init__(self):
        self.thoughts = []
        self.responses = []
        self.root = self.build_decision_tree()

    def build_decision_tree(self):
        return ThoughtNode(
            "Are you trying to make a decision right now?",
            yes_branch=ThoughtNode(
                "Do you already know your options?",
                yes_branch=ThoughtNode(
                    "Are you worried about choosing the wrong option?",
                    yes_branch=ThoughtNode(
                        suggestion="Compare the pros and cons of each option. Then choose the option with the best long-term benefit and lowest serious risk."
                    ),
                    no_branch=ThoughtNode(
                        suggestion="Choose the option that best matches your values, goal, and current situation."
                    )
                ),
                no_branch=ThoughtNode(
                    suggestion="Start by listing at least three possible options. Even imperfect options can help you think more clearly."
                )
            ),
            no_branch=ThoughtNode(
                "Are you feeling overwhelmed by too many thoughts?",
                yes_branch=ThoughtNode(
                    "Can you identify one main problem?",
                    yes_branch=ThoughtNode(
                        suggestion="Focus on the main problem first. Break it into smaller steps and complete the easiest step first."
                    ),
                    no_branch=ThoughtNode(
                        suggestion="Do a brain dump. Write everything down, then group similar thoughts into categories."
                    )
                ),
                no_branch=ThoughtNode(
                    suggestion="Take a short break, then write one clear sentence describing what you need to organize."
                )
            )
        )

    def get_yes_no(self, question):
        while True:
            try:
                answer = input(question + " (yes/no): ").strip().lower()

                if answer == "yes" or answer == "y":
                    return "yes"
                elif answer == "no" or answer == "n":
                    return "no"
                else:
                    print("Please type yes or no.")
            except:
                print("Something went wrong. Please try again.")

    def get_number(self, question, minimum, maximum):
        valid = False
        number = 0

        while not valid:
            try:
                number = int(input(question))
                if number >= minimum and number <= maximum:
                    valid = True
                else:
                    print("Please enter a number from", minimum, "to", maximum)
            except:
                print("Invalid input. Please enter a number.")

        return number

    def get_category(self):
        print("\nChoose a category:")
        print("1. School")
        print("2. Personal")
        print("3. Family")
        print("4. Friends/Relationships")
        print("5. Future/Goals")
        print("6. Other")

        choice = self.get_number("Enter a number from 1-6: ", 1, 6)

        if choice == 1:
            return "School"
        elif choice == 2:
            return "Personal"
        elif choice == 3:
            return "Family"
        elif choice == 4:
            return "Friends/Relationships"
        elif choice == 5:
            return "Future/Goals"
        else:
            return "Other"

    def collect_thoughts(self):
        print("\nFirst, you will enter the thoughts you want to organize.")
        print("You can enter up to 5 thoughts.")

        total = self.get_number("\nHow many thoughts would you like to organize? ", 1, 5)

        for i in range(total):
            print("\nThought", i + 1)

            text = input("Write your thought: ").strip()
            while text == "":
                print("Thought cannot be empty.")
                text = input("Write your thought: ").strip()

            category = self.get_category()
            urgency = self.get_number("How urgent is this thought? (1-5): ", 1, 5)
            importance = self.get_number("How important is this thought? (1-5): ", 1, 5)

            thought = Thought(text, category, urgency, importance)
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

    def organize_with_tree(self, node):
        if node.suggestion is not None:
            return node.suggestion

        answer = self.get_yes_no(node.question)
        self.responses.append((node.question, answer))

        if answer == "yes":
            return self.organize_with_tree(node.yes_branch)
        else:
            return self.organize_with_tree(node.no_branch)

    def create_action_plan(self):
        plan = []

        if len(self.thoughts) == 0:
            return plan

        top_thought = self.thoughts[0]

        plan.append("1. Start with your highest priority thought: " + top_thought.text)
        plan.append("2. Category: " + top_thought.category)
        plan.append("3. Priority level: " + top_thought.get_priority_level())

        if top_thought.priority_score >= 8:
            plan.append("4. Recommended action: Handle this soon. Break it into small steps and ask for support if needed.")
        elif top_thought.priority_score >= 5:
            plan.append("4. Recommended action: Schedule time to work on this after any urgent tasks are handled.")
        else:
            plan.append("4. Recommended action: Keep this in mind, but do not let it distract you from higher priorities.")

        return plan

    def display_report(self, suggestion, plan):
        print("\n===================================")
        print("        THOUGHT ORGANIZER REPORT")
        print("===================================")

        print("\nYour thoughts ranked by priority:")
        for i in range(len(self.thoughts)):
            thought = self.thoughts[i]
            print("\n" + str(i + 1) + ". " + thought.text)
            print("   Category:", thought.category)
            print("   Urgency:", thought.urgency)
            print("   Importance:", thought.importance)
            print("   Priority Score:", thought.priority_score)
            print("   Priority Level:", thought.get_priority_level())

        print("\nDecision Tree Responses:")
        for question, answer in self.responses:
            print("- " + question + " Answer: " + answer)

        print("\nMain Suggestion:")
        print(suggestion)

        print("\nAction Plan:")
        for step in plan:
            print(step)

    def save_report(self, suggestion, plan):
        answer = self.get_yes_no("\nWould you like to save this report to a text file?")

        if answer == "yes":
            try:
                file = open("thought_organizer_report.txt", "w")

                file.write("THOUGHT ORGANIZER REPORT\n")
                file.write("========================\n\n")

                file.write("Thoughts ranked by priority:\n")

                for i in range(len(self.thoughts)):
                    thought = self.thoughts[i]
                    file.write("\n" + str(i + 1) + ". " + thought.text + "\n")
                    file.write("Category: " + thought.category + "\n")
                    file.write("Urgency: " + str(thought.urgency) + "\n")
                    file.write("Importance: " + str(thought.importance) + "\n")
                    file.write("Priority Score: " + str(thought.priority_score) + "\n")
                    file.write("Priority Level: " + thought.get_priority_level() + "\n")

                file.write("\nDecision Tree Responses:\n")
                for question, answer in self.responses:
                    file.write("- " + question + " Answer: " + answer + "\n")

                file.write("\nMain Suggestion:\n")
                file.write(suggestion + "\n")

                file.write("\nAction Plan:\n")
                for step in plan:
                    file.write(step + "\n")

                file.close()
                print("Your report was saved as thought_organizer_report.txt")

            except:
                print("The report could not be saved.")

    def run(self):
        print("Welcome to Thought Organizer!")
        print("This program helps users organize overwhelming thoughts into clearer decisions.")
        print("It uses objects, a decision tree, recursion, validation, and priority scoring.")

        self.collect_thoughts()
        self.sort_thoughts_by_priority()

        print("\nNow answer a few questions so the program can guide your next step.")
        suggestion = self.organize_with_tree(self.root)

        plan = self.create_action_plan()

        self.display_report(suggestion, plan)
        self.save_report(suggestion, plan)


def main():
    organizer = ThoughtOrganizer()
    organizer.run()


main()
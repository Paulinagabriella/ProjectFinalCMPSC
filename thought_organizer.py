class ThoughtNode:
    def __init__(self, question, yes_branch=None, no_branch=None, suggestion=None):
        self.question = question
        self.yes_branch = yes_branch
        self.no_branch = no_branch
        self.suggestion = suggestion


class ThoughtOrganizer:
    def __init__(self):
        self.root = self.build_tree()
        self.responses = []

    def build_tree(self):
        return ThoughtNode(
            "Are you trying to make a decision?",
            yes_branch=ThoughtNode(
                "Do you already know your options?",
                yes_branch=ThoughtNode(
                    "Are you worried about making the wrong choice?",
                    yes_branch=ThoughtNode(
                        None,
                        suggestion="Write down the pros and cons of each option, then choose the one with the most benefits and least serious risks."
                    ),
                    no_branch=ThoughtNode(
                        None,
                        suggestion="Choose the option that best matches your goal and values."
                    )
                ),
                no_branch=ThoughtNode(
                    None,
                    suggestion="Start by listing all possible options, even if they are not perfect. Then narrow them down."
                )
            ),
            no_branch=ThoughtNode(
                "Are you feeling overwhelmed by too many thoughts?",
                yes_branch=ThoughtNode(
                    "Can you identify the main problem?",
                    yes_branch=ThoughtNode(
                        None,
                        suggestion="Focus only on the main problem first. Break it into smaller steps and complete one step at a time."
                    ),
                    no_branch=ThoughtNode(
                        None,
                        suggestion="Do a brain dump: write everything on your mind, then group similar thoughts together."
                    )
                ),
                no_branch=ThoughtNode(
                    None,
                    suggestion="Take a short break, then return and write one sentence describing what you need help organizing."
                )
            )
        )

    def get_valid_answer(self, question):
        while True:
            try:
                answer = input(question + " (yes/no): ").strip().lower()

                if answer in ["yes", "y"]:
                    return "yes"
                elif answer in ["no", "n"]:
                    return "no"
                else:
                    print("Please enter yes or no.")

            except Exception:
                print("An error occurred. Please try again.")

    def organize_thoughts(self, node):
        if node.suggestion is not None:
            return node.suggestion

        answer = self.get_valid_answer(node.question)
        self.responses.append((node.question, answer))

        if answer == "yes":
            return self.organize_thoughts(node.yes_branch)
        else:
            return self.organize_thoughts(node.no_branch)

    def display_summary(self, suggestion):
        print("\n--- Thought Organizer Summary ---")

        print("\nYour responses:")
        for question, answer in self.responses:
            print("- " + question + " Answer: " + answer)

        print("\nSuggested next step:")
        print(suggestion)

    def run(self):
        print("Welcome to Thought Organizer!")
        print("This program will help you organize your thoughts into clearer next steps.\n")

        suggestion = self.organize_thoughts(self.root)
        self.display_summary(suggestion)


def main():
    organizer = ThoughtOrganizer()
    organizer.run()


main()
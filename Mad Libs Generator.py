import random


class MadLibsGenerator:
    def __init__(self):
        self.stories = [
            "Once upon a time, there was a {adjective} {noun} named {name}. {pronoun} loved to {verb} {adverb}.",
            "In a {adjective} land, there lived a {noun}. {pronoun} always wanted to {verb} {adverb}.",
            "The {adjective} {noun} {verb} into a {adjective} forest with {number} {plural_noun}.",
            "Deep in the heart of {adjective} {noun}, {name} discovered a magical {singular_noun} and decided to {verb} it {number} times.",
            "{name} and {pronoun} embarked on a quest to find the legendary {adjective} {noun}. Along the way, they encountered {number} {plural_noun} who {adverb} {verb}.",
        ]

    def generate_story(self):
        # Get user input
        self.name = input("Enter a name: ")
        self.adjective = input("Enter an adjective: ")
        self.noun = input("Enter a noun: ")
        self.pronoun = input("Enter a pronoun (he/she/they): ")
        self.verb = input("Enter a verb: ")
        self.adverb = input("Enter an adverb: ")
        self.number = input("Enter a number: ")
        self.plural_noun = input("Enter a plural noun: ")

        # Select a random story
        selected_story = random.choice(self.stories)

        # Generate and return the selected story
        story = selected_story.format(
            name=self.name,
            adjective=self.adjective,
            noun=self.noun,
            pronoun=self.pronoun,
            verb=self.verb,
            adverb=self.adverb,
            number=self.number,
            plural_noun=self.plural_noun,
        )
        return story

    def run(self):
        # Generate and display a story
        story = self.generate_story()
        print("\nHere's your randomly generated story:")
        print(story)


if __name__ == "__main__":
    mad_libs = MadLibsGenerator()
    mad_libs.run()

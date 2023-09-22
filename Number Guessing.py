import random


class NumberGuessingGame:
    def __init__(self, min_num=1, max_num=100, max_attempts=10):
        self.min_num = min_num
        self.max_num = max_num
        self.max_attempts = max_attempts
        self.secret_number = random.randint(min_num, max_num)
        self.attempts = 0
        self.score = max_attempts

    def get_guess(self):
        while True:
            try:
                guess = int(input(f"Guess the number between {self.min_num} and {self.max_num}: "))
                if self.min_num <= guess <= self.max_num:
                    return guess
                else:
                    print(f"Please enter a number between {self.min_num} and {self.max_num}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def play(self):
        print("Welcome to the Number Guessing Game!")
        print(f"You have {self.max_attempts} attempts to guess the number.")
        while self.attempts < self.max_attempts:
            guess = self.get_guess()
            self.attempts += 1

            if guess == self.secret_number:
                print(f"Congratulations! You guessed the number {self.secret_number} in {self.attempts} attempts.")
                print(f"Your score is: {self.score}")
                break
            else:
                if self.attempts == self.max_attempts:
                    print(
                        f"Sorry, you've reached the maximum number of attempts. The secret number was {self.secret_number}.")
                else:
                    print(f"Wrong guess. Try again.")
                    self.score -= 1
                    if guess < self.secret_number:
                        print("Hint: The secret number is higher.")
                    else:
                        print("Hint: The secret number is lower.")
                    print(f"Attempts left: {self.max_attempts - self.attempts}")
                    print(f"Current score: {self.score}")


if __name__ == "__main__":
    game = NumberGuessingGame()
    game.play()

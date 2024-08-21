import random

def get_valid_number(prompt):
    while True:
        value = input(prompt)
        if value.isdigit():
            value = int(value)
            if value > 0:
                return value
            else:
                print('Please type a number larger than 0 next time.')
        else:
            print('Please type a valid number next time.')

def main():
    top_of_range = get_valid_number("Type a number: ")

    random_number = random.randint(0, top_of_range)
    guesses = 0

    while True:
        guesses += 1
        user_guess = get_valid_number("Make a guess: ")

        if user_guess == random_number:
            # print("You got it!")
            break
        elif user_guess > random_number:
            print("You were above the number!")
        else:
            print("You were below the number!")

    print("You got it in", guesses, "guesses")

if __name__ == "__main__":
    main()

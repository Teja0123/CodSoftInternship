import random

# Initialize player and computer scores
player_score = 0
computer_score = 0

while True:
    # User's choice
    player_choice = input("Choose rock, paper, or scissors (or 'quit' to exit): ").lower()

    if player_choice == "quit":
        break

    if player_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue

    # Computer's choice
    computer_choice = random.choice(["rock", "paper", "scissors"])

    print(f"Your choice: {player_choice}")
    print(f"Computer's choice: {computer_choice}")

    # Determine the winner of the round
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (
        (player_choice == "rock" and computer_choice == "scissors")
        or (player_choice == "paper" and computer_choice == "rock")
        or (player_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win this round!")
        player_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    # Display current scores
    print(f"Your score: {player_score}")
    print(f"Computer's score: {computer_score}")
    print("")

# Display the final scores
print("Game over!")
print(f"Your final score: {player_score}")
print(f"Computer's final score: {computer_score}")

import random

# Emoji representations
emoji_choices = {
    "rock": "🪨",
    "paper": "📄",
    "scissors": "✂️"
}

def get_computer_choice():
    return random.choice(list(emoji_choices.keys()))

def get_winner(user, computer):
    if user == computer:
        return "🤝 It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "🎉 You win!"
    else:
        return "💻 Computer wins!"

def play_game():
    print("🎮 Welcome to Rock, Paper, Scissors (Emoji Edition)!")
    print("Choose one: rock 🪨, paper 📄, or scissors ✂️\n")

    while True:
        user_choice = input("Your choice (rock/paper/scissors): ").lower()
        if user_choice not in emoji_choices:
            print("❌ Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()

        print(f"\nYou chose: {emoji_choices[user_choice]} ({user_choice})")
        print(f"Computer chose: {emoji_choices[computer_choice]} ({computer_choice})")

        result = get_winner(user_choice, computer_choice)
        print(result)

        play_again = input("\n🔁 Play again? (yes/no): ").lower()
        if play_again != "yes":
            print("👋 Thanks for playing!")
            break

# Start the game
play_game()

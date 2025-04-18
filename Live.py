

def welcome(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f"Hello {name} and welcome to the World of Games (WoG).")
    print(f"Here you can find many cool games to play.")


def get_valid_integer_input(prompt: str, min_value: int, max_value: int) -> int:
    while True:
        try:
            user_input = int(input(prompt))
            if min_value <= user_input <= max_value:
                return user_input
            else:
                print(f"Invalid input. Please enter a value between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def display_game_menu():
    print("\n Please choose a game to play:")
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    print("2. Guess Game - guess a number and see if you chose like the computer")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")


def load_game():
    try:
        display_game_menu()
        game_choice: int = get_valid_integer_input(
            prompt="Enter your choice: ",
            min_value=1,
            max_value=3
        )

        difficulty_level:int = get_valid_integer_input(
            prompt= "Enter game difficulty level: ",
            min_value=1,
            max_value=5
        )

        games = {
            1: "start_memory_game",
            2: "start_guess_game",
            3: "start_currency_roulette"
        }

        print(f"\nStarting game with difficulty {difficulty_level}...")
        return games[game_choice]
    except Exception as e:
        print(f"Error loading game: {e}")
        return None



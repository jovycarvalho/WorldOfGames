from Live import welcome, load_game


def get_player_name() -> str:
    name: str = str(input("What is your name? ")).strip()
    return  name

def main():
    name: str = get_player_name()
    welcome(name)
    print(load_game())

if __name__ == "__main__":
    main()
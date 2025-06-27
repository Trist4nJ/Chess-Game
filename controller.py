from game import Game

class ChessApp:
    def __init__(self):
        self.game = None

    def print_welcome_message(self):
        print("▖  ▖  ▜                  ▄▖▌       ▄▖    ▌\n"
              "▌▞▖▌█▌▐ ▛▘▛▌▛▛▌█▌  ▛▌▛▌  ▌ ▛▌█▌▛▘▛▘▙▌▌▌  ▌\n"
              "▛ ▝▌▙▖▐▖▙▖▙▌▌▌▌▙▖  ▙▌▌▌  ▙▖▌▌▙▖▄▌▄▌▌ ▙▌  ▖\n"
              "                                     ▄▌   \n"
              )

    def show_menu(self):
        while True:
            try:
                choice = int(input("\nPlease choose an option:\n"
                                   "1 - Start a normal game\n"
                                   "2 - Show the rules of the game\n"
                                   "3 - Play against the AI\n"
                                   "4 - Quit the game\n"))
                if 1 <= choice <= 4:
                    return choice
                else:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def run(self):
        self.print_welcome_message()
        while True:
            choice = self.show_menu()

            if choice == 1:
                self.game = Game()
                self.game.launch_game()

            elif choice == 2:
                f = open("rules.txt", "r")
                content = f.read()
                print(content)
                f.close()

            elif choice == 3:
                print("Hi! My name is Omega, the very first AI of this software! Let's start with black pieces...\n")

            elif choice == 4:
                print("Thanks for playing! See you soon! 😁")
                exit()

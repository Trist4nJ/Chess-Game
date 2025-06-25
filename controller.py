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
                                   "4 - Two-player local mode\n"
                                   "5 - Load a saved game\n"
                                   "6 - Quit the game\n"))
                if 1 <= choice <= 6:
                    return choice
                else:
                    print("Please enter a number between 1 and 6.")
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
                print("This will be implemented soon!")

            elif choice == 4:
                print("This will be implemented soon!")

            elif choice == 5:
                print("This will be implemented soon!")

            elif choice == 6:
                print("Thanks for playing! See you soon! 😁")
                exit()

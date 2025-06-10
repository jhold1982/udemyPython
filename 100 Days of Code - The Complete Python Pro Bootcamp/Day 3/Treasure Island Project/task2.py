class AdventureGame:
    def __init__(self):
        self.current_scene = "start"
        self.player_name = ""
        self.inventory = []
        self.health = 100

    def display_status(self):
        print(f"\n--- Status ---")
        print(f"Health: {self.health}")
        print(f"Inventory: {', '.join(self.inventory) if self.inventory else 'Empty'}")
        print("-" * 15)

    def get_player_choice(self, options):
        while True:
            try:
                print("\nWhat do you choose?")
                for i, option in enumerate(options, 1):
                    print(f"{i}. {option}")

                choice = int(input("Enter your choice (number): ")) - 1
                if 0 <= choice < len(options):
                    return choice
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a valid number.")

    def start_scene(self):
        print("=" * 50)
        print("Welcome to the Mysterious Forest Adventure!")
        print("=" * 50)

        self.player_name = input("What is your name, brave adventurer? ")
        print(f"\nHello, {self.player_name}! Your adventure begins now...")

        print(f"\nYou find yourself at the edge of a dark, mysterious forest.")
        print("Strange sounds echo from within, but you notice a glimmer of treasure deep inside.")

        options = [
            "Enter the forest boldly",
            "Look for a weapon first",
            "Turn back and go home"
        ]

        choice = self.get_player_choice(options)

        if choice == 0:
            self.current_scene = "forest_entrance"
        elif choice == 1:
            self.current_scene = "find_weapon"
        else:
            self.current_scene = "go_home"

    def find_weapon_scene(self):
        print(f"\n{self.player_name}, you decide to search for a weapon.")
        print("You find an old wooden stick that could serve as a club.")

        self.inventory.append("wooden club")
        print("You pick up the wooden club.")

        options = [
            "Now enter the forest",
            "Look for more supplies",
            "Change your mind and go home"
        ]

        choice = self.get_player_choice(options)

        if choice == 0:
            self.current_scene = "forest_entrance"
        elif choice == 1:
            self.current_scene = "find_supplies"
        else:
            self.current_scene = "go_home"

    def find_supplies_scene(self):
        print(f"\nYou search around and find some berries and a small healing potion.")

        self.inventory.extend(["berries", "healing potion"])
        print("You gather the berries and healing potion.")

        options = [
            "Finally enter the forest",
            "Go home with your supplies"
        ]

        choice = self.get_player_choice(options)

        if choice == 0:
            self.current_scene = "forest_entrance"
        else:
            self.current_scene = "go_home"

    def forest_entrance_scene(self):
        print(f"\n{self.player_name}, you step into the forest.")
        print("The trees tower above you, blocking out most of the sunlight.")
        print("You hear a rustling in the bushes ahead.")

        options = [
            "Investigate the rustling sound",
            "Try to sneak around quietly",
            "Call out 'Hello? Is anyone there?'"
        ]

        choice = self.get_player_choice(options)

        if choice == 0:
            self.current_scene = "encounter_creature"
        elif choice == 1:
            self.current_scene = "sneak_path"
        else:
            self.current_scene = "call_out"

    def encounter_creature_scene(self):
        print(f"\nYou push through the bushes and come face to face with a large, angry bear!")
        print("The bear rears up on its hind legs and roars!")

        fight_options = ["Fight the bear"]
        if "wooden club" in self.inventory:
            fight_options.append("Fight with your wooden club")
        if "healing potion" in self.inventory:
            fight_options.append("Throw the healing potion and run")
        fight_options.extend(["Try to back away slowly", "Run away screaming"])

        choice = self.get_player_choice(fight_options)

        if choice == 0:  # Fight with bare hands
            self.health -= 50
            print(f"\nYou fight the bear with your bare hands!")
            print(f"You manage to scare it off, but you're badly injured.")
            print(f"Health reduced to {self.health}")
            self.current_scene = "after_bear"
        elif "Fight with your wooden club" in fight_options and choice == 1:
            self.health -= 20
            print(f"\nYou fight the bear with your wooden club!")
            print(f"The club helps! You drive the bear away with only minor injuries.")
            print(f"Health reduced to {self.health}")
            self.current_scene = "after_bear"
        elif "Throw the healing potion and run" in fight_options and choice == len(fight_options) - 3:
            self.inventory.remove("healing potion")
            print(f"\nYou throw the healing potion at the bear and run!")
            print(f"The bear is distracted by the strange liquid. You escape unharmed!")
            self.current_scene = "deeper_forest"
        elif choice == len(fight_options) - 2:  # Back away slowly
            print(f"\nYou slowly back away from the bear.")
            print(f"The bear watches you but doesn't attack. You escape safely!")
            self.current_scene = "alternate_path"
        else:  # Run away screaming
            self.health -= 10
            print(f"\nYou run away screaming!")
            print(f"You trip and scrape your knee while running.")
            print(f"Health reduced to {self.health}")
            self.current_scene = "back_to_start"

    def sneak_path_scene(self):
        print(f"\nYou carefully sneak around the rustling bushes.")
        print("You successfully avoid whatever was making the noise!")
        print("You find a hidden path deeper into the forest.")

        options = [
            "Follow the hidden path",
            "Go back and investigate the rustling"
        ]

        choice = self.get_player_choice(options)

        if choice == 0:
            self.current_scene = "treasure_room"
        else:
            self.current_scene = "encounter_creature"

    def treasure_room_scene(self):
        print(f"\n{self.player_name}, you follow the hidden path and discover a small clearing!")
        print("In the center of the clearing, you find a chest filled with gold coins!")
        print("You've found the treasure!")

        self.inventory.append("treasure chest")

        print(f"\nCongratulations! You've successfully completed your adventure!")
        print(f"You return home safely with the treasure.")
        self.current_scene = "victory"

    def go_home_scene(self):
        print(f"\n{self.player_name}, you decide that discretion is the better part of valor.")
        print("You return home safely, but without any treasure.")
        print("Perhaps another day you'll be brave enough to explore the forest.")
        self.current_scene = "end"

    def game_over_scene(self):
        print(f"\nGame Over, {self.player_name}!")
        print("Your health has reached zero. Better luck next time!")
        self.current_scene = "end"

    def victory_scene(self):
        print(f"\n🎉 VICTORY! 🎉")
        print(f"You've completed your adventure successfully!")
        self.display_status()
        self.current_scene = "end"

    def play(self):
        scenes = {
            "start": self.start_scene,
            "find_weapon": self.find_weapon_scene,
            "find_supplies": self.find_supplies_scene,
            "forest_entrance": self.forest_entrance_scene,
            "encounter_creature": self.encounter_creature_scene,
            "sneak_path": self.sneak_path_scene,
            "treasure_room": self.treasure_room_scene,
            "go_home": self.go_home_scene,
            "victory": self.victory_scene,
            "game_over": self.game_over_scene
        }

        while self.current_scene != "end":
            self.display_status()

            if self.health <= 0:
                self.current_scene = "game_over"

            if self.current_scene in scenes:
                scenes[self.current_scene]()
            else:
                print("You continue your adventure...")
                break

        print(f"\nThank you for playing, {self.player_name}!")
        print("The adventure ends here.")


# Run the game
if __name__ == "__main__":
    game = AdventureGame()
    game.play()

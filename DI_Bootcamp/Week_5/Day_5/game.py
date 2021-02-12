import random


class Game:

    def __init__(self):
        self.result_dict = dict()

    
    def get_user_item(self):
        user_item = input("Choose (r) for rock, (p), for paper or (s) for scissors")
        while user_item not in ("r", "p", "s"):
            user_item = input("Choose (r) for rock, (p), for paper or (s) for scissors")
        return user_item


    def get_computer_item(self):
        item_list = ["r", "p", "s"]
        computer_item = random.choice(item_list)
        return computer_item


    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            print(f"Both chose {user_item}. It's a draw")
            return "draw"
        
        elif user_item == "r":
            if computer_item == "p":
                print(f"You picked {user_item} and the computer picked {computer_item}. You lost")
                return "loss"
            else:
                print(f"You picked {user_item}")
                return "win"
        
        elif user_item == "p":
            if computer_item == "s":
                print("You lost to scissors with paper")
                return "loss"
            else:
                print("You won with paper against scissors")
                return "win"

        else:
            if computer_item == "r":
                print("You lost to rock with scissors")
                return "loss"
            else:
                print("You won with scissors against paper")
                return "win"


    def play(self):

        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        if result == "win":
            if "win" not in self.result_dict:
                self.result_dict["win"] = 1
            else:
                self.result_dict["win"] += 1
        elif result == "loss":
            if "loss" not in self.result_dict:
                self.result_dict["loss"] = 1
            else:
                self.result_dict["loss"] += 1
        else:
            if "draw" not in self.result_dict:
                self.result_dict["draw"] = 1
            else:
                self.result_dict["draw"] += 1

        return self.result_dict    
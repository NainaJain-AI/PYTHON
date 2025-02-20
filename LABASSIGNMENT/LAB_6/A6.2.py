import random

class RockPaperScissors:
    def __init__(self, total_rounds):
        self.total_rounds, self.current_round, self.user_wins, self.computer_wins = total_rounds, 0, 0, 0
        self.choices = ["rock", "paper", "scissors"]

    def play_round(self, user_choice):
        if user_choice not in self.choices:
            return "Invalid choice. Choose rock, paper, or scissors."
        self.current_round += 1
        computer_choice = random.choice(self.choices)
        result = f"Round {self.current_round}: User chose {user_choice}, Computer chose {computer_choice}. "
        if user_choice == computer_choice:
            return result + "It's a draw!"
        winner = "user" if (user_choice, computer_choice) in [("rock", "scissors"), ("scissors", "paper"), ("paper", "rock")] else "computer"
        self.user_wins += winner == "user"
        self.computer_wins += winner == "computer"
        return result + ("User wins!" if winner == "user" else "Computer wins!")
    
    def play_game(self):
        while self.current_round < self.total_rounds and self.user_wins <= self.total_rounds // 2 and self.computer_wins <= self.total_rounds // 2:
            print(self.play_round(input("Enter rock, paper, or scissors: ").strip().lower()))
            if (self.user_wins!=self.computer_wins)and (self.current_round==self.total_rounds):
                   print("Game over!", "User wins the game!" if self.user_wins > self.computer_wins else "Computer wins the game!")
            elif(self.user_wins==self.computer_wins)and (self.current_round==self.total_rounds):
                print("game over!","it's a draww")
game = RockPaperScissors(5)
game.play_game()

    
      






    
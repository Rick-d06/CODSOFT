import random
def start_game():
    print("Welcome to the game")
    player_score = 0
    computer_score = 0
    while True:
      options = ["rock", "paper", "scissors"]
      exit_game = input("Do you want to exit the game? (yes/no): ")
      if exit_game.lower() == "yes":
          break

      user_choice = input("Enter a choice (rock, paper, scissors): ")
      computer_choice = random.choice(options)
      if user_choice not in options:
          print("Invalid choice")
      else:
          print(f"You chose {user_choice}, computer chose {computer_choice}")
          if user_choice == computer_choice:
              print("It's a tie!")
          elif user_choice == "rock":
              if computer_choice == "scissors":
                  print("You win!")
                  player_score += 1
              else:
                  print("You lose!")
                  computer_score += 1

          elif user_choice == "paper":
              if computer_choice == "rock":
                  print("You win!")
                  player_score += 1
              else:
                  print("You lose!")
                  computer_score += 1

          elif user_choice == "scissors":
              if computer_choice == "paper":
                  print("You win!")
                  player_score += 1
              else:
                  print("You lose!")
                  computer_score += 1



      print(f"Your score: {player_score}")
      print(f"Computer's score: {computer_score}")

start_game()

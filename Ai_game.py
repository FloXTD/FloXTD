import random
from collections import defaultdict, deque
import numpy as np

# Simple Neural Network class
class SimpleNN:
    def __init__(self):
        self.weights = {"rock": 1, "paper": 1, "scissors": 1}
        
    def predict(self, history):
        if len(history) < 2:
            return random.choice(["rock", "paper", "scissors"])
        move_sequence = ''.join(history[-2:])
        if move_sequence == 'rockpaper':
            return 'scissors'
        elif move_sequence == 'paperscissors':
            return 'rock'
        elif move_sequence == 'scissorsrock':
            return 'paper'
        return random.choice(["rock", "paper", "scissors"])

def rps_with_advancements():
    options = ["rock", "paper", "scissors"]
    move_history = deque(maxlen=5)  # Track the last 5 moves
    transition_probabilities = defaultdict(lambda: {"rock": 0, "paper": 0, "scissors": 0})
    weights = {"rock": 1, "paper": 1, "scissors": 1}  # For weight-based prediction
    nn = SimpleNN()  # Instantiate the simple neural network
    
    scores = {"player": 0, "ai": 0, "ties": 0}  # Scoreboard

    print("Let's play Rock, Paper, Scissors! Type 'exit' to quit.")

    while True:
        # Markov Chain: Predict based on the transition probabilities
        if len(move_history) >= 2:
            last_move = move_history[-1]
            predicted_move = max(transition_probabilities[last_move], key=transition_probabilities[last_move].get)
        else:
            predicted_move = random.choice(options)

        # Weight-Based Prediction: Consider the player's most frequent move
        if random.random() < 0.2:  # 20% randomness
            ai_choice = random.choice(options)
        else:
            ai_choice = {
                "rock": "paper",     # Paper beats Rock
                "paper": "scissors", # Scissors beats Paper
                "scissors": "rock"   # Rock beats Scissors
            }[predicted_move]

        # Neural Network Prediction: Use the simple NN to predict the next move
        nn_prediction = nn.predict(list(move_history))  # Simple NN prediction

        # Final AI decision: Mix predictions from Markov Chain, weights, and NN
        if random.random() < 0.5:
            ai_choice = nn_prediction
        else:
            ai_choice = ai_choice

        # Player's turn
        player_choice = input("\nChoose rock, paper, or scissors: ").strip().lower()
        if player_choice == "exit":
            print("\nFinal Scores:")
            print(f"Player: {scores['player']}, AI: {scores['ai']}, Ties: {scores['ties']}")
            print("Thanks for playing!")
            break
        if player_choice not in options:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        print(f"AI chose: {ai_choice}")
        if ai_choice == player_choice:
            print("It's a tie!")
            scores["ties"] += 1
        elif (player_choice == "rock" and ai_choice == "scissors") or \
             (player_choice == "paper" and ai_choice == "rock") or \
             (player_choice == "scissors" and ai_choice == "paper"):
            print("You win!")
            scores["player"] += 1
        else:
            print("AI wins!")
            scores["ai"] += 1

        # Update transition probabilities for Markov Chain
        if len(move_history) >= 1:
            transition_probabilities[move_history[-1]][player_choice] += 1

        # Update recent moves for weight-based prediction and NN
        move_history.append(player_choice)

        # Display updated scoreboard
        print("\nScoreboard:")
        print(f"Player: {scores['player']}, AI: {scores['ai']}, Ties: {scores['ties']}")

# Start the game
rps_with_advancements()

import random
print("================================")
print("Rock Paper Scissors Lizard Spock")
print("================================\n")
print("1) ✊ Rock")
print("2) ✋ Paper")
print("3) ✌️ Scissors")
print("4) 🦎 Lizard")
print("5) 🖖 Spock")
player = int(input("Pick a number from 1-5: "))
computer = random.randint(1,5)
choices = {
    1: "✊",  # Rock
    2: "✋",  # Paper
    3: "✌️",  # Scissors
    4: "🦎",  # Lizard
    5: "🖖"   # Spock
}
print(f"\nYou choose: {choices[player]}")
print(f"CPU choose: {choices[computer]}")
wins = [
    (3,2),
    (2,1),
    (1,4),
    (4,5),
    (5,3),
    (3,4),
    (4,2),
    (2,5),
    (5,1),
    (1,3)
]
if(player == computer):
    print("It's a tie!")
elif(player, computer) in wins:
    print("You Won!")
else:
    print("CPU won!")
import random
import art
def wants_to_play():
    wants_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':\n")
    if wants_play == "n":
        return False
    elif wants_play == "y":
        return True

def draw_card(each_cards):
    current_score1 = 0
    each_cards.append(random.choice(cards))
    for i in each_cards:
        current_score1 += i
    return current_score1

def draw_or_pass():
    draw_or_pass1 = input("Type 'y' to get another card, type 'n' to pass:\n")
    if draw_or_pass1 == "n":
        return False
    elif draw_or_pass1 == "y":
        return True

def score_print(my_cards, my_score, computer_):
    print(f"Your {my_cards}:  {your_cards}, {my_score}:  {current_score}\nComputer's {computer_}: {computer_cards},"
          f" {my_score}: {computer_score}")

def bust_check(score, person, state1, state2):
    if score == 21:
        print(f"{person} got Blackjack! You {state1}")
        return wants_to_play()
    elif score > 21:
        print(f"{person} went over 21. You {state2}")
        return wants_to_play()


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
print(art.logo)
play = wants_to_play()
while play is True:
    your_cards = []
    computer_cards = []
    your_cards.append(random.choice(cards))
    current_score = draw_card(your_cards)
    computer_score = draw_card(computer_cards)
    score_print("cards", "current score", "first card")
    play = bust_check(current_score, "You", "Win!", "Lose...")
    draw = True
    if current_score >= 21:
        draw = False
    while draw is True:
        draw = draw_or_pass()
        if draw is True:
            current_score = draw_card(your_cards)
            score_print("cards", "current score", "first card")
            if current_score >= 21:
                draw = False
        play = bust_check(current_score, "You", "Win!", "Lose...")
    if current_score < 21:
        while computer_score < 17:
            computer_score = draw_card(computer_cards)
        score_print("final hand", "final score", "final hand")
        play = bust_check(computer_score, "Computer", "Lose...", "Win!")
        if computer_score == current_score and not computer_score >= 21:
            print("Game ended in a DRAW..!!")
            play = wants_to_play()
        elif computer_score > current_score and not computer_score >= 21:
            print("Computer Won..")
            play = wants_to_play()
        elif computer_score < current_score and not computer_score >= 21:
            print("You Won!!")
            play = wants_to_play()
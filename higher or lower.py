import random

from game_data import data

def format_data(account):
    return f"{account['name']}, a {account['description']}, from {account['country']}"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        if guess == "a":
            return True
        else:
            return False
    else:
        if guess == "b":
            return True
        else:
            return False

score = 0
running = True

account_b = random.choice(data)

while running:

    account_a = account_b
    account_b = random.choice(data)
    
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print("==================== VS ======================")
    print(f"Compare B: {format_data(account_b)}")

    guess = input("Who has more followers? Type A or B : ").lower()
    print("\n" * 20)
    a_followers = account_a['follower_count']
    b_followers = account_b['follower_count']

    is_correct = check_answer(guess, a_followers, b_followers)

    if is_correct:
        score += 1
        print(f"You're Right! , Your current score : {score}")
    else:
        print(f"Sorry, You're Wrong! , Your final score : {score}")
        running = False
'''has_high_income = True
has_good_credit = False

if has_high_income and has_good_credit:
    print(f'It is a good ')
else:
    print('You are hired')

has_criminal_record = False
has_good_credit = True

if has_good_credit and not has_criminal_record:
    print("Credit")

secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess_number = int(input("Guess: "))
    guess_count += 1
    if guess_number == secret_number:
        print(f"You won, {guess_number} is the right one")
        break
else:
    print("Keep trying")'''

#


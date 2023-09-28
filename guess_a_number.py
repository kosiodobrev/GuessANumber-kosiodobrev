import random
computer_number = random.randint(1, 100)
playing = True
while playing:
    while True:
        player_number = input("Познай числото (1-100): ")
        if not player_number.isdigit():
            print("Невалиден вход. Опитай пак. Този път напиши число!")
            continue

        if int(player_number) == computer_number:
            print("Браво! Ти позна числото!")
            break
        elif int(player_number) > computer_number:
            print("По-надолу!")
        elif int(player_number) < computer_number:
            print("По-нагоре!")

    choose_input = input("Искаш ли да играеш пак? [д]/[н]")
    if choose_input == "д":
        continue
    else:
        print("Благодаря, че игра! Лек и успешен ден.")
        break
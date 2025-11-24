import random
def play_roulette():
    while True:
        print("Добро пожаловать в рулетку")
        print("Правила игры")
        print("Вы загадавываете число от 0 до 32")
        print("Крупье крутит рулетку, если числа совпадают - ВЫ ВЫИГРЫВАЕТЕ")



        try:
            player_number = int(input("\nЗагадайте ваше число от 0 до 32:"))
            if player_number < 0 or player_number > 32:
                print("Ошибка. Число должно быть от 0 до 32")
                continue

            print(f"\nВы загадали число: {player_number}")
            input("Нажмите Enter, чтобы совершить прокрут")

            roulette_number = random.randint(0,32)
            print(f"Выпало число {roulette_number}")

            if player_number == roulette_number:
                print("\nПоздравляю вы выиграли!")
            else:
                print(f"\n К сожалению вы не угадали.")
                print(f"\nВаше число {player_number}, а выпало {roulette_number}")

        except ValueError:
            print("Пожалуйста, введите корректное число")
            continue
        while True:
            play_again = input("\nХотите сыграть в рулетку еще раз? (да/нет): ")
            if play_again in ['да','yes']:
                print("\nОтлично! Давайте сыграем еще раз!")
                break
            elif play_again in ['нет', 'н', 'no', 'n']:
                print("\nСпасибо за игру в рулетку! Возвращаемся в главное меню.")
                return
            else:
                print("Пожалуйста, ответьте 'да' или 'нет'")


def play_poker():
    print("Добро пожаловать в покерный зал")
    print("К сожалению, покерный зал временно не работает")
    print("Но наши дилеры готовы сыграть с вами в рулетку!")
    play_again = input("\nХотите попробовать рулетку вместо покера ?(да/нет):")
    if play_again in ['да', 'yes']:
        play_roulette()

def play_slots():
    print("Добро пожаловать в игру Однорукий бандит")
    print("К сожалению, игровые автоматы временно не работает")
    print("Но наши дилеры готовы сыграть с вами в рулетку!")
    play_again = input("\nХотите попробовать рулетку вместо покера ?(да/нет):")
    if play_again in ['да', 'yes']:
        play_roulette()
def choose_game():
    print("Выберете Игру")
    print("1 - Рулетка")
    print("2 - Покер")
    print("3 - Однорукий бандит")


    while True:
        try:
            choice = input("\nВведите номер игры (1,2 или 3):")
            if choice == "1":
                play_roulette()
                break
            elif choice == "2":
                play_poker()
                break
            elif choice == "3":
                play_slots()
                break
            else:
                print("Неверный выбор! Пожалуйста , введите 1,2 или 3")

        except KeyboardInterrupt:
            print("\n\nИгра прервана.До свидания!")
def ask_to_play():

    print("'Добро пожаловать в наше казино! Хотите сыграть в азартные игры?'")
    while True:
        play_answer = input("\nХотите сыграть в игру? (да,нет):")
        if play_answer == "да":
            print("\nОтлтчно! Тогда предлагаю выбрать одно из наших игр!")
            return True
        elif play_answer == "нет":
            print("\nКак жаль!Мы всегда рады видеть вас в нашем казино!")
            return False
        else:
            print("Пожалуйста , ответьте 'да' или 'нет'" )
def main():

    print("   ДОБРО ПОЖАЛОВАТЬ В КАЗИНО!")





    while True:
        enter_answer = input("\nЖелаете ли вы войти в казино? (да/нет): ")

        if enter_answer in ['да','yes']:
            print("\n 'Отлично! Добро пожаловать в казино!'")
            print("'Проходите, наши игры ждут вас!'")
            break
        elif enter_answer in ['нет', 'no']:
            print("\n 'Как жаль! Надеемся увидеть вас снова!'")

            return
        else:
            print(" Пожалуйста, ответьте 'да' или 'нет'")


    print("\nВы проходите в главный зал казино.")


    wants_to_play = ask_to_play()


    if not wants_to_play:

        print("Возможно, в следующий раз вы решитесь сыграть!")
        return


    choose_game()

    # Завершение игры

    print("     СПАСИБО ЗА ВИЗИТ В КАЗИНО !")
    print("           Надеемся увидеть вас снова!")



if __name__ == "__main__":
    main()
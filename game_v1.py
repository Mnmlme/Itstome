"""Game guess number"""
import random 

def guess_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100. Попробуйте угадать его.")

    while True:
        user_input = input("Введите ваше предположение: ")

        # Проверка, что введено число
        if not user_input.isdigit():
            print("Пожалуйста, введите целое число.")
            continue

        guess = int(user_input)
        attempts += 1

        if guess < number_to_guess:
            print("Загаданное число больше.")
        elif guess > number_to_guess:
            print("Загаданное число меньше.")
        else:
            print(f"Поздравляем! Вы угадали число с {attempts} попытки.")
            break

if __name__ == "__main__":
    guess_number()


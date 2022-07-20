"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""

import numpy as np

def random_predict(number: int=1) -> int:
    """Рандомно угадываем число
    Args:
        number (int, optional): Загаданное число. Defaults to 1.
    Returns:
        int: Число попыток
    """
    # Количество попыток
    count = 0 

    # Минимальное значение диапазона поиска
    min_value = 1

    # Максимальное значение диапазона поиска
    max_value = 101
    while True:
        count+=1
        predict_number = np.random.randint(min_value,max_value)# Предполагаемое число 
        if number < predict_number:  # Условие корректировки максимальной границы
            max_value = predict_number
        elif number > predict_number: # Условие корректировки минимальной границы
            min_value = predict_number
        else:
            break # Выход из цикла если угадали 
    return (count)

def score_game(random_predict) -> int:
    """ За какое количество попыток в среднем за 1000 подходов угадыванет наш алгоритм
    Args:
        random_predict (_type_): функция угадывания
    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1) # Фиксируем сид для вопроизводимости
    random_array = np.random.randint(1,101, size=(1000)) # Загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number)) # Добавление в список количества попыток

    score = int(np.mean(count_ls)) #  Среднее значение количества попыток
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток.")
    return score


if __name__ == '__main__':
    # Запуск
    score_game(random_predict)  
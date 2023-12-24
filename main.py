import random

def create_array_manually():
    n = int(input("Введите размер массива: "))
    arr = []
    for i in range(n):
        value = int(input(f"Введите элемент {i + 1}: "))
        arr.append(value)
    return arr


def create_array_random():
    n = int(input("Введите размер массива: "))
    min_value = int(input("Минимальное значение: "))
    max_value = int(input("Максимальное значение: "))
    arr = [random.randint(min_value, max_value) for _ in range(n)]
    return arr
    
def gnome_sort(arr):
    index = 0
    while index < len(arr):
        if index == 0:
            index = 1
        if arr[index] >= arr[index - 1]:
            index += 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index -= 1
    return arr


while True:
    print("Выберите способ создания массива:")
    print("1. Вручную")
    print("2. С использованием случайных чисел")
    print("3. Выход")

    choice = input("Ваш выбор: ")

    if choice == '1':
        manual_array = create_array_manually()
        print("Созданный массив:", manual_array)
        if len(manual_array) == 1:
            print("Отсортированный массив:", manual_array)
        else:
            print("Отсортированный массив:", gnome_sort(manual_array))
    elif choice == '2':
        random_array = create_array_random()
        print("Созданный массив:", random_array)
        if len(random_array) == 1:
            print("Отсортированный массив:", random_array)
        else:
            print("Отсортированный массив:", gnome_sort(random_array))
    elif choice == '3':
        break
    else:
        print("Неверный выбор. Пожалуйста, выберите 1, 2 или 3.")

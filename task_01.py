import timeit
import random


# Алгоритм сортування злиттям (Merge Sort)
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Злиття двох половин
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Залишкові елементи лівої частини
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Залишкові елементи правої частини
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


# Алгоритм сортування вставками (Insertion Sort)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Переміщуємо елементи, що більше за key, на одну позицію вперед
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Використовуємо вбудовану функцію sorted(), яка реалізує Timsort
def timsort(arr):
    return sorted(arr)


# Функція для створення випадкового масиву
def generate_random_array(size):
    return [random.randint(0, 10000) for _ in range(size)]


# Функція для тестування часу виконання алгоритму
def measure_time(func, arr):
    # Копіюємо масив, щоб алгоритми працювали з однаковими даними
    arr_copy = arr.copy()
    timer = timeit.Timer(lambda: func(arr_copy))
    return timer.timeit(number=1)


# Генеруємо випадковий масив
array_size = 10000
random_array = generate_random_array(array_size)

# Вимірюємо час виконання для кожного алгоритму
merge_sort_time = measure_time(merge_sort, random_array)
insertion_sort_time = measure_time(insertion_sort, random_array)
timsort_time = measure_time(timsort, random_array)

# Результати:
print(f"Merge Sort :{merge_sort_time}")
print(f"Insertion Sort :{insertion_sort_time}")
print(f"Timsort :{timsort_time}")


"""Висновок:
Як показують результати, алгоритм Timsort є значно швидшим за сортування \n
злиттям та сортування вставками. Це пояснюється тим, що Timsort використовує \n
гібридний підхід, поєднуючи сортування вставками для малих підмножин\n
і сортування злиттям для великих масивів. Він є оптимізованим для реальних\n
даних і тому застосовується у вбудованих функціях сортування Python. \n
Сортування вставками працює повільніше на великих масивах,\n
оскільки має квадратичну складність. \n
​"""

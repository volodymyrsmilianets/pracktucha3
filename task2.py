import time

# Декоратор для вимірювання часу виконання функції
def timer_wrapper(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Початок вимірювання часу
        result = func(*args, **kwargs)  # Виклик оригінальної функції
        end_time = time.time()  # Кінець вимірювання часу
        print(f"Час виконання: {end_time - start_time:.4f} секунд")
        return result
    return wrapper

# Генератор простих чисел
def prime_number_generator():
    num = 2  # Початкове просте число
    while True:
        # Перевірка, чи є число простим
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
        num += 1

# Функція для отримання n простих чисел
@timer_wrapper
def prime_num_getter(n):
    prime_gen = prime_number_generator()
    primes = []
    for _ in range(n):
        primes.append(next(prime_gen))  # Отримуємо наступне просте число
    print(f"Перші {n} простих чисел: {primes}")

# Тестування:
prime_num_getter(10)  # Отримуємо перші 10 простих чисел

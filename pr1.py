def fibonacci_seq_generator():
    a, b = 0, 1  # Початкові числа послідовності Фібоначі
    while True:  # Безкінечний цикл
        yield a  # Повертаємо поточне число
        a, b = b, a + b  # Оновлюємо значення a і b для наступного числа

# Тести:
fib_gen = fibonacci_seq_generator()

# Викликаємо генератор кілька разів:
for _ in range(10):
    print(next(fib_gen))

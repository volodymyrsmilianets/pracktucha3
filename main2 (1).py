import time

def timer_wrapper(func):
    def wrapper(*args, **kwargs):
        start_time = time.time() 
        result = func(*args, **kwargs) 
        end_time = time.time() 
        print(f"Час виконання: {end_time - start_time:.4f} секунд")
        return result
    return wrapper

def prime_number_generator():
    num = 2
    while True:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
        num += 1

@timer_wrapper
def prime_num_getter(n):
    prime_gen = prime_number_generator()
    primes = []
    for _ in range(n):
        primes.append(next(prime_gen)) 
    print(f"Перші {n} простих чисел: {primes}")

prime_num_getter(10) 

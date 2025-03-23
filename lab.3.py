
greet_user = lambda name: print('Hello My Dear,', name)
user_name = input("What is your name? ")
greet_user(user_name)

tuples_list = [(3, 11), (1, 7), (7, 8), (16, 88), (23, 15), (5, 3), (9, 20)]
sorted_list = sorted(tuples_list, key=lambda x: x[1])
print("Lista sortată:", sorted_list)

square = lambda x: x ** 2
num = 5
print(f"Pătratul lui {num} este {square(num)}")

say_hello = lambda: print("Hello, world!")
say_hello()

add_numbers = lambda a, b: a + b
print("Suma lui 3 și 7 este:", add_numbers(3, 7))

default_greeting = lambda name="User": f"Hello, {name}!"
print(default_greeting())
print(default_greeting("Alice"))

multiply = lambda a, b: a * b
print("Produsul lui 4 și 6 este:", multiply(4, 6))

show_message = lambda msg: print("Mesajul tău este:", msg)
show_message("Acesta este un exemplu.")

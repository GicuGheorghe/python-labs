
# Aceasta este o funcție lambda care primește un nume și afișează un mesaj de salut.
# Funcția este apelată cu un nume introdus de utilizator.

greet_user = lambda name: print('Hello My Dear,', name)
user_name = input("What is your name? ")
greet_user(user_name)

# 2. Sortarea unei liste de tupluri după al doilea element
# Se creează o listă de tupluri și se sortează folosind o expresie lambda ca key.

tuples_list = [(3, 11), (1, 7), (7, 8), (16, 88), (23, 15), (5, 3), (9, 20)]
sorted_list = sorted(tuples_list, key=lambda x: x[1])
print("Lista sortată:", sorted_list)

# 3. Crearea propriei funcții-lambda
# Funcție lambda pentru calculul pătratului unui număr
square = lambda x: x ** 2
num = 5
print(f"Pătratul lui {num} este {square(num)}")

# 4. Definirea funcțiilor cu diferite tipuri de parametri
# a) Funcție fără parametri
say_hello = lambda: print("Hello, world!")
say_hello()

# b) Funcție cu parametri
add_numbers = lambda a, b: a + b
print("Suma lui 3 și 7 este:", add_numbers(3, 7))

# c) Funcție cu parametri predefiniți
default_greeting = lambda name="User": f"Hello, {name}!"
print(default_greeting())
print(default_greeting("Alice"))

# d) Funcție care returnează un rezultat
multiply = lambda a, b: a * b
print("Produsul lui 4 și 6 este:", multiply(4, 6))

# e) Funcție care nu returnează nimic, doar afișează
show_message = lambda msg: print("Mesajul tău este:", msg)
show_message("Acesta este un exemplu.")

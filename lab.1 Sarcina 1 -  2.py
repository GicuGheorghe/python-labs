# Sarcina 1

name = input("Introduceți numele dvs.: ")
print(f"Salut, {name}, Bine ai venit!" )


real_value = 3.14
short_text = "Laborator"
a = short_text
short_text = "kkokok"
print(a)
integer_value = 42
long_text = """Python este un limbaj de programare
 foarte popular și ușor de învățat.
 Se folosește în multe domenii, inclusiv AI
 și dezvoltare web."""

print(type(real_value))
print(type(integer_value))

print("Lungimea variabilei short_text:", len(short_text))

print("Textul transformat in litere mari:", long_text.upper())

substring = short_text[0:4]
print("Subsir extras din short_text:", substring)

print("Mesaj format cu metoda string_format : {} {} " .format(integer_value,real_value))
print(f"Mesaj format cu metoda f-string,Variabila real_value are valoarea {real_value}" )


# Sarcina 2

#a)
txt = "More results from text..."
substr = txt[4:12]
print(substr)
print(substr.strip()) 


#b)
txt = "More results from text..."
print(txt.split())



#c)
age = 36
txt = "My name is Mary, and I am {}"
print(txt.format(age))






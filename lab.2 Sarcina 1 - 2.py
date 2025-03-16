
my_list = [10, 20, 30, 40, 50]

# Afisarea primei si a treia valori
element1 = my_list[0]
element3 = my_list[2]
print(f"Prima valoare: {element1}, A treia valoare: {element3}")

# Inlocuirea unei valori\my_list[1] = 25  # Inlocuim 20 cu 25
print("Lista modificata:", my_list)

# Taietura (slicing) a listei
slice_list = my_list[1:4]
print("Taietura listei:", slice_list)

# Aplicarea unei metode, 2 functii si 3 operatori
my_list.append(60)  # Metoda append adauga un element la final
print("Lista dupa append:", my_list)

lungime = len(my_list)  # Functie len pentru lungime
suma = sum(my_list)  # Functie sum pentru suma elementelor
print(f"Lungimea listei: {lungime}, Suma elementelor: {suma}")

# Operatorii: +, *, in
lista_dublata = my_list * 2  # Multiplicarea listei
print("Lista dublata:", lista_dublata)

concatenare = my_list + [70, 80]  # Concatenarea a doua liste
print("Lista concatenata:", concatenare)

print("40 este in lista?", 40 in my_list)  # Operator "in" verifica daca un element e in lista

# Definirea unui tuplu
tuple_data = (5, 15, 25, 35, 45)
print("Tipul tuplului:", type(tuple_data))

# Afisarea primei si ultimei valori
tuple_first = tuple_data[0]
tuple_last = tuple_data[-1]
print(f"Prima valoare: {tuple_first}, Ultima valoare: {tuple_last}")

# Taietura (slicing) pe tuplu
tuple_slice = tuple_data[1:4]
print("Taietura tuplului:", tuple_slice)

# Aplicarea a 3 functii pe tuplu
lungime_tuple = len(tuple_data)
max_value = max(tuple_data)
min_value = min(tuple_data)
print(f"Lungime: {lungime_tuple}, Max: {max_value}, Min: {min_value}")

# Definirea unui set (multime) cu valori duplicate
my_set = {1, 2, 2, 3, 4, 4, 5}
print("Setul definit:", my_set)  # Valorile duplicate sunt eliminate

# Aplicarea unei metode si a unei functii pe set
my_set.add(6)  # Metoda add adauga un element
print("Setul dupa adaugare:", my_set)

set_length = len(my_set)  # Functie len pentru lungimea setului
print("Lungimea setului:", set_length)

# Crearea unui dictionar cu chei textuale si numerice
dict_text = {"nume": "Alex", "varsta": 25, "oras": "Bucuresti"}
dict_num = {1: "unu", 2: "doi", 3: "trei"}

# Accesarea elementelor din dictionar
print("Nume:", dict_text["nume"])
print("Cifra 2 corespunde cu:", dict_num[2])

# Aplicarea a 2 metode si 2 functii pe dictionar
valori = dict_text.values()  # Metoda values
print("Valorile dictionarului text:", valori)

chei = dict_num.keys()  # Metoda keys
print("Cheile dictionarului numeric:", chei)

lungime_dict = len(dict_text)  # Functie len pentru lungime
print("Lungimea dictionarului text:", lungime_dict)

eliminare = dict_text.pop("oras")  # Functie pop pentru eliminare
print("Dictionar dupa pop:", dict_text)

# Conversia unui tip de date
list_to_tuple = tuple(my_list)  # Convertim lista in tuplu
print("Lista convertita in tuplu:", list_to_tuple)

set_to_list = list(my_set)  # Convertim setul in lista
print("Set convertit in lista:", set_to_list)



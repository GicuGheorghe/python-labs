
my_list = [10, 20, 30, 40, 50]


element1 = my_list[0]
element3 = my_list[2]
print(f"Prima valoare: {element1}, A treia valoare: {element3}")


print("Lista modificata:", my_list)


slice_list = my_list[1:4]
print("Taietura listei:", slice_list)


my_list.append(60)  
print("Lista dupa append:", my_list)

lungime = len(my_list) 
suma = sum(my_list) 
print(f"Lungimea listei: {lungime}, Suma elementelor: {suma}")


lista_dublata = my_list * 2 
print("Lista dublata:", lista_dublata)

concatenare = my_list + [70, 80] 
print("Lista concatenata:", concatenare)

print("40 este in lista?", 40 in my_list)  


tuple_data = (5, 15, 25, 35, 45)
print("Tipul tuplului:", type(tuple_data))


tuple_first = tuple_data[0]
tuple_last = tuple_data[-1]
print(f"Prima valoare: {tuple_first}, Ultima valoare: {tuple_last}")


tuple_slice = tuple_data[1:4]
print("Taietura tuplului:", tuple_slice)


lungime_tuple = len(tuple_data)
max_value = max(tuple_data)
min_value = min(tuple_data)
print(f"Lungime: {lungime_tuple}, Max: {max_value}, Min: {min_value}")


my_set = {1, 2, 2, 3, 4, 4, 5}
print("Setul definit:", my_set)  


my_set.add(6)  
print("Setul dupa adaugare:", my_set)

set_length = len(my_set)  
print("Lungimea setului:", set_length)


dict_text = {"nume": "Alex", "varsta": 25, "oras": "Bucuresti"}
dict_num = {1: "unu", 2: "doi", 3: "trei"}


print("Nume:", dict_text["nume"])
print("Cifra 2 corespunde cu:", dict_num[2])


valori = dict_text.values()  
print("Valorile dictionarului text:", valori)

chei = dict_num.keys()  
print("Cheile dictionarului numeric:", chei)

lungime_dict = len(dict_text)  
print("Lungimea dictionarului text:", lungime_dict)

eliminare = dict_text.pop("oras")  
print("Dictionar dupa pop:", dict_text)


list_to_tuple = tuple(my_list)  
print("Lista convertita in tuplu:", list_to_tuple)

set_to_list = list(my_set)  
print("Set convertit in lista:", set_to_list)



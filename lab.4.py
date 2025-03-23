def calculate_ideal_weight(height, age, sex, weight):
    if sex == 'M':
        ideal_weight = height - 100 - ((height - 150) / 4 + (age - 20) / 4)
    else:  # sex == 'F'
        ideal_weight = height - 100 - ((height - 150) / 2.5 + (age - 20) / 6)
    
    difference = weight - ideal_weight
    recommendation = "Trebuie să slăbești." if difference > 0 else "Trebuie să iei în greutate."
    return ideal_weight, recommendation

def get_valid_input(prompt, min_val, max_val):
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Valoare invalidă! Trebuie să fie între {min_val} și {max_val}.")
        except ValueError:
            print("Introdu o valoare numerică validă!")

def get_valid_sex():
    while True:
        sex = input("Introduceți sexul (M/F): ").strip().upper()
        if sex in ('M', 'F'):
            return sex
        else:
            print("Introduceți doar M sau F!")

def get_cat_age_human_equivalent():
    young_cat_mapping = {
        1: "6 luni", 2: "10 luni", 3: "2 ani", 4: "5 ani", 5: "8 ani", 6: "14 ani", 
        7: "15 ani", 8: "16 ani", 10: "17 ani", 11: "17 ani"
    }
    
    is_kitten = input("Pisica este mai mică de un an? (Da/Nu): ").strip().lower()
    
    if is_kitten in ('da', 'yes'):
        while True:
            try:
                months = int(input("Câte luni are pisicul? (1-11): "))
                if 1 <= months <= 11:
                    return young_cat_mapping.get(months, "Valoare necunoscută")
                else:
                    print("Introduceți un număr între 1 și 11.")
            except ValueError:
                print("Introduceți un număr valid!")
    else:
        while True:
            try:
                years = int(input("Câți ani are pisicul? (1-35): "))
                if 1 <= years < 35:
                    if years == 1:
                        return "18 ani"
                    elif years == 2:
                        return "25 ani"
                    elif 3 <= years <= 15:
                        return f"{25 + (years - 2) * 4} ani"
                    else:
                        return f"{77 + (years - 15) * 3} ani"
                else:
                    print("Introduceți un număr între 1 și 34.")
            except ValueError:
                print("Introduceți un număr valid!")

def main():
    print("--- Calculator Greutate Ideală ---")
    height = get_valid_input("Introduceți înălțimea (150-220 cm): ", 150, 220)
    age = get_valid_input("Introduceți vârsta (20-120 ani): ", 20, 120)
    sex = get_valid_sex()
    weight = get_valid_input("Introduceți greutatea (45-300 kg): ", 45, 300)
    
    ideal_weight, recommendation = calculate_ideal_weight(height, age, sex, weight)
    print(f"Greutatea ideală: {ideal_weight:.2f} kg. {recommendation}")
    
    print("\n--- Calculator Vârstă Pisică ---")
    cat_human_age = get_cat_age_human_equivalent()
    print(f"Vârsta pisicii în ani omenești: {cat_human_age}")
    
if __name__ == "__main__":
    main()

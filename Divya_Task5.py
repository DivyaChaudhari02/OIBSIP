import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    # Alag-alag character sets taiyar karna
    character_pool = ""
    
    if use_letters:
        character_pool += string.ascii_letters  # a-z aur A-Z dono add honge
    if use_numbers:
        character_pool += string.digits         # 0-9 add honge
    if use_symbols:
        character_pool += string.punctuation    # Special characters (!, @, #, etc.) add honge

    # Agar user ne sabhi options mana kar diye ho
    if not character_pool:
        print("\n[Error] Kripya password mein kam se kam ek character type zaroor select karein!")
        return None

    # Random characters select karke password banana
    password = "".join(random.choice(character_pool) for _ in range(length))
    return password

def main():
    print("-" * 50)
    print("      Oasis Infobyte: Random Password Generator      ")
    print("-" * 50)

    try:
        # User se password ki length poochna
        length = int(input("Aapko kitne lambai (length) ka password chahiye? (Eg. 8, 12, 16): "))
        
        if length <= 0:
            print("\n[Error] Password ki lambai 0 se badi honi chahiye!")
            return

        # User se preferences poochna (Yes/No)
        print("\n--- Password Customization ---")
        include_letters = input("Kya password mein Letters (A-Z, a-z) chahiye? (y/n): ").strip().lower() == 'y'
        include_numbers = input("Kya password mein Numbers (0-9) chahiye? (y/n): ").strip().lower() == 'y'
        include_symbols = input("Kya password mein Special Symbols (!, @, #) chahiye? (y/n): ").strip().lower() == 'y'

        # Password generate karna
        generated_pass = generate_password(length, include_letters, include_numbers, include_symbols)

        if generated_pass:
            print("\n" + "=" * 40)
            print(f" Aapka Strong Password Yeh Hai: {generated_pass}")
            print("=" * 40)
            print("Tip: Is password ko safe jagah copy kar ke rakh lein.")

    except ValueError:
        print("\n[Error] Kripya sahi number enter karein (jaise 8, 12, 14)!")

if __name__ == "__main__":
    main()
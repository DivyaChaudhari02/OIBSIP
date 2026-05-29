def calculate_bmi(weight, height):
    try:
        bmi = weight / (height ** 2)
        return round(bmi, 2)
    except ZeroDivisionError:
        return None

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight (Kam vajan)"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight (Swaasth vajan)"
    elif 25.0 <= bmi < 29.9:
        return "Overweight (Vajan jyaada hai)"
    else:
        return "Obese (Motaapa)"

def main():
    print("-" * 40)
    print("      Oasis Infobyte: BMI Calculator     ")
    print("-" * 40)
    
    try:
        weight = float(input("Apna vajan (Weight) Kilograms (kg) me dalein: "))
        height_cm = float(input("Apni lambai (Height) Centimeters (cm) me dalein: "))
        
        height_m = height_cm / 100
        
        if weight <= 0 or height_cm <= 0:
            print("[Error] Weight aur Height hamesha 0 se badi honi chahiye!")
            return

        bmi_value = calculate_bmi(weight, height_m)
        
        if bmi_value is not None:
            category = get_bmi_category(bmi_value)
            
            print("\n" + "="*30)
            print(f"Aapka BMI hai: {bmi_value}")
            print(f"Aapka Status: {category}")
            print("="*30)
        else:
            print("Kuch galat hua! Kripya sahi values enter karein.")
            
    except ValueError:
        print("[Error] Kripya sirf numbers hi enter karein (jaise 65 ya 165)!")

if __name__ == "__main__":
    main()
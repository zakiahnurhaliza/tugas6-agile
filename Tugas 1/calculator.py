# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

if __name__ == "__main__":
    print("Kalkulator Sederhana")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    choice = input("Pilih operasi (1/2/3/4): ")
    num1 = float(input("Masukkan angka pertama: "))
    num2 = float(input("Masukkan angka kedua: "))

    if choice == '1':
        print(f"Hasil: {add(num1, num2)}")
    elif choice == '2':
        print(f"Hasil: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"Hasil: {multiply(num1, num2)}")
    elif choice == '4':
        try:
            print(f"Hasil: {divide(num1, num2)}")
        except ValueError as e:
            print(e)
    else:
        print("Pilihan tidak valid.")
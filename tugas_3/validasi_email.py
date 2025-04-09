import re

def validasi_email(email):
    # Pola regex untuk memvalidasi email
    pola = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(pola, email):
        return True
    else:
        return False

# Program utama
if __name__ == "__main__":
    email = input("Masukkan alamat email: ")
    
    if validasi_email(email):
        print("Email valid ✅")
    else:
        print("Email tidak valid ❌")

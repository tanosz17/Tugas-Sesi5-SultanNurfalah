#Sultan Nurfalah
#TI23H

class Autentikasi:
    def login(self):
        pass

class EmailPasswordAuth(Autentikasi):
    def login(self):
        print("Login menggunakan email dan kata sandi.")

class GoogleAuth(Autentikasi):
    def login(self):
        print("Login menggunakan akun Google.")

class SidikJariAuth(Autentikasi):
    def login(self):
        print("Login menggunakan autentikasi sidik jari.")

# polymorphism
def proses_login(autentikasi):
    autentikasi.login()

# penggunaan
email_login = EmailPasswordAuth()
google_login = GoogleAuth()
sidikjari_login = SidikJariAuth()

for metode in [email_login, google_login, sidikjari_login]:
    proses_login(metode)

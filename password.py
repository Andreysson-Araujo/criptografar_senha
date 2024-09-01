from cryptography.fernet import Fernet

secret_key = Fernet.generate_key()
fernet=Fernet(secret_key)


def criptG(password):
    return fernet.encrypt(password.encode()).decode()

def descriptografa(password_noview):
    return fernet.decrypt(password_noview.encode()).decode()

original_password = input('Digite sua senha : ')
password_noview = criptG(original_password)
password_view = descriptografa(password_noview)

print(f'Senha original:{original_password}')
print(f'Senha criptografada: {password_noview}')


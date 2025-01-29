import random

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"
kol = int(input("Сколько паролей придумать? "))
dlina = int(input("Какая будет длина пароля? "))
dig = input("Включать ли цифры в пароль? (Y - да, N - нет) ")
propis = input("Включать ли прописные буквы в пароль? (Y - да, N - нет) ")
stroch = input("Включать ли строчные буквы в пароль? (Y - да, N - нет) ")
symb = input("Включать ли символы в пароль? (Y - да, N - нет) ")
chars = ''
if dig == 'Y':
    chars += digits
if propis == 'Y':
    chars += lowercase_letters
if stroch == 'Y':
    chars += uppercase_letters
if symb == 'Y':
    chars += punctuation
def gen_pass (dlina, chars):
    password = ''
    passwords = ''
    for i in range(kol):
        password = ''
        for j in range(dlina):
            password += chars[random.randrange(len(chars))]
        passwords += password + ' '
    return passwords
print(gen_pass (dlina, chars))
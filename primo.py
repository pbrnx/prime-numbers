import math
import os
import time

def primo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


while True:



    num = int(input("Digite um número: "))
    if primo(num):
        print(f"{num} é um número primo.")
    else:
        print(f"{num} NÃO é um número primo.")
    input("Pressione Enter para inserir um novo número...")

    os.system('cls')
    
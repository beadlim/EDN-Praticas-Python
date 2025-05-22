# Prática 3

# 1 - Calculadora com tratamento de erros

while True:
    try:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida: digite apenas números.\n")
        continue

    op = input("Digite a operação (+, -, *, /): ").strip()

    if op not in {"+", "-", "*", "/"}:
        print("Operação inválida. Tente novamente.\n")
        continue

    try:
        if op == "+":
            resultado = a + b
        elif op == "-":
            resultado = a - b
        elif op == "*":
            resultado = a * b
        elif op == "/":
            resultado = a / b      
    except ZeroDivisionError:
        print("Erro: divisão por zero não é permitida.\n")
        continue

    print(f"✅ Resultado: {a} {op} {b} = {resultado}")
    break  

# 2 - Calculadora de Média com tratamento de erros

notas = []

while True:
    entrada = input("Digite a nota (0‑10) ou 'fim' para encerrar: ").strip().lower()

    if entrada == "fim":
        break

    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota fora do intervalo 0‑10. Ignorada.")
    except ValueError:
        print("Entrada inválida. Digite um número ou 'fim'.")

if notas:
    media = sum(notas) / len(notas)
    print(f"\nMédia da turma: {media:.2f} (com {len(notas)} notas válidas)")
else:
    print("\nNenhuma nota válida foi registrada.")

# 3 - Verificador de senha

while True:
    senha = input("Digite uma senha (mín. 8 caracteres e 1 número) ou 'sair': ")

    if senha.lower() == "sair":
        print("Encerrado pelo usuário.")
        break

    possui_numero = any(ch.isdigit() for ch in senha)
    if len(senha) >= 8 and possui_numero:
        print("Senha forte!")
        break
    else:
        print("Senha fraca. Tente novamente.\n")
    
# 4 - Par ou ímpar até ‘fim’

pares = impares = 0

while True:
    entrada = input("Digite um número inteiro ou 'fim': ").strip().lower()

    if entrada == "fim":
        break

    try:
        n = int(entrada)
        if n % 2 == 0:
            print(f"{n} é par.")
            pares += 1
        else:
            print(f"{n} é ímpar.")
            impares += 1
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.\n")

print(f"\nTotais — pares: {pares} | ímpares: {impares}")





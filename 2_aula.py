# #num1 = 5.5
# num2 = 7.9
# print(num1 + num2)
# print(type(num1))
# print(type(num2))

# #pi = 3.1415
# print(f"O numero pi com duas casas decimais é {pi:.2f}.")

d = True
e = False
print(type(e))
print(type(d))

# #nota = 8
# media = 7
# aprovado = nota >= media
# print(aprovado)

media_final = float(input("Media final da disciplina de 0 a 10 = "))
frequencia = int(input("frequencia da disciplina em porcentagem ="))

if media_final >= 6 and frequencia >= 75:
print("Aprovado!")
else:
print("Reprovado!")


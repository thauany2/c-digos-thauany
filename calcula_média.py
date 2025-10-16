nota_ana = float(input("qual é a sua nota bimestral ana ? :"))
nota_guilherme = float(input("qual é a sua nota bimestral guilherme ? :"))
nota_vitoria = float(input("qual é a sua nota bimestral vitoria ? :"))
nota_luisa = float(input("qual é a sua nota bimestral luisa ? :"))

soma = nota_ana + nota_guilherme + nota_vitoria + nota_luisa
media = soma/4


if media >=7.0:
    print("Aprovado ✅")
elif media >=5.0 and media <=7.0:
    print("Recuperação 🚨")
else:
    print("reprovado ❌ ")

print(f" A média escolar é {media}")

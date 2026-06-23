print("===== MEDIA DE NOTAS =====")

Aluno = input("Digite o nome do aluno: ")
nota1 = int(input("Digite primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print("A media de {} é: {:.1f}".format(Aluno, media))
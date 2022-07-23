# nome = (input("Digite o nome: "))
# idade = int(input("Digite a idade: "))
# if idade>=65:
#   print("O paciente " + nome + " POSSUI atendimento prioritário! ")
# else:
#   print("O paciente " + nome + " NÃO possui atendimento prioritário")
# print("FIM")


nome = (input("Digite o nome: "))
idade = int(input("Digite a idade: "))
doenca_infectocontagiosa = (
    input("Suspeita de doença infectocontagiosa? ")).upper()
if idade >= 65:
    print("O paciente " + nome + " POSSUI atendimento prioritário! ")
elif doenca_infectocontagiosa == "SIM":
    print("O paciente " + nome +
          " dave ser atendido na sala de espera reservada.")
else:
    print("O paciente " + nome + " NÃO possui atendimento prioritário")
print("FIM")

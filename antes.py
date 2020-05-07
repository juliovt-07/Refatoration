def verificacaoLonga():
    minhaIdade = int(input("Sua Idade: "))
    idade = minhaIdade
    obrigatorio1 = True
    obrigatorio2 = True
    if idade < 18:
        obrigatorio1 = False 
    if idade > 69:
        obrigatorio2 = False
    if obrigatorio1 == False or obrigatorio2 == False:
        return False
    if obrigatorio1 == True and obrigatorio2 == True:
        return True         
if verificacaoLonga() == False:
    print("Seu Voto não é obrigatório!")
else:
    print("Seu Voto é obrigatório")

#função refatorada
def verificacaoVoto():
    minhaIdade = int(input("Sua Idade: "))
    idade = minhaIdade
    if idade < 18 or idade > 69:
        return False
    else:
        return True
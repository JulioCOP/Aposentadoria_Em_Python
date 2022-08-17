#Programa que lê nome, ano de nascimento, carteira de trabalho e o sexo da pessoa, para em seguida e cadastra-lo
# em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário
#receberá também o ano de contratação e o salário. Adjacente a isso, o programa calcula, além da idade,
#com quantos anos a pessoa vai se aposentar. Se o usuário informar que é uma mulher, é calculado o tempo de contribuição
#uma mulher deve ter para se aprosentar. O mesmo ocorre se for um homem, mas com seu respectivo tempo de contribuição

###  DICIONARIO VARIAVÉL  ###
#idade de aposentadoria= (idade + ano contratado + tempo de contribuição) - ano atual

from datetime import datetime
dados=dict()

dados['NOME']=str(input("NOME: "))
ano_nasc= int(input("ANO DE NASCIMENTO: "))
dados['IDADE']=datetime.now().year - ano_nasc
dados['CTPS']=int(input("Nº CATEIRA DE TRABALHO: "))
dados['SEXO']=str(input("[MASCULINO] / [FEMININO]")).strip().upper()[0]
if dados['CTPS']==0:
    for i, k in dados.items():
        print(f"{i} TEM VALOR DE {k}")
    print(f"{dados['NOME']} NÃO TEM CARTEIRA DE TRABALHO")
else:
    if dados['SEXO']=='M':
        dados['ANO CONTRATRAÇÃO']=int(input(f"ANO EM QUE {dados['NOME']} FOI CONTRATADO: "))
        dados['SALARIO']=float(input("SALARIO R$: "))
        dados['APOSENTADORIA']=(dados['IDADE']+ dados['ANO CONTRATRAÇÃO']+35) - datetime.now().year
        for i, k in dados.items():
            print(f"{i} TEM VALOR DE {k}")
    if dados['SEXO']=='F':
        dados['ANO CONTRATRAÇÃO']=int(input(f"O ANO EM QUE {dados['NOME']} FOI CONTRATADO: "))
        dados['SALARIO']=float(input("SALARIO R$: "))
        dados['APOSENTADORIA']=(dados['IDADE']+dados['ANO CONTRATRAÇÃO']+30)- datetime.now().year
        for i, k in dados.items():
            print(f"{i} TEM VALOR DE {k}")
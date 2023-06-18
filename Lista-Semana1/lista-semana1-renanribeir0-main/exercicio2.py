#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui
def cumulativo(lista):
    soma_cumulativa = 0
    lista_cumulativa = []
    
    for num in lista:
        soma_cumulativa += num
        lista_cumulativa.append(soma_cumulativa)
    
    return lista_cumulativa







# Teste a sua função aqui (caso ache necessário)












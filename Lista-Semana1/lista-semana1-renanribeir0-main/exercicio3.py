#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui
def soma_dos_aninhados(lista):
    soma_total = 0
    
    for sublistas in lista:
        for num in sublistas:
            soma_total += num
    
    return soma_total







# Teste a sua função aqui (caso ache necessário)












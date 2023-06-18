#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui
def is_anagram(str1, str2):
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")
    
    return sorted(str1) == sorted(str2)







# Teste a sua função aqui (caso ache necessário)












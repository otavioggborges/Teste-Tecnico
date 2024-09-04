# 5) Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada
#  de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;


### Utilizando as informações propostas foi feita a seguinte solução: ###


def inverter_string(string):
    # Se a string for vazia ou de comprimento 1, retorna a string
    if len(string) == 0:
        return string
    else:
        # Faz a recursão e adiciona o primeiro caractere ao final
        return inverter_string(string[1:]) + string[0]

string = "TargetSistemas"
string_invertida = inverter_string(string)
print(string_invertida)
# 1) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
# Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
# Imprimir(SOMA);
# Ao final do processamento, qual será o valor da variável SOMA?


### Utilizando as informações propostas foi feita a seguinte solução: ###

Indice = 13
Soma = 0
K = 0
while K < Indice:
    K = K + 1
    Soma = Soma + K
print(Soma)

# O resultado final é 91.
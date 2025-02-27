"""5) Escreva um programa que inverta os caracteres de um string. IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou
pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;"""

def inverter_string(string):
    inverted_string = ''
    for char in string:
        inverted_string = char + inverted_string
    return inverted_string

original_string = input('Digite uma string para inverter seus caracteres: ')
inverted_string = inverter_string(original_string)

print(f'A string invertida é: {inverted_string}')

#output exemple for "hello": A string invertida é: olleh

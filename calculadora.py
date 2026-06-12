def main(): # define a função main, que é a função que executa o progama 
    print('CALCULADORA DO JONATHAN')
    
    num1=int(input('Digite um numero: '))
    num2=int(input('Digite outro numero: '))

# estou pedindo para o python ler um numero inteiro e armazenar na memoria, e depois ler outro numero inteiro e armazenar para depois somar, subtrair, multiplicar ou dividir.
    

    print('1- soma')
    print('2- subtração')
    print('3- multiplicação')
    print('4- divisão')
    print('5- sair')

    # dei opçoes para o usuario escolher qual operação fazer usando o print, e depois armazenando a escolha na memoria para depois usar o if

    escolha = int(input('Escolha a operação que deseja realizar: '))

    if escolha == 1:  # se a escolha for 1, ele vai executar o bloco de codigo abaixo por causa do if
        print('A soma é: ', num1 + num2)
    elif escolha == 2: # se a escolha for 2, ele vai executar o bloco de codigo abaixo por causa do elif
        print('A subtração é: ', num1 - num2)
    elif escolha == 3: 
        print('A multiplicação é: ', num1 * num2) # * é o simbolo de multiplicação
    elif escolha == 4:
        print('A divisão é: ', num1 / num2) # / é o simbolo de divisão
    elif escolha == 5:
        print('THANKS GUYS')


main() # executa a função main para iniciar o progama
   
    


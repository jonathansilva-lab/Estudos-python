def main(): # criei uma função junto ao comando 'main()' para organizar o codigo
    print("CALCULADORA DO JONATHAN") # pedi pro python exibir o nome da minha calculadora

    while True: # iniciei um loop para voltar para o menu sempre depois que finalizar o calculo
        print("\n1- Soma")
        print("2- Subtração")
        print("3- Multiplicação")
        print("4- Divisão")
        print("5- Potência")
        print("6- Sair")

        escolha = int(input("Escolha uma opção: ")) # criei uma variavel com um tipo primitivo 'int'  que vai executar uma entrada via 'input' 

        if escolha == 6: # criei um comando 'if' junto com um variavel e 'break(finaliza o loop)' para se escolher '6' sair
            print("Thanks guys")
            break

        if escolha < 1 or escolha > 6: # iniciei um comando para o usuario escolher de 1 a 6 no meu menu, se a escolha for menor que 1 e maior que 6 o print vai exibir:
            print("Opção inválida!")
            continue

        num1 = int(input("Digite um número: ")) # dei opções para o usuario digitar um numero do tipo primitivo 'inteiro' para calcular
        num2 = int(input("Digite outro número: "))

        if escolha == 1:
            print("Resultado:", num1 + num2) # criei um comando para executar a conta 'se isso for verdadeiro execute' com if

        elif escolha == 2: # criei um comando com ' senão, se issofor verdadeiro' com o elif para criar varias opções
            print("Resultado:", num1 - num2)

        elif escolha == 3:
            print("Resultado:", num1 * num2)

        elif escolha == 4:
            print("Resultado:", num1 / num2)

        elif escolha == 5:
            print("Resultado:", num1 ** num2)


main() # rodei o progama fechando com o 'main()'

    

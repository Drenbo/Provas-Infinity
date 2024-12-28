while True:
    print('Olá usuário, bem vindo a sua calculadora!')
    print('Menu:\n 1. Soma\n 2. Subtração\n 3. Multiplicação\n 4. Divisão\n 5. Sair')
    resposta = int(input('Qual opção deseja usar? '))
    
    def somar(x, y):
        soma = x + y
        return soma
    def subtrair(x, y):
        subtracao = x - y
        return subtracao
    def multiplicar(x, y):
        multiplicacao = x * y
        return multiplicacao
    def dividir(x, y):
        if y == 0:
            print('O divisor deve ser maior de zero.\n')
            y = int(input('Digite um novo divisor: '))
            divisao = x / y
        return divisao
    
    if resposta == 1:
        x = int(input('Qual o primeiro valor da soma? '))
        y = int(input('E qual o segundo? '))
        print(f'O resultado é = {somar(x, y)}\n')
        
    elif resposta == 2:
        x = int(input('Qual o primeiro valor da subtração? '))
        y = int(input('E qual o segundo? '))
        print(f'O resultado é = {subtrair(x, y)}\n')
        
    elif resposta == 3:
        x = int(input('Qual o primeiro valor da multiplicação? '))
        y = int(input('E qual o segundo? '))
        print(f'O resultado é = {multiplicar(x, y)}\n') 
         
    elif resposta == 4:
        x = int(input('Qual o primeiro valor da divisão? '))
        y = int(input('E qual o segundo? '))
        print(f'O resultado é = {dividir(x, y)}\n')
        
    elif resposta == 5:
        print('Certo, até mais!')
        break
        
    else:
        print('Digite uma opção válida\n')
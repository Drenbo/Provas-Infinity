print('Olá usuário, tudo bem? Seja bem vindo ao Manipulador de textos\nVamos começar digitando seu texto:')
texto = input('--> ')

while True:
    print(f'\n-- {texto} --')
    print('Menu:\n 1. Contar Palavras\n 2. Contar Letras\n 3. Inverter Texto\n 4. Substituir Palavra-Chave\n 5. Sair')
    escolha = int(input('O que deseja fazer no texto? '))
    
    def contar_Palavras(x):
        palavras = x.split()
        quantidade = len(palavras)
        return quantidade
    
    def contar_Letras(x):
        quantidade = 0
        for i in x:
            if i != ' ':
                quantidade += 1
        return quantidade
    
    def inverter_Texto(x):
        inverso = x[::-1]
        return inverso
    
    def substituir_Palavra(texto, palavra_antiga, palavra_nova):
        return texto.replace(palavra_antiga, palavra_nova)
    
    if escolha == 1:
        print(f'Seu texto tem {contar_Palavras(texto)} palavras.')   
    elif escolha == 2:
        print(f'Seu texto tem {contar_Letras(texto)} letras.')     
    elif escolha == 3:
        print(f'\nO seu texto invertido ficaria:\n- {inverter_Texto(texto)}')    
    elif escolha == 4:
        palavra_antiga = input('Qual a palavra você quer remover? ')
        palavra_nova = input('E a palavra para substituir? ')
        texto = substituir_Palavra(texto, palavra_antiga, palavra_nova)
        print(f'O seu texto ficou assim:\n- {texto}')
    elif escolha == 5: 
        print('Vida longa e próspera! 🖖')
        break
    else:
        print('A opção escolhida está inválida, vamos tentar de novo.')

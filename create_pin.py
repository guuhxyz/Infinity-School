# Criar um pin
while True:
    pin = input('Cadastre um PIN: ')
    if len(pin) != 4:
        print('O PIN deve ter somente 4 caracteres')
    else:
        print('Seu PIN foi cadastrado com sucesso!')
        break

tentativas = 3

while True:
    senha = input("Digite seu PIN para desbloquear seu celular: ")
    if senha == pin:
        print("PIN correto")
        break
    else:
        tentativas -= 1
        print(f'PIN incorreto, você tem mais {tentativas} tentativas: ')
        if tentativas < 1:
            print("PIN bloqueado")
            break

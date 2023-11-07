# Projeto pedra papel tesoura
import random

def vencendor(choice_user, choice_pc):
    if choice_user == choice_pc:
        return "Empate"
    elif (choice_user == 'pedra' and choice_pc == 'tesoura') or \
    (choice_user == 'papel' and choice_pc == 'pedra') or \
    (choice_user == 'tesoura' and choice_pc == 'papel'):
        return "Você venceu!!"
    else:
        return "O computador venceu."

def jogar():
    win_user = 0
    win_pc = 0
    empate = 0
    while True:
        escolha_user = input("Escolha pedra, papel ou tesoura: ").lower()
        if escolha_user not in ['pedra', 'papel', 'tesoura']:
            print("Opção inválida, tente novamente")
            continue
        escolha_pc = random.choice(['pedra', 'papel', 'tesoura'])
        resultado = vencendor(escolha_user, escolha_pc)
        print(f"Escolha do usuário: {escolha_user}")
        print(f"Escolha do computador: {escolha_pc}")
        print(resultado)
        if resultado == "Você venceu!!":
            win_user += 1
        elif resultado == "Empate":
            empate += 1
        else:
            win_pc += 1
        while True:
            play_again = input("Jogar novamente? ('S' para sim/'N' para não) ").lower()
            if play_again == 's':
                break
            elif play_again == 'n':
                print(f"Vezes que o usário ganhou: {win_user}")
                print(f"Vezes que o computador ganhou: {win_pc}")
                print(f"Empates: {empate}")
                return
            else:
                print("Opção não encontrada.")

print("Bem-vindo ao jogo de Pedra, Papel e Tesoura!")
jogar()
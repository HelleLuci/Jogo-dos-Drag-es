# PROJETO: O Despertar dos Dragões
# AUTORA: Futura Tecnóloga em ADS (Unopar) 
# OBJETIVO: Jogo de escolhas baseado em texto utilizando manipulação de strings
# ==================================

def jogar_despertar_dos_dragoes():
    print("--- Bem-vindo ao Totem ---")
    
    while True:
        # Captura a cor, remove espaços (.strip) e padroniza a primeira letra (.capitalize)
        cor_escolhida = input("\n🟡 Escolha uma cor para libertar o Dragão (Vermelho, Azul, Amarelo ou 'Sair'): ").strip().capitalize()

        # Condição de saída do jogo
        if cor_escolhida == "Sair":
            print("\nVocê se despede do totem. Os dragões voltam a descansar em suas caixas...")
            break

        # O cérebro do programa decide qual dragão mostrar com base na cor
        if cor_escolhida == "Vermelho":
            print("\n🔥 Você libertou o Dragão Severino!")
            print("✨ Sensação: Suas escamas são feitas de medalhas de alumínio antigas e ele tem cheiro de carvão doce.")

        elif cor_escolhida == "Azul":
            print("\n💧 Você libertou o Dragão da Compadecida!")
            print("✨ Sensação: Ele é suave como uma aquarela, traz paz aos ouvidos e a pele fica fresca a 28 graus.")

        elif cor_escolhida == "Amarelo":
            print("\n🍂 Você libertou o Dragão do Pôr do Sol!")
            print("✨ Sensação: O som ao redor vira vento nas árvores e você sente o estalar de folhas secas ao tocá-lo.")

        else:
            print("\n❌ Essa cor não abre nenhuma caixa.")
            print("💡 Dica: Tente uma das cores primárias que você usava nos palitinhos de picolé!")

# Inicialização segura do jogo
if __name__ == "__main__":
    jogar_despertar_dos_dragoes()

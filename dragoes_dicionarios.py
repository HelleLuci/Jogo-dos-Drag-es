# PROJETO: O Despertar dos Dragões (Edição Exposição do Ateliê)
# AUTORA: Futura Tecnóloga em ADS (Unopar) 
# =====================================================================

def jogar_despertar_dos_dragoes():
    print("--- 🏛️ Bem-vinda à Exposição Interativa do Ateliê 🏛️ ---")

    # O Dicionário agora funciona como o catálogo oficial da galeria de arte
    dragoes = {
        "Vermelho": {
            "nome": "Severino",
            "material": "Metal fundido e Carvão Vegetal",
            "status": "Disponível para venda",
            "sensacao": "Suas escamas são feitas de medalhas de alumínio antigas e ele tem cheiro de carvão doce."
        },
        "Azul": {
            "nome": "da Compadecida",
            "material": "Aquarela sobre Porcelana Fria",
            "status": "Coleção Privada (Apenas exposição)",
            "sensacao": "Ele é suave como uma aquarela, traz paz aos ouvidos e a pele fica fresca a 28 graus."
        },
        "Amarelo": {
            "nome": "do Pôr do Sol",
            "material": "Argila Polímera e Folhas Secas Resinadas",
            "status": "Vendido (Enviado para o colecionador)",
            "sensacao": "O som ao redor vira vento nas árvores e você sente o estalar de folhas secas ao tocá-lo."
        }
    }
    
    while True:
        cor_escolhida = input("\n🟡 Escolha uma cor de palitinho para ver a obra (Vermelho, Azul, Amarelo ou 'Sair'): ").strip().capitalize()

        if cor_escolhida == "Sair":
            print("\nVocê se despede do totem. As luzes da galeria se apagam e os dragões descansam...")
            break

        if cor_escolhida in dragoes:
            dragao_libertado = dragoes[cor_escolhida]
            
            print(f"\n🎨 Obra: Dragão {dragao_libertado['nome']}")
            print(f"🧱 Material Escultórico: {dragao_libertado['material']}")
            print(f"📦 Status no Ateliê: {dragao_libertado['status']}")
            print(f"✨ Experiência Sensorial: {dragao_libertado['sensacao']}")
            
        else:
            print("\n❌ Essa cor de palitinho não corresponde a nenhuma obra exposta.")
            print("💡 Dica: Lembre das cores primárias daquelas forminhas de picolé da nossa infância!")

if __name__ == "__main__":
    jogar_despertar_dos_dragoes()

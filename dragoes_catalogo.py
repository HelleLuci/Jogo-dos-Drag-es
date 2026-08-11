# PROJETO: O Despertar dos Dragões (Edição Catálogo Completo)
# AUTORA: Futura Tecnóloga em ADS (Unopar) / Especialista em Gestão de TI
# =====================================================================

def jogar_despertar_dos_dragoes():
    print("--- 🏛️ Bem-vinda à Exposição Interativa do Ateliê 🏛️ ---")

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
        # Agora o usuário também tem a opção de digitar 'Catalogo'
        cor_escolhida = input("\n🟡 Escolha uma cor, digite 'Catalogo' para ver todos ou 'Sair': ").strip().capitalize()

        if cor_escolhida == "Sair":
            print("\nVocê se despede do totem. As luzes da galeria se apagam e os dragões descansam...")
            break

        # 📚 NOVA FUNCIONALIDADE: Exibe todas as obras da galeria de uma vez só
        if cor_escolhida == "Catalogo":
            print("\n--- 📖 CATÁLOGO COMPLETO DA EXPOSIÇÃO ---")
            
            # O 'for' passa por cada dragão dentro do dicionário
            for cor, info in dragoes.items():
                print(f"\n🎨 Dragão {info['nome']} ({cor})")
                print(f"   🧱 Material: {info['material']}")
                print(f"   📦 Status: {info['status']}")
            
            print("\n-----------------------------------------")
            continue # Faz o jogo voltar para o início do 'while' sem passar pelos outros 'if/else'

        # Busca um dragão específico pela cor
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

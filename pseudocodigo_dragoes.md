programa
{
	// O Portugol usa a palavra "funcao"
	// Emojis deixam o jogo convidativo e ainda simples
	funcao inicio()
	{
		
		escreva("--- Bem-vindo ao Totem ---\n")
		
		// O "enquanto (verdadeiro)" no Portugol é a sentença de condição
		enquanto (verdadeiro) 
		{
			escreva("\n🟡 Escolha uma cor para libertar o Dragão (Vermelho, Azul, Amarelo ou 'Sair'): ")
			leia(cor_escolhida) // O "leia" faz o papel do "input" do Python

			// Condição de saída do jogo
			if (cor_escolhida == "Sair" ou cor_escolhida == "sair")
			{
				escreva("\n👋 Você se despede do totem. Os dragões voltam a descansar em suas caixas...\n")
				pare // O "pare" faz o papel de parar de fato o código
			}

			// O cérebro do programa decide qual dragão mostrar com base na cor
			se (cor_escolhida == "Vermelho" ou cor_escolhida == "vermelho")
			{
				escreva("\n🔥 Você libertou o Dragão Severino!\n")
				escreva("✨ Sensação: Suas escamas são feitas de medalhas de alumínio antigas e ele tem cheiro de carvão doce.\n")
			}
			senao se (cor_escolhida == "Azul" ou cor_escolhida == "azul")
			{
				escreva("\n💧 Você libertou o Dragão da Compadecida!\n")
				escreva("✨ Sensação: Ele é suave como uma aquarela, traz paz aos ouvidos e a pele fica fresca a 28 graus.\n")
			}
			senao se (cor_escolhida == "Amarelo" ou cor_escolhida == "amarelo")
			{
				escreva("\n🍂 Você libertou o Dragão do Pôr do Sol!\n")
				escreva("✨ Sensação: O som ao redor vira vento nas árvores e você sente o estalar de folhas secas ao tocá-lo.\n")
			}
			senao
			{
				escreva("\n❌ Essa cor não abre nenhuma caixa.\n")
				escreva("💡 Dica: Tente uma das cores primárias que você usava nos palitinhos de picolé!\n")
			}
		}
	}
}

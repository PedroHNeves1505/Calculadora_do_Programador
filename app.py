import funcoes
import os


def main():
	"""Inicia e mantém o ciclo de vida da Calculadora do Programador"""
	os.system('cls')
	funcoes.exibir_titulo()
	base, valor = funcoes.coletar_valores()
	resultados = funcoes.decidir_operacao(base, valor)
	funcoes.mostrar_resultado(base, resultados)
	input('\nPressione Enter para voltar ao menu...')
	main()


if __name__ == '__main__':
	main()
	
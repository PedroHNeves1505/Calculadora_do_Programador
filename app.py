import funcoes
import os
import sys


def main():
	"""Inicia e mantém o ciclo de vida da Calculadora do Programador"""
	os.system('cls')
	funcoes.exibir_titulo()
	base, valor = funcoes.coletar_valores()
	resultados = funcoes.decidir_operacao(base, valor)
	funcoes.mostrar_resultado(base, resultados)
	continuar = funcoes.sair_do_sistema()
	if continuar:
		input('\nDigite qualquer tecla para voltar ao menu principal.')
		main()
	else:
		print('Saindo so sistema!')
		sys.exit()
		
		
if __name__ == '__main__':
	main()
	
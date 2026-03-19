import os


def exibir_titulo():
	print('ℂ𝕒𝕝𝕔𝕦𝕝𝕒𝕕𝕠𝕣𝕒 𝕕𝕠 ℙ𝕣𝕠𝕘𝕣𝕒𝕞𝕒𝕕𝕠𝕣\n')


def coletar_valores():
	print('=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~')
	base = int(input('Digite a base do número para calculo: '))
	valor = int(input('Digite o valor: '))
	print('=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~')
	return base and valor


def decidir_operacao(base, valor):
	match base:
		case 2:
			resultados = [
				binario_quartenario(valor),
				binario_octal(valor),
				binario_decimal(valor),
				binario_hexadecimal(valor),
			]
			return resultados



def binario_quartenario(valor):
	valor = str(valor)
	num_quartenario = ''
	if len(valor) % 2 != 0:
		valor = '0' + valor
	for i in range(0, len(valor), 2):
		dupla = valor[i: i + 2]
		match dupla:
			case '00':
				num_quartenario = num_quartenario + '0'
			case '01':
				num_quartenario = num_quartenario + '1'
			case '10':
				num_quartenario = num_quartenario + '2'
			case '11':
				num_quartenario = num_quartenario + '3'
	return num_quartenario


def binario_octal(valor):
	return 8


def binario_decimal(valor):
	return 10


def binario_hexadecimal(valor):
	return 16


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
	valor = str(valor)
	resto = len(valor) % 3
	num_octal = ''
	if resto != 0:
		if resto == 1:
			valor = '00' + valor
		else:
			valor = '0' + valor
	for i in range(0, len(valor), 3):
		trio = valor[i: i + 3]
		match trio:
			case '000':
				num_octal = num_octal + '0'
			case '001':
				num_octal = num_octal + '1'
			case '010':
				num_octal = num_octal + '2'
			case '011':
				num_octal = num_octal + '3'
			case '100':
				num_octal = num_octal + '4'
			case '101':
				num_octal = num_octal + '5'
			case '110':
				num_octal = num_octal + '6'
			case '111':
				num_octal = num_octal + '7'
	return num_octal


def binario_decimal(valor):
	valor = str(valor)[::-1]
	num_decimal = 0
	for i in range(len(valor)):
		unidade_bin = int(valor[i])
		valor_decimal = int(unidade_bin) * 2**i
		num_decimal = num_decimal + valor_decimal
	return num_decimal
		
	
def binario_hexadecimal(valor):
	return 16


import os


def exibir_titulo():
	print('ℂ𝕒𝕝𝕔𝕦𝕝𝕒𝕕𝕠𝕣𝕒 𝕕𝕠 ℙ𝕣𝕠𝕘𝕣𝕒𝕞𝕒𝕕𝕠𝕣\n')


def coletar_valores():
	print('=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~')
	base = int(input('Digite a base do número para calculo: '))
	valor = int(input('Digite o valor: '))
	print('=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~')
	return base, valor


def decidir_operacao(base, valor):
	match base:
		case 2:
			return [
				binario_quartenario(valor),
				binario_octal(valor),
				binario_decimal(valor),
				binario_hexadecimal(valor),
			]
		case 4:
			return [
				quartenario_binario(valor),
				quartenario_octal(valor),
				quartenario_decimal(valor),
				quartenario_hexadecimal(valor),
			]
		case 8:
			return [
				octal_binario(valor),
				octal_quartenario(valor),
				octal_decimal(valor),
				octal_hexadecimal(valor),
			]
		case 10:
			return [
				decimal_binario(valor),
				decimal_quartenario(valor),
				decimal_octal(valor),
				decimal_hexadecimal(valor),
			]
		case _:
			print('Valor de base não suportada pelo sistema!')
			return None


def mostrar_resultado(base, resultados, valor):
	match base:
		case 2:
			print(f'Resultados\nBinario : {valor}\nQuartenario: {resultados[0]}\nOctal : {resultados[1]}\nDecimal : {resultados[2]}\nHexadecimal : {resultados[3]}')
		case 4:
			print(f'Resultados\nBinario : {resultados[0]}\nQuartenario: {valor}\nOctal : {resultados[1]}\nDecimal : {resultados[2]}\nHexadecimal : {resultados[3]}')
		case 8:
			print(f'Resultados\nBinario : {resultados[0]}\nQuartenario: {resultados[1]}\nOctal : {valor}\nDecimal : {resultados[2]}\nHexadecimal : {resultados[3]}')
		case 10:
			print(f'Resultados\nBinario : {resultados[0]}\nQuartenario: {resultados[1]}\nOctal : {resultados[2]}\nDecimal : {valor}\nHexadecimal : {resultados[3]}')
		case _:
			return None
	
	
def sair_do_sistema():
	input('\nDigite qualquer tecla para continuar.')
	os.system('cls')
	print('=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~')
	print('Deseja continuar do sistema?')
	continuar = input('Sim ou Não: ')
	if continuar == 'sim'.lower():
		return True
	else:
		return False


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
	valor = str(valor)
	resto = len(valor) % 4
	num_hexadecimal = ''
	if resto != 0:
		if resto == 1:
			valor = '000' + valor
		elif resto == 2:
			valor = '00' + valor
		else:
			valor = '0' + valor
	for i in range(0, len(valor), 4):
		quarteto = valor[i: i + 4]
		match quarteto:
			case '0000':
				num_hexadecimal = num_hexadecimal + '0'
			case '0001':
				num_hexadecimal = num_hexadecimal + '1'
			case '0010':
				num_hexadecimal = num_hexadecimal + '2'
			case '0011':
				num_hexadecimal = num_hexadecimal + '3'
			case '0100':
				num_hexadecimal = num_hexadecimal + '4'
			case '0101':
				num_hexadecimal = num_hexadecimal + '5'
			case '0110':
				num_hexadecimal = num_hexadecimal + '6'
			case '0111':
				num_hexadecimal = num_hexadecimal + '7'
			case '1000':
				num_hexadecimal = num_hexadecimal + '8'
			case '1001':
				num_hexadecimal = num_hexadecimal + '9'
			case '1010':
				num_hexadecimal = num_hexadecimal + 'A'
			case '1011':
				num_hexadecimal = num_hexadecimal + 'B'
			case '1100':
				num_hexadecimal = num_hexadecimal + 'C'
			case '1101':
				num_hexadecimal = num_hexadecimal + 'D'
			case '1110':
				num_hexadecimal = num_hexadecimal + 'E'
			case '1111':
				num_hexadecimal = num_hexadecimal + 'F'
	return num_hexadecimal


def quartenario_binario(valor):
	valor = str(valor)
	num_binario = ''
	for digito in valor:
		match digito:
			case '0':
				num_binario = num_binario + '00'
			case '1':
				num_binario = num_binario + '01'
			case '2':
				num_binario = num_binario + '10'
			case '3':
				num_binario = num_binario + '11'
	return num_binario


def quartenario_octal(valor):
	valor = quartenario_binario(valor)
	return binario_octal(valor)


def quartenario_decimal(valor):
	valor = str(valor)[::-1]
	num_decimal = 0
	for i in range(len(valor)):
		unidade_quartenaria = int(valor[i])
		valor_decimal = int(unidade_quartenaria) * 4**i
		num_decimal = num_decimal + valor_decimal
	return num_decimal


def quartenario_hexadecimal(valor):
	valor = quartenario_binario(valor)
	return binario_hexadecimal(valor)


def octal_binario(valor):
	valor = str(valor)
	num_binario = ''
	for digito in valor:
		match digito:
			case '0':
				num_binario = num_binario + '000'
			case '1':
				num_binario = num_binario + '001'
			case '2':
				num_binario = num_binario + '010'
			case '3':
				num_binario = num_binario + '011'
			case '4':
				num_binario = num_binario + '100'
			case '5':
				num_binario = num_binario + '101'
			case '6':
				num_binario = num_binario + '110'
			case '7':
				num_binario = num_binario + '111'
	return num_binario


def octal_quartenario(valor):
	valor = octal_binario(valor)
	return binario_quartenario(valor)


def octal_decimal(valor):
	valor = str(valor)[::-1]
	num_decimal = 0
	for i in range(len(valor)):
		unidade_quartenaria = int(valor[i])
		valor_decimal = int(unidade_quartenaria) * 8**i
		num_decimal = num_decimal + valor_decimal
	return num_decimal


def octal_hexadecimal(valor):
	valor = octal_binario(valor)
	return binario_hexadecimal(valor)


def decimal_binario(valor):
	num_binario = ''
	while valor > 0:
		resto = valor % 2
		num_binario = str(resto) + num_binario
		valor = valor // 2
	return num_binario
def decimal_quartenario(valor):
	num_quartenario = ''
	while valor > 0:
		resto = valor % 4
		num_quartenario = str(resto) + num_quartenario
		valor = valor // 4
	return num_quartenario


def decimal_octal(valor):
	num_octal = ''
	while valor > 0:
		resto = valor % 8
		num_octal = str(resto) + num_octal
		valor = valor // 8
	return num_octal


def decimal_hexadecimal(valor):
	num_hexadecimal = ''
	while valor > 0:
		resto = valor % 16
		num_hexadecimal = str(resto) + num_hexadecimal
		valor = valor // 16
	return num_hexadecimal

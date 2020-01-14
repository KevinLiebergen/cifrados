#!/usr/bin/python3
from codecs import getencoder
import base64


def preguntar_texto():
	print("Introduce texto a cifrar")
	texto_plano = input()
	return texto_plano

# CODIFICAMOS EN BASE64 2 VECES
def b64(texto):
	codi = base64.b64encode(texto.encode())
	return codi.decode()

# ROT 13 - CIFRADO CESAR
def rot13(codi_dos):
	enc = getencoder("rot-13")
	return enc(codi_dos)[0]

# ASCII A NUMEROS - CIFRADO CLASICO
def ascii_numeros(cesar):
	texto_cifrado = ""
	for i in range(len(cesar)):
		texto_cifrado += str(ord(cesar[i])) + " "
	return texto_cifrado



if __name__ == '__main__':
	plano = preguntar_texto()
	una_vez = b64(plano)
	dos_veces = b64(una_vez)
	rotado = rot13(dos_veces)
	cifrado = ascii_numeros(rotado)
	print("Mensaje cifrado: {}".format(cifrado))


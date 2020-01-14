#!/usr/bin/python3
from codecs import getencoder
import base64


def preguntar_texto():
	print("Introduce texto a descifrar")
	texto_plano = input()
	return texto_plano

# DE-CODIFICAMOS EN BASE64
def b64(texto):
	#codi = base64.b64encode(texto.encode())
	codi = base64.b64decode(texto.encode())
	return codi.decode()

# ROT 13 - CIFRADO CESAR
def rot13(codi_dos):
	enc = getencoder("rot-13")
	return enc(codi_dos)[0]

# NUMEROS A ASCII - CIFRADO CLASICO
def numeros_ascii(texto):
	ascii = ""
	partido = texto.split()
	for i in range(len(partido)):
		ascii += chr(int(partido[i]))
	return ascii


if __name__ == '__main__':
	plano = preguntar_texto()
	asciis = numeros_ascii(plano)
	rotado = rot13(asciis)
	una_vez = b64(rotado)
	dos_veces = b64(una_vez)
	print("Texto plano: {}".format(dos_veces))


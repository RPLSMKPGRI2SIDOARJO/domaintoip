#	Tools by X-Rpl
#	since 09/07/2021
import socket
import os
import time
header = """
'########:::'#######::'##::::'##::::'###::::'####:'##::: ##:'####:'########::
 ##.... ##:'##.... ##: ###::'###:::'## ##:::. ##:: ###:: ##:. ##:: ##.... ##:
 ##:::: ##: ##:::: ##: ####'####::'##:. ##::: ##:: ####: ##:: ##:: ##:::: ##:
 ##:::: ##: ##:::: ##: ## ### ##:'##:::. ##:: ##:: ## ## ##:: ##:: ########::
 ##:::: ##: ##:::: ##: ##. #: ##: #########:: ##:: ##. ####:: ##:: ##.....:::
 ##:::: ##: ##:::: ##: ##:.:: ##: ##.... ##:: ##:: ##:. ###:: ##:: ##::::::::
 ########::. #######:: ##:::: ##: ##:::: ##:'####: ##::. ##:'####: ##::::::::
........::::.......:::..:::::..::..:::::..::....::..::::..::....::..:::::::::

Tools by      : X-Rpl
date creation : 24/06/2022
"""
def domaintoip():
	try:
		domain = input("\nMasukan Domain> ")
		print("============{{ HASIL }}============\n")
		print("Domain> ", domain)	
		print("Ip>     ", socket.gethostbyname(domain), "\n")
		input("Terimakasih Telah menggunakan tools ini\nklik [ENTER] untuk keluar")
	except:
		alert = input("input yang anda masukan salah!\napakah anda ingin mengulang script?\n[Y/N]\nPilihan: ")
		for i in alert:
			if i != "N":
				domaintoip()
os.system("clear")
print(header)
domaintoip()

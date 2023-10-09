#!/usr/bin/env python3
"""
program pro vypocet objemu/obsahu/obvodu
"""
import math

def objem_koule():
     polomer = float(input("Zadejte polomer koule:"))
     objem = (4/3)*math.pi*(polomer*polomer*polomer)
     print(f"Objem koule s polomerem {polomer} je {objem}")
def objem_kvadr():
    stranaA = float(input("Zadejte delku strany a:"))
    stranaB = float(input("Zadejte delku strany b:"))
    stranaC = float(input("Zadejte delku strany c:"))
    objem = stranaA * stranaB * stranaC
    print(f"Objem kvadru je {objem}")
def objem_krychle():
    stranaA = float(input("Zadejte delku strany a:"))
    objem = stranaA*stranaA*stranaA
    print(f"Objem krychle je {objem}")


def obsah_kruh():
    polomer = float(input("Zadejte polomer kruhu:"))
    obsah = math.pi*(polomer*polomer)
    print(f"Obsah kruhu je {obsah}")
def obsah_ctverec():
    stranaA = float(input("Zadejte delku strany a:"))
    obsah = stranaA*stranaA
    print(f"Obsah ctverce je {obsah}")
def obsah_obdelnik():
    stranaA = float(input("Zadejte delku strany a:"))
    stranaB = float(input("Zadejte delku strany b:"))
    obsah = stranaA*stranaB
    print(f"Obsah obdelniku je {obsah}")


def obvod_ctverec():
    stranaA = float(input("Zadejte delku strany a:"))
    obvod = 4 * stranaA
    print(f"Obvod ctverce je {obvod}")
def obvod_obdelnik():
    stranaA = float(input("Zadejte delku strany a:"))
    stranaB = float(input("Zadejte delku strany b:"))
    obvod = 2*(stranaA + stranaB)
    print(f"Obvod obdelniku je {obvod}")
def obvod_kruh():
    polomer = float(input("Zadejte polomer kruhu:"))
    obvod = 2*math.pi*polomer
    print(f"Obvod kruhu je {obvod}")



def main():
    print("Zvol 1 pro objem, 2 pro obsah nebo 3 pro obvod")
    vyber1 = input()
    if vyber1 == "1":
        print("Zvol 1 pro koule 2 pro kvadr, nebo 3 pro krychle")
        vyber2 = input()
        if vyber2 == "1":
            objem_koule()
        elif vyber2 == "2":
            objem_kvadr()
        elif vyber2 == "3":
            objem_krychle()
    elif vyber1 == "2":
        print("Zvol 1 pro kruh, 2 pro ctverec, nebo 3 pro obdelnik")
        vyber3 = input()
        if vyber3 == "1":
            obsah_kruh()
        elif vyber3 == "2":
            obsah_ctverec()
        elif vyber3 == "3":
            obsah_obdelnik()
    elif vyber1 == "3":
        print("Zvol 1 pro kruh, 2 pro ctverec, nebo 3 pro obdelnik")
        vyber4 = input()
        if vyber4 == "1":
            obvod_kruh()
        elif vyber4 == "2":
            obvod_ctverec()
        elif vyber4 == "3":
            obvod_obdelnik()
        
if __name__ == "__main__":
    main()
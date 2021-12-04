#!/usr/bin/env python3
import hashlib
import sys
import time


def Banner():
    print("Usage : Python3 md5.py hash password file")
    print("""


        MD5 Cracker Coded By Eng Yazeed


                       ...
             ;::::;
           ;::::; :;
         ;:::::'   :;
        ;:::::;     ;.
       ,:::::'       ;           OOO\
       ::::::;       ;          OOOOO\
       ;:::::;       ;         OOOOOOOO
      ,;::::::;     ;'         / OOOOOOO
    ;:::::::::`. ,,,;.        /  / DOOOOOO
  .';:::::::::::::::::;,     /  /     DOOOO
 ,::::::;::::::;;;;::::;,   /  /        DOOO
;`::::::`'::::::;;;::::: ,#/  /          DOOO
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O
  `:::::`::::::::;' /  / `:#
   ::::::`:::::;'  /  /   `#



     """)


def crack_MD5_Hash(hash_to_crack, wordlist):
    file = open(wordlist, "r")
    for password in file:
        md5_hash = (password.strip("\n")).encode('UTF-8')
        if hashlib.md5(md5_hash).hexdigest() == hash_to_crack:
            return password
            return None



if __name__ == '__main__':

    hash_to_crack = sys.argv[1]
    
    wordlist = sys.argv[2]
    

    Banner()
    print(crack_MD5_Hash(hash_to_crack , wordlist))


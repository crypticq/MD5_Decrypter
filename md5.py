#!/usr/bin/env python3
import hashlib
import sys
import time

class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'



def Banner():
    print(style.RED+"Usage : Python3 md5.py hash password file")
    print(style.CYAN+"""


        MD5 Cracker Coded By Eng Yazeed

                                                                   _...
                                                       _.'`       -_ ``.
                                                   .-'`                 `.
                                                .-`                     q ;
                                             _-`                       __  \
                                         .-'`                  . ' .   \ `;/
                                     _.-`                    /.      `._`/
                             _...--'`                        \_`..._
                          .'`                         -         `'--:._
                       .-`                           \                  `-.
                      .                `              `-..__.....----...., `.
                     '                 `  '''---..-''`'              : :  : :
                   .` -                '`.  `-.                       `'   `'
                .-` .` '             .`'.__ ;
            _.-` .-`   '            .
        _.-` _.-`    .' '         .`
(`''--'' _.-`      .'  '        .'
 `'----''        .'  .`       .`
               .'  .'     .-'`
             .'   :    .-`
             `. .`   ,`
              .'   .'
             '   .`
            '  .`
            `  '.
            `.___;


     """)


def crack_MD5_Hash(hash_to_crack, wordlist):
    file = open(wordlist, "r")
    for password in file:
        md5_hash = (password.strip("\n")).encode('UTF-8')
        if hashlib.md5(md5_hash).hexdigest() == hash_to_crack:
            print(style.CYAN +"**************************************")
            return f"password Cracked ! >> Password is >>> {password}"
            return None



if __name__ == '__main__':

    hash_to_crack = sys.argv[1]
    
    wordlist = sys.argv[2]
    

    Banner()
    print(crack_MD5_Hash(hash_to_crack , wordlist))


from stegano import exifHeader
import pyfiglet
import os
from colorama import *

figl = pyfiglet.figlet_format('STEGANO', font='slant')
print(figl)

def steganohide(foto, donefoto, message):
    secret = exifHeader.hide(foto, donefoto, message)

def steganoopen(donefoto):
    result = exifHeader.reveal(donefoto)
    result = result.decode()
    print(result)

if __name__ == '__main__':
    try:
        tanla = int(input(Fore.MAGENTA + 'Hide Messege[1] Read Message[0] : '))
    except:
        pass

    if tanla == 1:
        photopath = str(input(Fore.BLUE + 'Path to Photo>>>'))
        donephotopath = str(input(Fore.BLUE + 'Finished photo path>>>'))
        xabar = str(input(Fore.BLUE + 'Message>>>'))
        steganohide(photopath, donephotopath, xabar)
    elif tanla == 0:
        goresult = str(input(Fore.BLUE + 'Path to photo with message>>>'))
        steganoopen(goresult)
    else:
        x = input(Fore.RED + 'E R R O R(press ENTER to exit th programm)')

    # y = input(Fore.RED + 'E R R O R(press ENTER to exit th programm)')

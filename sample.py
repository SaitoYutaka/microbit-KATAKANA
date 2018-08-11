from microbit import *
from katakana import Katakana

k = Katakana()
while True:
    k.display_kana("ko nn ni ti ha")
    sleep(2000)
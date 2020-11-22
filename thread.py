import random
import sys
from threading import Thread
import time

class Afficheur(Thread) :
    def __init__(self, lettre):
        Thread.__init__(self)
        self.lettre = lettre

    def run(self):
        i = 0
        while i < 60:
            sys.stdout.write(self.lettre)
            sys.stdout.flush()
            attente = 0.2
            attente += random.randint(1, 60) / 1000000
            time.sleep(attente)
            i += 1

thread_1 = Afficheur("1")
thread_2 = Afficheur("2")
thread_3 = Afficheur("3")
thread_4 = Afficheur("4")

thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()

thread_1.join()
thread_2.join()
thread_3.join()

thread_4.join()
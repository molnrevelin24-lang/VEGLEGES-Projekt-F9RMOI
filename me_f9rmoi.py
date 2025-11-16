import time
import random

def ME_var(min_s, max_s):
    return random.randint(min_s, max_s)

def ME_ido():
    return time.time()

def ME_mentes(tartalom):
    try:
        f = open("eredmenyek.txt", "a")
        try:
            f.write(tartalom+"\n")
            print("A program lefutott!")
        except:
            print("HIBA: nem sikerült a fájl mentés")
        finally:
            f.close()
    except:
        print("HIBA: nem sikerült a fájl nyitása")



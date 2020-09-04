import time

def jogando():

    load = []

    for i in range(0,4):
        load.append(".")

    print("\nJogando",end = " ")
    for i in range(0,len(load)-1):
        time.sleep(1.0)
        print(load[i], end = " " )


jogandp = jogando()


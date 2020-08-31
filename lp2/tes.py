from time import sleep

while True:
    for h in range(24):
        for m in range(60):
            for s in range(60): # [0..60[
                print('%02d:%02d:%02d' % (h,m,s))
                sleep(0.00001)
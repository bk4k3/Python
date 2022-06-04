import random

min = "abcdefghijklmnñopqrstuvwxyz"

may = min.upper()

num = str(1234567890)

sim  = "$#@_&-+()/*':;!?~`|%{}[\]÷×"

sim2 = '"'

long = 15
all = min+may+num+sim+sim2

for x in range(1000):
    gen = random.sample(all, long)
    psw = "".join(gen)
    print(psw)

  

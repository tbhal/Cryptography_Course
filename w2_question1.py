import numpy as np

def get_order():

    amounts = np.array(
        [pow(2,128), pow(10,6), pow(pow(10,6),5),
        pow(pow(10,6),6), pow(pow(10,6),7)]
    )

    sorteIndex = np.argsort(amounts)
    sorteIndex = [i+1 for i in sorteIndex]
    print(sorteIndex)

get_order()

# order is [2, 3, 4, 1, 5]
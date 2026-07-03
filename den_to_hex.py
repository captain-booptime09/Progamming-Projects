import random

def denhexcon(denary_input):

    hexa = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

    binarr = [0,0,0,0,0,0,0,0]
    binval = [128,64,32,16,8,4,2,1]

    input_number1 = int(denary_input)

    count = 0

    while input_number1 > 0 and count < 8:
        if (input_number1 - binval[count]) >= 0:
            input_number1 = input_number1 - binval[count] 
            binarr[count] = 1
        

        count = count + 1

    halfval = [8,4,2,1]

    half1 = []
    for i in range(0,4):
        half1.append(binarr[i])

    half2 = []
    for i in range(0,4):
        index = i + 4
        half2.append(binarr[index])

    half1val = 0
    half2val = 0

    count = 0
    while count < len(half1):
        if half1[count] == 1:
            half1val = half1val + halfval[count]
        count = count + 1

    count = 0
    while count < len(half2):
        if half2[count] == 1:
            half2val = half2val + halfval[count]
        count = count + 1

    hexaformat = ""

    hexaformat = hexaformat + hexa[half1val]
    hexaformat = hexaformat + hexa[half2val]

    return hexaformat


def main():
    denaryvalue = random.randint(0,256)
    result = denhexcon(denaryvalue)
    print(f"Hexadecimal format of {denaryvalue} is {result}")
    
main()
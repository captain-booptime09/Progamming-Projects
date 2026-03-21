
def fibo(num, num_arr):
    lenarr = len(num_arr) - 1
    if num == 0:
        return num + 1
    elif num == 1:
        return num + 1
    else:
        return num_arr[lenarr - 1] + num_arr[lenarr]
    
def main():
    file = open("fibo_text.txt",'w')
    file.write("\n")
    file.close()
    num = 0
    print(num)
    num_arr = [0]
    count = 0
    file = open("fibo_text.txt",'a')
    while count < 9999:
        print(num)
        file.write(str(num) + "\n")
        result = fibo(num, num_arr)
        num = result
        num_arr.append(num)
        count += 1
    file.close()

main()

file = open("fibo_text.txt",'r')
readcontent = file.read()
even = ["0","2","4","6","8"]
evencount = 0
oddcount = 0
for i in range(len(readcontent)):
    for ii in range(0,5):
        if readcontent[i] == even[ii]:
            evencount += 1
        else:
            oddcount += 1
file.close()

print(f"EVEN COUNT: {evencount}.")
print(f"ODD COUNT: {oddcount}.")
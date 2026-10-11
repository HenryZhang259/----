num_first = int(print("请输入起始的数: "))
num_last= int(print("请输入结尾的数: "))
prime_number = []
for num in range(num_first, num_last + 1):
    if num = 1:
        continue
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            prime_number.append(num)
print("素数列表为:", prime_number)

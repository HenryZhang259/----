num_first = input("请输入起始的数: ")
num_last = input("请输入结尾的数: ")
num_first = int(float(num_first))
num_last = int(float(num_last))
prime_number = []
for num in range(num_first, num_last + 1):
    if num <= 1:
        continue
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            prime_number.append(num)
print("素数列表为:", prime_number)

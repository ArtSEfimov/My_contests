repeat_string = input()
ind = 0

for i in range((len(repeat_string) // 2) + 1):
    elem = repeat_string[:ind + 1]
    count = repeat_string.count(elem)
    if len(elem) * count == len(repeat_string):
        print(count)
        break
    elif (len(repeat_string) - count * len(elem)) == 1:
        print(1)
        break

    ind += 1

else:
    print(1)

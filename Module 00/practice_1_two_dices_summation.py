for i in range(7):
    if i==0:
        print('+ ', end='')
    else:
        print("{}".format(i), end=' ')
    for j in range(1, 7):
        n = i+j
        if n >= 10:
            print("{:02d}".format(n), end=' ')
        else:
            print(" {}".format(n), end=' ')
    print('')

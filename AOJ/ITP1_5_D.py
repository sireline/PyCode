def func(n):
    i = 1
    while i <= n:
        x = i
        if x%3 == 0:
            print(f' {i}', end='')
        else:
            while x:
                if x%10 == 3:
                    print(f' {i}', end='')
                    break
                else:
                    x /= 10
        i += 1
    print('')

func(int(input()))
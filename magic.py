while 1:
    N = int(input("Введите число от 4 до 1000: "))
    if 4 <= N <= 1000:
        a = [None] * N
        for i in range(N):
            a[i] = [None] * N
        c = 1
        up = 0
        while(up < N // 2):
            n = N - up * 2 - 1
            for x in range(n):
                a[up][up + x] = c
                c += 1
            for y in range(n):
                a[up + y][N - 1 - up] = c
                c += 1
            for x in range(n):
                a[N - 1 - up][N - 1 - up - x] = c
                c += 1
            for y in range(n):
                a[N - 1 - up - y][up] = c
                c += 1
            up += 1
        if (N % 2):
            a[up][up] = c
        for y in range(N): print(a[y])
    else:
        print("Вы ввели неврное число.")
    continue

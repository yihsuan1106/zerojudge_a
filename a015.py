while True:
    try:
        r, c = map(int,input().split())
        q = []
        for i in range(r):
            q.append(list(map(int,input().split())))
        for i in range(c):
            for j in range(r):
                print(q[j][i],end=' ')
            print()
    except EOFError:
        break

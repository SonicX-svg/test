def task1(m, n):
    i, result = 0, []
    while True:
        result.append(m[i:i+n][0])
        print(m[i:i+n]+m[:n-len(m[i:i+n])])
        i = (i+n)%len(m)-bool((i+n)%len(m))
        if m[i:i+n][0] == m[0]:
            result.append(m[-1])     
            print('\nresult = ',result)
            break
        
if __name__ == '__main__':        
    m = list(range(1, 1+int(input('введите длину массива '))))
    n = int(input('введите шаг массива '))
    task1(m, n)

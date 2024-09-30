def solution(x, n) :
    arr = []
    for i in range(n):
        arr.append(x * (i + 1))
    return arr

print(solution(2,5))
print(solution(4,3))
print(solution(-4,2))
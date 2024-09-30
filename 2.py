def solution(phone_number):
    str = ''
    for i in range(len(phone_number)) :
        if(i < len(phone_number) - 4) : str += '*'
        else : str += phone_number[i]
    return str

print(solution('01033334444'))
print(solution('027778888'))
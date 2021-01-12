# if set set(a) = set(b) = 0, then result is 1
import re


def solution(a: str, b:str):

    # change lower_characters
    a = a.lower()
    b = b.lower()

    a_set = []
    b_set = []
    for i in range(len(a)-1):
        if re.findall('[a-z]',a[i]) and re.findall('[a-z]', a[i+1]):
            a_set.append(a[i]+a[i+1])
    for j in range(len(b)-1):
        if re.findall('[a-z]', b[j]) and re.findall('[a-z]',b[j+1]):
            b_set.append(b[j]+b[j+1])
    #intersaction
    inter = []
    for i in a_set:
        if i in b_set:
            inter.append(i)
            b_set.remove(i)
    #union
    sum = a_set + b_set

    #union == 0 case
    if len(sum) == 0:
        return 65536
    # else
    return (int(len(inter) / len(sum) * 65536))

a = "FRANCE"
b = "FRENCH"
a2 = "handshake"
b2 = "shake hands"
a3 = "aa1+aa2"
b3 = "AAAA12"
a4 = "E=M*C^2"
b4 = "e=m*c^2"
print (solution(a3,b3))

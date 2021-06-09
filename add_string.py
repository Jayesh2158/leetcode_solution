num1="9333852702227987"
num2="85731737104263"
res = []

carry = 0
p1 = len(num1) - 1  #15
p2 = len(num2) - 1  #13
while p1 >= 0 or p2 >= 0:
    x1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
    x2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0
    print(x1,x2)
    value = (x1 + x2 + carry) % 10
    print('value=',value)
    carry = (x1 + x2 + carry) // 10
    print('carry=',carry)
    res.append(value)
    p1 -= 1
    p2 -= 1
        
if carry:
    res.append(carry)
        
print(''.join(str(x) for x in res[::-1]))
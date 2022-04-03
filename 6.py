def change(number, base):
   
    strings = "0123456789ABCDEF"
    
    if number < base:
       return strings[number]
   
    else:
       return change(number // base, base) + strings[number % base]


n2, n8, n16 = '', '', ''

n = int(input('10진수 입력 -->'))

n2 = change(n, 2)
n8 = change(n, 8)
n16 = change(n, 16)

print('2진수 : ', n2)
print('8진수 : ', n8)
print('16진수 : ', n16)

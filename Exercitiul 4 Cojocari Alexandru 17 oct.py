a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
if pow(a,2)+pow(b,2)==pow(c,2) or pow(a,2)+pow(c,2)==pow(b,2) or pow(b,2)+pow(c,2)==pow(a,2):
    print(a,b,c,'sunt numere pitagoriene')
else:
    print(a,b,c,'nu sunt numere pitagoriene')

a=int(input('Dati a='))
b=int(input('Dati b='))
c=int(input('Dati c='))
if a<b<c or c<b<a:
    print(b,'este numarul intre celelante')
elif b<a<c or c<a<b:
    print(a,'este numarul intre celelate')
elif a<c<b or b<c<a:
    print(c,'este numarul intre celelate')
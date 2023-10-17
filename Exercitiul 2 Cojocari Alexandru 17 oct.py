h_max=20
h1=int(input('h1='))
h2=int(input('h2='))
h3=int(input('h3='))
h4=int(input('h4='))
h5=int(input('h5='))
h6=int(input('h6='))
h7=int(input('h7='))
if h1+h2+h3+h4+h5+h6+h7>h_max:
    print('El va fi pedepsit')
elif h1+h2+h3+h4+h5+h6+h7<h_max or h1+h2+h3+h4+h5+h6+h7==h_max:
    print('El nu va fi pedepsit')

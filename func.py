def func(name):
    str1='mississipi'
    i=0
    c=0
    d=0
    p=0
    for count in str1:
        if count=='m':
            i+=1
        elif count=='i':
            c+=1
        elif count=='s':
            d+=1
        elif count=='p':
            p+=1
    print(f'm->{i}')
    print(f'i->{c}')
    print(f's->{d}')
    print(f'p->{p}')

func('mississipi')


    
def function (data1, data2, deret):
    if deret =='plus1' :
        hasil = [i for i in range (data1,data2+1)]

    elif deret =='kuadrat':
        n1 = data1
        hasil = []
        for i in range (data1, data2+1):
            hasil.append(n1)
            n1 = data1**i
            if n1 > data2:
                break

    elif deret =='fibonacci':
        count = 0
        n1 = data1
        n2 = data1+1
        hasil =[]
        for count in range (data2):
            hasil.append(n1)
            bilangan_akhir = n1+n2
            n1=n2
            n2 = bilangan_akhir
            if n1 > data2:
                break
            count +=1

    return hasil


hasil_plus1 = function (2,10,'plus1')
hasil_kuadrat = function (2,10,'kuadrat')
hasil_fibonaci = function (2,10,'fibonacci')

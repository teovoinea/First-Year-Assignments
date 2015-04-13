def roman(n):
    translation =''
    table=[['M',1000],['CM',900],['D',500],['CD',400],['C',100],['XC',90],
           ['L',50],['XL',40],['X',10],['IX',9],['V',5],['IV',4],['I',1]]
    for o in table:
        while n-o[1]>=0:

            n-=o[1]
            translation+=o[0]
    return translation

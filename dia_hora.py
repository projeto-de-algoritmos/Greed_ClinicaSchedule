def ler_dia(x):
    count = 0
    position = 0
    for i in x:
        position+=1
        if i == "/" or position == (len(x)-1):
            if count == 0:
                dia = d
                count+=1
            
            elif count == 1:
                mes = d

            else:
                ano = d

            d = ""
        
        else:
            d.append(i)
    
    return dia, mes, ano

def ler_hora(x):
    count = 0
    position = 0
    for i in x:
        position+=1
        if i == ":" or position == (len(x)-1):
            if count == 0:
                hora = d
                count+=1
            
            elif count == 1:
                minuto = d

            d = ""
        
        else:
            d.append(i)
    
    return hora, minuto
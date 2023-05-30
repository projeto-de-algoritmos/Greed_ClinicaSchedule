import datetime

# essa solução não ordena os dados, quando utilizar passe rows ordenado
def interval_partioniong(rows):
    salas = 0   #usado para contar salas usadas ao mesmo tempo
    d = []
    count = 0
    print(rows)
    for i in rows:
        if len(d) == 0:
            salas+=1
            i.append(salas)
            d.append(i)

        else:   #kala
            fim = datetime.datetime.strptime(d[-1][2], '%H:%M')   #recebe o horário de termino consulta
            verifica = datetime.datetime.strptime(d[-1][1], '%H:%M')   #variavel para verificar virada do dia
            disputante = datetime.datetime.strptime(i[1], '%H:%M')   #recebe horário de inicio da disputante a ultima

            #verifica virada do dia
            if fim<verifica:
                if disputante > verifica or disputante < fim:
                    salas+=1
                    i.append(salas)
                    d.append(i)

                else:
                    salas = 0
            
            else:
                if fim > disputante:
                    salas+=1
                    i.append(salas)
                    d.append(i)

                else:
                    salas = 0
        count += 1

    return d
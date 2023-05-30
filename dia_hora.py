import datetime

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

def verifica_conflito_hora(exp_ini, exp_fi, horario_inicio, horario_fim):
    time_ini = datetime.datetime.strptime(exp_ini, '%H:%M')
    time_fim = datetime.datetime.strptime(exp_fi, '%H:%M')

    time_horario = datetime.datetime.strptime(horario_inicio, '%H:%M')
    time_horFim = datetime.datetime.strptime(horario_fim, '%H:%M')

    # Tratamento erros causados pela virada de dia
    if time_horario > time_horFim and time_ini < time_fim:
        return False

    elif time_ini > time_fim and time_horario < time_horFim:
        # Se a consulta estiver entre os horarios de não atendimento retorna falso
        if time_horFim <= time_ini and time_horario >= time_fim:
            return False
        
        else:
            return True

    else:
        # Se a consulta estiver entre os horarios de atendimento retorna true
        if time_horFim <= time_fim and time_horario >= time_ini:
            return True
        
        else:
            return False
        
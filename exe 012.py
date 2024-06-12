hora =  int(input('digite a Hora'))
minuto = float(input('digite os minutos'))
dia =  int(input('digite o dia'))
segundos = hora * 3600
segundos = minuto * 60
dia = dia * 24 * 3600
ts = (hora*3600) + (minuto*60) + (dia*24*3600)
print('o total de segundos é',ts)
from datetime import datetime
import locale
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')


def calculadora(calculo):
    return f'El resultado de {calculo} es {round(eval(calculo), 2)}'


def calendario(ahora):
    return ahora.strftime('Hoy es %A, %d de %B de %Y.')


def reloj(ahora):
    return ahora.strftime('Son las %l:%M.')


if __name__ == "__main__":

    print('*** BIENVENIDO A SU ASISTENTE PERSONAL ***',
          '[1] para abrir la calculadora',
          '[2] para abrir el calendario',
          '[3] para abrir el reloj', sep="\n")

    ahora = datetime.now()
    funcionalidad = input('Por favor introduzca la funcionalidad deseada: ')

    if funcionalidad == '1':
        calculo = input('Ingrese el cálculo deseado: ')
        print(calculadora(calculo))
    elif funcionalidad == '2':
        print(calendario(ahora))
    elif funcionalidad == '3':
        print(reloj(ahora))
    else:
        print('Por favor, introduzca una opción válida')

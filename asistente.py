from datetime import datetime
import locale
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')


def calculadora(calculo):
    return f'El resultado de {calculo} es {round(eval(calculo), 2)}'


def calendario(ahora):
    return ahora.strftime('Hoy es %A, %d de %B de %Y.')


def reloj(ahora):
    return ahora.strftime('Son las %l:%M.')


def conversor_distancia(unidad, distancia):
    if unidad == 'k':
        return f'{distancia} kilómetros son {distancia * 0.621371} millas.'
    elif unidad == 'm':
        return f'{distancia} millas son {round((distancia / 0.621371), 2)} kilómetros.'
    else:
        return 'Por favor ingrese una opción válida.'
    return conversor_distancia(unidad, distancia)


if __name__ == "__main__":

    print('*** BIENVENIDO A SU ASISTENTE PERSONAL ***',
          '[1] para abrir la calculadora',
          '[2] para abrir el calendario',
          '[3] para abrir el reloj',
          '[4] para abrir el conversor de millas a kilómetros y viceversa',
          sep="\n")

    ahora = datetime.now()
    funcionalidad = input('Por favor introduzca la funcionalidad deseada: ')

    if funcionalidad == '1':
        calculo = input('Ingrese el cálculo deseado: ')
        print(calculadora(calculo))
    elif funcionalidad == '2':
        print(calendario(ahora))
    elif funcionalidad == '3':
        print(reloj(ahora))
    elif funcionalidad == '4':
        unidad = input('Por favor introduzca el factor de conversión deseado,'
                       '[k] para kilómetros y [m] para millas: ')
        distancia = int(input(
            'Por favor introduzca la distancia que desea calcular: '))
        print(conversor_distancia(unidad, distancia))
    else:
        print('Por favor, introduzca una opción válida')

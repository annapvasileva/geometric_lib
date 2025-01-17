import math


def area(r):
    '''
    Принимает радиус круга и возвращает
    его площадь.
    
            Параметры:
                    r (int) : радиус круга
            
            Возвращаемое значение:
                    area (r) : площадь круга с радиусом r
    
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Принимает радиус окружности и
    возвращает её длину.
    
            Параметры:
                    r (int) : сторона квадрата
            
            Возвращаемое значение:
                    perimiter (r) : длина окружности с радиусом r
    
    '''
    return 2 * math.pi * r


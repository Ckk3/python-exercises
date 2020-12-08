
def increase(value, tax):
    '''
    Increases tax in a value
    :param value: number that will be increased
    :param tax: tax that will be added
    :return: number increased in 10%
    '''

    percentage = tax/100 + 1
    total = value * percentage
    return total


def decrease(value, tax):
    '''
    Decreases a value with the tax
    :param value: number that will be decreased
    :param tax: tax that will be removal
    :return:
    '''

    percentage = 1 - tax/100
    total = value * percentage
    return total


def double(value):
    '''
    Double a value
    :param value: number
    :return: number * 2
    '''

    num = value * 2
    return num


def half(value):
    '''
    find halt of value
    :param value: number
    :return: number/2
    '''

    num = value/2
    return num


def formatPrice(value):
    '''
    Format price to R${value}.00
    :param value: price
    :return: string strPrice
    '''

    price = float(value)
    strPrice = 'R$' + (f'{price:.2f}')
    return strPrice


def readMoney(question):
    '''
    verify the input price
    :return: the correct price (float())
    '''
    while True:
        value = str(input(question)).strip().replace(',', '.')
        if value.isalpha() or value == '' or not value.isnumeric():
            print(f'{value} is invalid!!')
        else:
            return float(value)



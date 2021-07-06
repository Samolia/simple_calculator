from django.shortcuts import render
import operator

ACTIONS = {
    'умножить': operator.mul,
    'поделить': operator.truediv,
    'поделить без остатка': operator.floordiv,
    'получить остаток от деления': operator.mod,
    'сложить': operator.add,
    'отнять': operator.sub,
    'возвести в степень': operator.pow,
}


def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def choice_of_operation(request):
    print(request)
    context = {
        'operators': ACTIONS.keys
    }
    return render(request, 'operators.html', context)


def enter_numbers(requests, selected_operation):
    return render(requests, 'calculate.html')


def calculate(request, selected_operation):
    if is_number(request.GET['num1']) and is_number(request.GET['num2']):
        num1, num2 = float(request.GET['num1']), float(request.GET['num2'])
        if selected_operation in ACTIONS:
            to_do = ACTIONS.get(selected_operation)
            if num2 == 0 and to_do == operator.truediv:
                result = 'На ноль делить нельзя'
            else:
                result = to_do(num1, num2)
    else:
        result = 'Введи числа для рассчета!'

    context = {
        'result': result
    }
    return render(request, 'result.html', context)

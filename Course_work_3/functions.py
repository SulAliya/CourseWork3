import json
from datetime import datetime

def load_operations():
    '''
    Загружает список выполненных операций из файла
    :return: studs
    '''
    with open('operations.json', 'r', encoding='utf-8') as file:
        operations_list = json.load(file)
    return operations_list


def executed_operations(operations_list):
    """
    Загружает список по значению EXECUTED.
    :param operations_list:
    :return:
    """
    executed_operations = []
    for state in operations_list:
        if state.get("state") == "EXECUTED":
            executed_operations.append(state)
    return executed_operations


def sorted_list(executed_operations):
    """
    Загружает список, остортированный по дате.
    :return:
    """
    sort_list = sorted(executed_operations, key=lambda k: k['date'], reverse=True)
    return sort_list


def five_operations_from_list(sort_list):
    """
    Загружает 5 значений из списка.
    :param sort_list:
    :return:
    """
    five_operations= sort_list[0:5]
    return five_operations


def get_type(five_operations):
    '''
    Загружает тип операции.
    :return:
    '''

    type_of_operation = five_operations["description"]
    return type_of_operation


def get_amount(operation):
    """
    Загружает сумму операции.
    :param operation:
    :return:
    """

    amount = operation["operationAmount"]["amount"]
    return amount


def get_currency(operation):
    """
    Загружает валюту операции.
    :param operation:
    :return:
    """
    currency = operation["operationAmount"]["currency"]["name"]
    return currency


def transaction_date(operation):
    """
    Загружает дату в формате ДД.ММ.ГГГГ.
    :param operation:
    :return:
    """
    transfer_date = operation["date"]
    PATTERN_IN = "%Y-%m-%dT%H:%M:%S.%f"  # формат даты из списка
    PATTERN_OUT = "%d.%m.%Y" #необходимый формат
    date = datetime.strptime(transfer_date, PATTERN_IN)
    correct_transfer_date = datetime.strftime(date, PATTERN_OUT)
    return correct_transfer_date


def get_payment_system(operation):
    """
    Загружает платежную систему карты отправителя.
    :param operation:
    :return:
    """
    operation_from = operation.setdefault("from", "")
    payment_system = []
    for word in operation_from:
        if word.isdigit():
            continue
        else:
            payment_system.append(word)
    payment_system = "".join(payment_system)
    return payment_system


def get_card_number(operation):
    """
    Загружает номер карты отправителя.
    :param operation:
    :return:
    """
    operation_from = operation.setdefault("from", "")
    card_number = []
    for word in operation_from:
        if word.isdigit():
            card_number.append(word)
        else:
            continue
    card_number = "".join(card_number)
    return card_number


def get_disquised_card_number(card_number):
    """
    Загружает номер карты в зашифрованном виде.
    :param card_number:
    :return:
    """
    a = len(card_number)
    disquised_card_number = ''
    for i in range(a):
        if i >=6 and i < (a - 4):
            disquised_card_number += "*"
        else:
            disquised_card_number += card_number[i]
    return disquised_card_number


def split_card_number(disquised_card_number):
    """
    Загружает зашифрованный номер карты разбитого по блокам по 4 цифры, разделенных пробелом.
    :param disquised_card_number:
    :return:
    """
    a = len(disquised_card_number)
    split_card_number = [disquised_card_number[i:i + 4] for i in range(0, a, 4)]
    sender_card_number = ' '.join(split_card_number)
    return sender_card_number


def get_disguised_account(operation):
    """
    Загружает замаскированный счёт получателя.
    :param operation:
    :return:
    """
    operation_to = operation["to"]
    disguised_account = ('*' * len(operation_to[:2]) + operation_to[-4:])
    return disguised_account


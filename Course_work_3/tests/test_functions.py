import pytest
from Course_work_3.course_work_3.functions import *


@pytest.fixture
def src():
    return {'id': 782295999, 'state': 'EXECUTED', 'date': '2019-09-11T17:30:34.445824',
            'operationAmount': {'amount': '54280.01', 'currency': {'name': 'USD', 'code': 'USD'}},
            'description': 'Перевод организации', 'from': 'Счет 24763316288121894080',
            'to': 'Счет 96291777776753236930'}

def test_get_currency(src):
    assert get_currency(src) =='USD'


def test_get_amount(src):
    assert get_amount(src) == '54280.01'


def test_transaction_date(src):
    assert transaction_date(src) == '11.09.2019'


def test_get_disquised_card_number(src):
    assert get_disquised_card_number('247633**********4080') == '247633**********4080'


def test_split_card_number(src):
    assert split_card_number('247633**********4080') == '2476 33** **** **** 4080'


def test_get_type(src):
    assert get_type(src) == 'Перевод организации'


def test_get_disguised_account(src):
    assert get_disguised_account(src) == '**6930'


def test_get_card_number(src):
    get_card_number(src) == '24763316288121894080'


def test_get_payment_system(src):
    get_payment_system(src) == 'Счет'











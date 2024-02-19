from Course_work_3.course_work_3 import functions

operations_list= functions.load_operations()
executed_operations = functions.executed_operations(operations_list)

sort_list = functions.sorted_list(executed_operations)
five_operations = functions.five_operations_from_list(sort_list)

for operation in five_operations:
    correct_transfer_date = functions.transaction_date(operation)
    type_of_operation = functions.get_type(operation)
    payment_system = functions.get_payment_system(operation)
    card_number = functions.get_card_number(operation)
    disquised_card_number = functions.get_disquised_card_number(card_number)
    disguised_account = functions.get_disguised_account(operation)
    amount = functions.get_amount(operation)
    currency = functions.get_currency(operation)
    sender_card_number = functions.split_card_number(disquised_card_number)
    print(f'{correct_transfer_date} {type_of_operation}\n{payment_system}{sender_card_number} -> {disguised_account}\n{amount} {currency}\n')

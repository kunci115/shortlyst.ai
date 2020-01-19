def insert_coin(state, current_coin, new_coin):
    new_coin = int(new_coin)
    valid_coin = [10, 50, 100, 500]
    if new_coin not in valid_coin:
        print('insert only {}'.format(valid_coin))
        return True, current_coin

    current_coin = int(current_coin) + int(new_coin)
    print('Accepted')
    return True, current_coin


def purchase(state, current_coin, items, item_id):
    if items[item_id][2] < 1:
        print('Stock empty')
        return True, current_coin, items

    if current_coin < items[item_id][1]:
        print('Coin {} - Item {}'.format(current_coin, items[item_id][1]))
        print('Please Insert more coin')
        return True, current_coin, items
    else:
        print('Delivering {}'.format(items[item_id][0]))
        current_coin = current_coin - items[item_id][1]
        items[item_id][2] = items[item_id][2] - 1
        state = False
        return state, current_coin, items


def vending_machine():
    # name, price, stock
    items = {1: ['Canned coffee', 120, 5], 2: ['Water PET bottle', 100, 0], 3: ['Sport drinks', 150, 1]}

    current_coin = 0
    state = True
    while state is True:
        user_input = input("Please Choose 1-5: ").split(' ')

        if user_input[0] == '1':
            new_coin = user_input[1]
            state, current_coin = insert_coin(state, current_coin, new_coin)
        elif user_input[0] == '2':
            item_id = int(user_input[1])
            state, current_coin, items = purchase(state, current_coin, items, item_id)
        elif user_input[0] == '4':
            print('Return coins')
            state = False

    if current_coin > 0:
        print('Your change is {}'.format(current_coin))

    print(items)
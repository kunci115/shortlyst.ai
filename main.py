from display import print_display


def insert_coin(state, current_coin, new_coin):
    new_coin = int(new_coin)
    valid_coin = [10, 50, 100, 500]
    if new_coin not in valid_coin:
        print('insert only {}'.format(valid_coin))
        return True, current_coin

    current_coin = int(current_coin) + int(new_coin)
    print('Accepted')
    return True, current_coin


def choose_item(state, current_coin, items, item_id, current_purchase):
    if items[item_id][2] < 1:
        print('Stock empty')
        return True, items, current_purchase

    current_total = 0
    for c in current_purchase:
        current_total = current_total + items[c][1]

    need = (items[item_id][1] + current_total)

    if current_coin < need:
        print('Coin {} - Need {}'.format(current_coin, need))
        print('Please Insert more coin')
        return True, items, current_purchase
    else:
        print('Add {}'.format(items[item_id][0]))
        current_purchase.append(item_id)
        items[item_id][2] = items[item_id][2] - 1
        return True, items, current_purchase


def get_item(state, items, current_coin, current_purchase):
    current_total = 0
    for c in current_purchase:
        current_total = current_total + items[c][1]

    return True, (current_coin - current_total), []


def return_coin(items, current_purchase):
    for c in current_purchase:
        items[c][2] = items[c][2] + 1

    return False, items, 0


def vending_machine():
    # name, price, stock
    items = {1: ['Canned coffee', 120, 5], 2: ['Water PET bottle', 100, 0], 3: ['Sport drinks', 150, 1]}

    current_coin = 0
    current_purchase = []
    state = True
    while state:
        print_display()
        user_input = input("Please Choose 1-5: ").split(' ')

        if user_input[0] == '1':
            new_coin = user_input[1]
            state, current_coin = insert_coin(state, current_coin, new_coin)
        elif user_input[0] == '2':
            item_id = int(user_input[1])
            state, items, current_purchase = choose_item(state, current_coin, items, item_id, current_purchase)
        elif user_input[0] == '3':
            print('Get items')
            state, current_coin, current_purchase = get_item(state, items, current_coin, current_purchase)
        elif user_input[0] == '4':
            print('Return coins')
            state, items, current_coin = return_coin(items, current_purchase)
        elif user_input[0] == '5':
            print('Get returned coins')
            if current_coin > 0:
                print('Your change is {}'.format(current_coin))
            state = False

    print('Stock is {}'.format(items))


print('START')
vending_machine()
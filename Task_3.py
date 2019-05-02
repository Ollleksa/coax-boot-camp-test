# Create console application that return car's price for inputed car's name.
# When user enter car's name you should look for it in the file.
#
#     1) If car with the name is found you need show user its price (USD)
#
#     2) If car with the name is not found you need to ask user to input car's price and currency for that price
#     (possible currency values are USD, EUR, GBP); then show user price of that car in USD
#     and append the car with the price into car's list in file.


CONVERT_RATES = {'USD': 1.0, 'EUR': 1.12, 'GBR': 1.31, }


def main():
    name = input('Please type name of the car to find it price:\n')

    price = find_car_price(name)
    if price:
        print('{} cost {} USD'.format(name, price))
    else:
        name, price, currency = collect_data(name)
        add_new_car(name, price, currency)
        print('{} was added to out database.'.format(name))


def find_car_price(name):
    try:
        with open("cars.dat","r") as cars_db:
            for car in cars_db.readlines():
                if car.split()[0] == name:
                    return car.split()[1]
    except FileNotFoundError:
        pass


def collect_data(name):
    print('Car "{}" wasnt found in our database. We need some info to add it.'.format(name))
    price = get_price()
    currency = get_currency()
    return name, price, currency


def get_price():
    while True:
        try:
            price = float(input('Price of the car:\n'))
            if price > 0:
                return price
            else:
                print('Price should be greater then zero.')
        except ValueError:
            print('Price should be a number.')


def get_currency():
    while True:
        currency = input('What currency (USD, EUR, GBR)?\n')
        if currency in CONVERT_RATES:
            return currency
        else:
            print('Please submit a valid currency.')


def add_new_car(name, price, currency):
    price_in_usd = price * CONVERT_RATES[currency]
    with open("cars.dat", "a") as cars_db:
        cars_db.write('{} {}\n'.format(name, str(price_in_usd)))


if __name__ == '__main__':
    main()
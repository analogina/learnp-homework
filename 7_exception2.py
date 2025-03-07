"""

Домашнее задание №1

Исключения: приведение типов

* Перепишите функцию discounted(price, discount, max_discount=20)
  из урока про функции так, чтобы она перехватывала исключения,
  когда переданы некорректные аргументы.
* Первые два нужно приводить к вещественному числу при помощи float(),
  а третий - к целому при помощи int() и перехватывать исключения
  ValueError и TypeError, если приведение типов не сработало.
    
"""

# def discounted(price, discount, max_discount=20):
#     price = abs(price)
#     discount = abs(discount)
#     max_discount = abs(max_discount)
#     if max_discount >= 100:
#         raise ValueError('Слишком большая максимальная скидка')
#     if discount >= max_discount:
#         return price
#     else:
#         return price - (price * discount / 100)

def discounted(price, discount, max_discount=20):
    try:
        price = float(price)
        discount = float(discount)
        max_discount = int(max_discount)
    except(ValueError, TypeError):
        print('Приведение не сработало.')
        return

    if discount >= 100:
        raise ValueError('Слишком большая максимальная скидка')

    if discount >= max_discount:
        price_with_discount = price

    else:
        price_with_discount = price - (price * discount / 100)
    return price_with_discount
    
def main():
    print(discounted(100, 2))
    print(discounted(100, "3"))
    print(discounted("100", "4.5"))
    print(discounted("five", 5))
    print(discounted("сто", "десять"))
    print(discounted(100.0, 5, "10"))


if __name__ == "__main__":
  main()
    # print(discounted(100, 2))
    # print(discounted(100, "3"))
    # print(discounted("100", "4.5"))
    # print(discounted("five", 5))
    # print(discounted("сто", "десять"))
    # print(discounted(100.0, 5, "10"))

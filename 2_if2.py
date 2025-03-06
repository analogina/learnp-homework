"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def check_func(str1, str2):
  if type(str1) != str or type(str2) != str:
    return 0
  elif (str1 == str2):
    return 1
  elif (str2 == 'learn'):
    return 3
  elif (len(str1) > len(str2)):
    return 2
  return -1
    
def main():

  res = check_func(1, 4)
  print(f"С двумя цифрами результат: {res}")
  res = check_func("string", "string")
  print(f"С двумя одинаковыми строчками. Результ: {res}")
  res = check_func("python", "learn")
  print(f"Вторая строчка -'learn'.Результат: {res}")
  res = check_func("long_string", "string")
  print(f"Первая строчка длиннее второй. Результат: {res}")

  for a in range(3):
    string1 = input("Введите первую строку: ")
    string2 = input("Введите вторую строку: ")
    res = check_func(string1, string2)
    print(f"Результатпроверки функции: {res}")

if __name__ == "__main__":
  main()

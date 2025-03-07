"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
    user_saw = ""
    while user_saw != "Хорошо":
        try:
          user_saw = input("Как дела? ")
        except KeyboardInterrupt:
          print(' Пока!')
          break

        # if user_saw == "Хорошо":
        #   break
    else:
        return
    
if __name__ == "__main__":
    hello_user()


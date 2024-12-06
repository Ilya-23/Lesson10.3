import threading
import random
import time
class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            sym1 = random.randint(50, 500)
            print(f'Запрос на {sym1}.')
            if self.balance >= 500 and  self.lock.locked() is True:
                self.lock.release()
            self.balance += sym1
            time.sleep(0.001)
            print(f'Пополнение: {sym1}. Баланс: {self.balance}.')

    def take(self):
        for i in range(100):
            sym2 = random.randint(50, 500)
            print(f'Запрос на {sym2}.')
            if sym2 <= self.balance:
                self.balance -= sym2
                print(f'Снятие: {sym2}. Баланс: {self.balance}.')
            else:
                print('Запрос отклонён, недостаточно средств.')
                self.lock.acquire()

bk = Bank()


th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')





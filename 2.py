""" Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.
Обоснуйте выбор парадигм. """




class MultiplicationTable:
    def __init__(self, n):
        self.n = n

    def print_table(self):
        for i in range(1, self.n+1):
            print(f'{i*self.n}')


def main():
    n = int(input("Введите число n: "))
    table = MultiplicationTable(n)
    table.print_table()

if __name__ == "__main__":
    main()

""" ООП позволяет структурировать код, делая его более понятным и поддерживаемым.
 """



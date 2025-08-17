#Задание 1
#Перед тобой класс OnlineSalesRegisterCollector. Он отвечает за работу онлайн-кассы.
#Класс содержит:
#список name_items с перечнем товаров в чеке;
#переменную number_items с количеством товаров в чеке;
#cловарь item_price, где перечислены товары магазина и их стоимость;
#словарь tax_rate, где записана налоговая ставка на товары. Она составляет 10% или 20% от стоимости.
#Твоя задача — добавить в класс методы. Из них — девять обязательных и один дополнительный.

import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}
    
    #1. Напиши геттеры
    @property
    def name_items(self):
        return self.__name_items

    @property
    def number_items(self):
        return self.__number_items
    
    #2. Добавь товар в чек
    def add_item_to_cheque(self, name):
        if len(name) == 0 or len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        else:
            if name not in self.__item_price:
                raise NameError('Позиция отсутствует в товарном справочнике')
            else:
                self.__name_items.append(name)
                self.__number_items += 1

    #3. Удали товар из чека
    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        else:
            self.__name_items.remove(name)
            self.__number_items -= 1
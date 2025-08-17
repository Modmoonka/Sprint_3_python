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

    #4. Посчитай общую стоимость товаров
    def check_amount(self):
        total = []
        for i in self.__name_items:
            total.append(self.__item_price[i])
        amount = sum(total)
        if self.__number_items > 10:
            amount = amount * 0.9
        return amount
    
    #5. Вычисли НДС для товаров со ставкой 20%
    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []
        for i in self.__name_items:
            if self.__tax_rate[i] == 20:
                twenty_percent_tax.append(i)
                total.append(self.__item_price[i])

        total_amount = sum(total)
        if self.__number_items > 10:
            total_amount *= 0.9

        check_amount = total_amount * 0.2
        return check_amount
    
    #6. Вычисли НДС для товаров со ставкой 10%
    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []
        for i in self.__name_items:
            if self.__tax_rate[i] == 10:
                ten_percent_tax.append(i)
                total.append(self.__item_price[i])

        total_amount = sum(total)
        if self.__number_items > 10:
            total_amount *= 0.9

        check_amount = total_amount * 0.1
        return check_amount
    
    #7. Посчитай общую сумму налогов
    def total_tax(self):
        return self.ten_percent_tax_calculation() + self.twenty_percent_tax_calculation()
    
    #8. Верни номер телефона покупателя
    @staticmethod
    def get_telephone_number(telephone_number):
        if not isinstance(telephone_number, int):
            raise ValueError('Необходимо ввести цифры')
        if len(telephone_number) > 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        return f'+7{telephone_number}'


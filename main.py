import random

"""
Я створив програму шифрування(class Encoder) і дешифрування(class Decoder) тексту
за алгоритмом шифру Цезаря.
Програма працює тільки з англійськими літерами.
Шифруються тільки літери, інші символи залишаються без змін.
При шифруванні літери зміщуються вправо на випадкове число від 1 до 9
і це зміщення записується в ключ шифрування(self.__decodeKey).
Щоб отримати ключ, потрібо ввести пароль(self.__password): itstep
Пароль можна спробувати тільки 3 рази.
При дишифруванні літери зміщуються вліво згідно ключа.
Без ключа шифрування декодувати текст правільно неможливо.
Всі поля класів приховані, щоб неможливо було підлаштувати параметри ззовні.
"""
abc_lower = 'abcdefghijklmnopqrstuvwxyz'
abc_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Encoder:
    def __init__(self, text):
        self.__text = text
        self.__tryCounter = 0
        self.__password = 'itstep'
        self.__encodeText = ''
        self.__decodeKey = ''

    def encode(self):
        for i in self.__text:
            if i.isalpha():
                rand = random.randint(1, 9)
                self.__decodeKey += str(rand)
                if i.islower(): self.__encodeText += abc_lower[(abc_lower.find(i) + rand) % 26]
                else: self.__encodeText += abc_upper[(abc_upper.find(i) + rand) % 26]
            else:
                self.__encodeText += i
                self.__decodeKey += '0'
        while self.__tryCounter < 3:
            temp = input('Введіть пароль: ')
            if temp == self.__password: return [self.__encodeText, self.__decodeKey]
            self.__tryCounter += 1
            print('Пароль - невірний. У Вас залишилось %s спроби' % (3 - self.__tryCounter))
        return [self.__encodeText, '']

class Decoder:
    def __init__(self, decText, decKey):
        self.__text = decText
        self.__decodeText = ''
        self.__decodeKey = decKey

    def decode(self):
        if len(self.__text) != len(self.__decodeKey): return 'У Вас невірний ключ'
        for i in range(len(self.__text)):
            if self.__text[i].isalpha():
                if self.__text[i].islower(): self.__decodeText += abc_lower[(abc_lower.find(self.__text[i]) - int(self.__decodeKey[i])) % 26]
                else: self.__decodeText += abc_upper[(abc_upper.find(self.__text[i]) - int(self.__decodeKey[i])) % 26]
            else: self.__decodeText += self.__text[i]
        return self.__decodeText

text = 'Hello world!!!'
print('Текст перед кодуванням: "%s"' % text)
text1 = Encoder(text)
encoded = text1.encode()
print('Закодований текст: "%s"' % encoded[0])
print('Ключ кодування: "%s"' % encoded[1])
print('-' * 30)
text2 = Decoder(encoded[0], encoded[1])
print('Текст після розкодування: "%s"' % text2.decode())
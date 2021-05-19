# Задание 1:
# Напишите Программу - которая работает по принципу алгоритма Шифр Цезаря.
# Нужно создать класс состоящий из 2 методов:
# 1. Метод который ШИФРУЕТ данные.
# 2. Метода который ДЕШИФРУЕТ эти же данные.
# Представим что ваш метод получает слово состоящее из ЛЮБЫХ символов.
# Ваш 1-й метод должен вернуть зашифрованную строку.
# Алгоритм Шифрования: ASCII позиция + 7.
# Алгоритм Дешифровки: Обратная операция Алгоритма Шифрования.



class Cipher:
    def init(self, text):
        self.text = text

    def decrypt(self,text):
        result = ""
        # traverse text
        for i in range(len(text)):
            char = text[i]
            # Encrypt uppercase characters
            if (char.isupper()):
                result += chr((ord(char) - 7))
            # Encrypt lowercase characters
            else:
                result += chr((ord(char) - 7))
        return result


    def encrypt(self):
        result = ""
    # traverse text
        for i in range(len(self.text)):
            char = self.text[i]
            # Encrypt uppercase characters
            if (char.isupper()):
                result += chr((ord(char) + 7))
            # Encrypt lowercase characters
            else:
                result += chr((ord(char) + 7))
        return result

    def str(self):
        cipherText = self.encrypt()
        return f'Исходный текст:{self.text}\nТекст после шифровки:{cipherText}\nДешифрованный текст:{self.decrypt(cipherText)} '
text = input('Введите текст: ')
obj = Cipher(text)
print(str(obj))
import pyAesCrypt


password = input('Введите пароль для шифрования файла: ')

#encrypt

pyAesCrypt.encryptFile('data.txt', 'data.txt.aes', password)
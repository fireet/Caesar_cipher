
alphabet = [x for x in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя']


def test_lang(crypt_text, data):
    for x in crypt_text:
        x = x.lower()
        if x in data:
            return True


def crypt_or_decrypt_text(crypt_text:str, data:list, key:int, crypt_or_decrypt:bool = True) -> str:
    crypt = ''
    data_len = len(data)
    if not crypt_or_decrypt:
        key = -key

    for x in crypt_text:
        char = x
        x = x.lower()

        try:

            ind = data.index(x) + key
            if -data_len>ind:
                while -data_len > ind:
                    ind = ind + data_len

            elif ind >= data_len:
                while ind >= data_len:
                    ind = ind - data_len

            value = data[ind]

        except ValueError:
            value = x

        if char.isupper():
            value = value.upper()
        crypt += value

    return crypt


if __name__ == '__main__':

    text = 'Тулезх!'
    if test_lang(text, alphabet):
        answer = crypt_or_decrypt_text(text, alphabet, 3, crypt_or_decrypt = False)
        print(answer)
    else:
        print('need another data')
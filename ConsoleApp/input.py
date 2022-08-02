
class Input:
    def entry(self, info='[*]> '):
        try:
            data = input(info).strip()
        except Exception as e:
            print(e)
            data = self.entry(info)
        return data

    def entry_id(self):
        data = input('[Выберите адрес](0): ').rstrip()
        try:
            data = int(data)
            return data
        except Exception as e:
            print(e)
            return 0

    def get_data(self, datab):
        print('[Вход]')
        token = self.entry('[*] Введите API_KEY: ')
        secret = self.entry('[*] Введите SECRET_KEY: ')
        print()
        datab.change_data(token, secret)
        return token, secret

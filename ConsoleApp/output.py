
class Output:
    def DataError(self):
        print('Error: API_KEY или SECRET_KEY введены неправильно')

    def not_found(self):
        print('Ничего не найдено')

    def hello(self):
        print('Dadata.ru Console application', '\n')

    def output_geo(self, result):
        data = [
            result['value'],
            'Широта: ' + result.get('geo_lat', 'None'),
            'Долгота: ' + result.get('geo_lon', 'None')]
        print(*data, sep='\n')

    def get_value(self, result, entry):
        n = len(result)
        if n > 1:
            for i in range(n):
                print(i, result[i]['value'], sep=' - ')
            id_address = entry.entry_id()
            if 0 <= id_address < n:
                self.output_geo(result[id_address])
        elif n == 1:
            self.output_geo(result[0])
        else:
            self.not_found()

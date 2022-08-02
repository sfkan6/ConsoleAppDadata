import httpx
from dadata import Dadata  # https://github.com/hflabs/dadata-py
from .manager_db import DataB


class ToApiDadata:
    def __init__(self, entry, output):
        self.language = 'ru'
        self.entry = entry
        self.output = output
        self.datab = DataB()

        token, secret = self.get_profile()
        self.dadata = Dadata(token, secret)

    def get_profile(self):
        data = self.datab.return_data()
        if data:
            return data[0], data[1]
        else:
            return self.entry.get_data(self.datab)

    def change_profile(self):
        token, secret = self.entry.get_data(self.datab)
        self.dadata = Dadata(token, secret)
        self.output.hello()

    def change_language(self, query):
        if 'en' == query:
            self.language = 'en'
            return True
        elif 'ru' == query:
            self.language = 'ru'
            return True
        return False

    def search_address(self, query):
        try:
            result = self.dadata.suggest('address', query, language=self.language)
        except httpx.HTTPStatusError:
            return self.output.DataError()

        self.output.get_value(result, self.entry)

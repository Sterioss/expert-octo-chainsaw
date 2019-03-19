import requests


class Badger:

    def __init__(self, firstname, lastname):
        self.firstName = firstname
        self.lastName = lastname
        self.__endpoint = 'http://10.3.1.56:8080'
        self.__timeout = 2

    def __getlogin(self):
        try:
            r = requests.post(self.__endpoint + '/login/',
                              data={'action': 'tryConnect',
                                    'userMail': self.firstName + '.' + self.lastName + '@uha.fr',
                                    'password': 'uha'}, timeout=self.__timeout).json()
        except requests.exceptions.RequestException as e:
            print(e)
            raise TimeoutError
        else:
            return r

    def __gettoken(self):
        try:
            r = self.__getlogin()['token']
        except TypeError as e:
            print(e)
        else:
            __token = r
            return r

    def __userid(self):
        try:
            r = requests.post(self.__endpoint + '/user/',
                              data={'token': self.__gettoken(),
                                    'action': 'getIdUser',
                                    'userName': self.lastName + " " + self.firstName,
                                    }, timeout=self.__timeout)
        except requests.exceptions.RequestException as e:
            print(e)
        else:
            return r

    def setpresence(self, presence):
        try:
            badger = requests.post(self.__endpoint + '/badger/',
                                   data={'token': self.__gettoken(),
                                         'action': 'setPresence',
                                         'id_user': self.__userid(),
                                         'presence': presence,
                                         }, timeout=self.__timeout).json()
        except TypeError as e:
            print(e)
            return 1
        except requests.exceptions.RequestException as e:
            print(e)
            return 1
        except TimeoutError:
            return 1
        else:
            print(badger['message'])
            return badger

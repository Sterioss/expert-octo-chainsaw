import requests


class Badger:

    def __init__(self, firstname, lastname):
        self.firstName = firstname
        self.lastName = lastname
        self.__endpoint = 'http://10.3.1.56:8080'
        self.__timeout = 1

    def __getlogin(self):
        try:
            r = requests.post(self.__endpoint + '/login/',
                              data={'action': 'typeLogin', 'userMail': self.firstName + '.' + self.lastName + '@uha.fr',
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
            return r

    def __username(self):
        try:
            r = self.__getlogin()['userName']
        except TypeError as e:
            print(e)
        else:
            return r

    def __userid(self):
        try:
            r = requests.post(self.__endpoint + '/user/',
                              data={'action': 'getIdUser',
                                    'userName': self.__username(),
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
                                         }, timeout=self.__timeout)
        except TypeError as e:
            print(e)
            return 1
        except requests.exceptions.RequestException as e:
            print(e)
            return 1
        except TimeoutError:
            return 1
        else:
            return badger

import requests


class Badger:
    __endpoint = 'http://145.239.32.254:8080'
    __timeout = 3

    def __init__(self, firstname, lastname, password):
        self.firstName = firstname
        self.lastName = lastname
        self.password = password

    def __getlogin(self):
        try:
            login = requests.post(self.__endpoint + '/login/',
                                  data={'action': 'tryConnect',
                                        'userMail': self.firstName + '.' + self.lastName + '@uha.fr',
                                        'password': 'UHA' + self.password}, timeout=self.__timeout).json()
        except requests.exceptions.RequestException as e:
            print(e)
            raise TimeoutError
        else:
            return login

    def __gettoken(self):
        try:
            r = self.__getlogin()['token']
        except TypeError as e:
            print(e)
        else:
            return r

    def __getuserid(self):
        try:

            userid = requests.post(self.__endpoint + '/user/',
                                   data={'token': self.__gettoken(),
                                         'action': 'getIdUser',
                                         'userName': self.lastName + " " + self.firstName,
                                         }, timeout=self.__timeout).json()['user']
        except requests.exceptions.RequestException as e:
            print(e)
        else:

            return userid

    def setpresence(self, presence):
        try:
            if presence == '1':
                badger = requests.post(self.__endpoint + '/badger/',
                                       data={'token': self.__gettoken(),
                                             'action': 'setPresence',
                                             'id_user': self.__getuserid()
                                             }, timeout=self.__timeout).json()
            elif presence == '0':
                badger = requests.post(self.__endpoint + '/badger/',
                                       data={'token': self.__gettoken(),
                                             'action': 'setPresence',
                                             'id_user': self.__getuserid(),
                                             'presence': '1'
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
            print(badger['message'] if 'message' in badger else "Already logged in or out. " + badger['success'])
            return badger

import request


class Badger:

    def __init__(self, firstname, lastname):
        self.firstName = firstname
        self.lastName = lastname
        self.__endpoint = 'http://10.3.1.56:8080/'

    def __getlogin(self):
        return request.POST(self.__endpoint + '/login/',
                            data={'action': 'typeLogin', 'userMail': self.firstName + '.' + self.lastName + '@uha.fr',
                                  'password': 'uha'})

    def __gettoken(self):
        return self.__getlogin()['token']

    def __username(self):
        return self.__getlogin()['userName']

    def __userid(self):
        return request.POST(self.__endpoint + '/user/',
                            data={'action': 'getIdUser',
                                  'userName': self.__username(),
                                  })

    def setpresence(self, presence):
        badger = request.POST(self.__endpoint + '/badger/',
                                data={'token': self.__gettoken(),
                                      'action': 'setPresence',
                                      'id_user': self.__userid(),
                                      'presence': presence,
                                      })

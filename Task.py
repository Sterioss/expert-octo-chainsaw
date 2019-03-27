from badger import Badger
import time


class Task:
    def __init__(self, on, off, firstname, lastname, password):
        self.on = on
        self.off = off
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        self.__off()
        self.__on()

    def __seton(self, firstname, lastname, password):
        onbadger = Badger(firstname, lastname, password)
        return onbadger.setpresence("1")

    def __setoff(self, firstname, lastname, password):
        offbadger = Badger(firstname, lastname, password)
        return offbadger.setpresence("0")

    def __on(self):
        if time.strftime("%H:%M") == self.on:
            self.__seton(self.firstname, self.lastname, self.password)

    def __off(self):
        if time.strftime("%H:%M") == self.off:
            self.__setoff(self.firstname, self.lastname, self.password)

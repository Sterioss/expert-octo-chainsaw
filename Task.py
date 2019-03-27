import randomTime
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

    @staticmethod
    def __seton(firstname, lastname, password):
        onbadger = Badger(firstname, lastname, password)
        return onbadger.setpresence("1")

    @staticmethod
    def __setoff(firstname, lastname, password):
        offbadger = Badger(firstname, lastname, password)
        return offbadger.setpresence("0")

    def __on(self):
        if time.strftime("%H:%M") == self.on:
            self.__seton(self.firstname, self.lastname, self.password)

    def __off(self):
        if time.strftime("%H:%M") == self.off:
            self.__setoff(self.firstname, self.lastname, self.password)

    def __newrandom(self):
        if time.strftime("%H:%M") == "00:00":
            randomTime.RandomTime().randomizer()

from badger import Badger
import time


class Task:
    def __init__(self, on, off, firstname, lastname):
        self.on = on
        self.off = off
        self.firstname = firstname
        self.lastname = lastname
        self.__off()
        self.__on()

    def __seton(self, firstname, lastname):
        onbadger = Badger(firstname, lastname)
        return onbadger.setpresence(1)

    def __setoff(self, firstname, lastname):
        offbadger = Badger(firstname, lastname)
        return offbadger.setpresence(0)

    def __on(self):
        if time.strftime("%H:%M") == self.on:
            self.__seton(self.firstname, self.lastname)
            return 0
        else:
            return 1

    def __off(self):
        if time.strftime("%H:%M") == self.off:
            self.__setoff(self.firstname, self.lastname)
            return 0
        else:
            return 1

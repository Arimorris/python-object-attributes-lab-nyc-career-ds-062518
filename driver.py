class Driver:

    def greet_passenger(self):
        return ("Hello! I'll be your driver today. My name is {} {}" .format(self._first,  self._last))

    @property
    def first(self):
        return self._first

    @first.setter
    def first(self, name):
        self._first = name

    @property
    def last(self):
        return self._last

    @last.setter
    def last(self, name):
        self._last = name

    @property
    def miles_driven(self):
        return self._miles_driven

    @miles_driven.setter
    def miles_driven(self, mile):
        self._miles_driven = mile

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, rating):
        self._rating = rating

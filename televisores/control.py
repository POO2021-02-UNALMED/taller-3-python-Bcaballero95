
class Control:
    def __init__(self):
        pass

    def turnOn(self):
        self.TV.turnOn()

    def turnOff(self):
        self.TV.turnOff()

    def canalUp(self):
        self.TV.canalUp()

    def canalDown(self):
        self.TV.canalDown()

    def volumenUp(self):
        self.TV.volumenUp()

    def volumenDown(self):
        self.TV.volumenDown()

    def enlazar(self, tv):
        self.TV = tv
        self.TV.setControl(tv)

    def setTV(self, tv):
        self.TV= tv

    def getTv(self):
        return self.TV

    def setCanal(self, n):
        self.TV.setCanal(n)


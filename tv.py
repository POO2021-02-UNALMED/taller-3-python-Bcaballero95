
class TV:
    numTV = 0

    def __init__(self, marca, estado ):
        self._marca = marca
        self._estado = estado
        self._canal = 1
        self._precio = 500
        self._volumen = 1
        TV.numTV += 1

    def setMarca(self, marca ):
        self._marca = marca

    def setControl(self, control ):
        self._control = control

    def setPrecio(self, precio ):
        self._precio = precio

    def setCanal(self, canal ):
        if 1 <= canal <= 120 :
            self._canal = canal

    def setVolumen(self, volumen ):
        if 1 <= volumen <= 7:
            self._volumen = volumen

    def getMarca(self) :
        return self._marca

    def getPrecio (self) :
        return self._precio

    def getCanal (self) :
        return self._canal

    def getVolumen (self) :
        return self._volumen

    @classmethod
    def getNumTV (cls) :
        return cls.numTV

    def turnOn (self, estado) :
        self._estado = estado

    def turnOff (self, estado) :
        self._estado = estado

    def getEstado (self) :
        return self._estado

    def canalUp (self) :
        if 1 <= self._canal < 120 :
            self._canal += 1

    def canalDown (self) :
        if 1 < self._canal <= 120 :
            self._canal -= 1

    def volumeUp(self):
        if 1<= self._volumen < 7:
            self._volumen +=1

    def volumenDown(self):
        if 1< self._volumen <= 7:
            self._volumen -=1


class TV :
    numTV = 0

    def __init__ (self, marca, estado) :
        self._marca = marca
        self._estado = estado
        self._canal = 1
        self._precio = 500
        self._volumen = 1
        TV.numTV += 1

    def setMarca (self, marca) :
        self._marca = marca

    def setControl (self, control) :
        self._control = control

    def setPrecio (self, precio) :
        self._precio = precio

    def setCanal (self, canal) :
        if 1 <= canal <= 120 and self._estado is True:
            self._canal = canal

    def setVolumen (self, volumen) :
        if 1 <= volumen <= 7 and self._estado is True :
            self._volumen = volumen
    @classmethod
    def setNumTV (cls, numTV) :
        cls.numTV = numTV
    def getControl(self):
        return self._control

    def getMarca (self) :
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

    def turnOn (self) :
        self._estado = True

    def turnOff (self) :
        self._estado = False

    def getEstado (self) :
        return self._estado

    def canalUp (self) :
        if 1 <= self._canal < 120 and self._estado is True :
            self._canal += 1

    def canalDown (self) :
        if 1 < self._canal <= 120 and self._estado is True:
            self._canal -= 1

    def volumenUp (self) :
        if 1 <= self._volumen < 7 and self._estado is True :
            self._volumen += 1

    def volumenDown (self) :
        if 1 < self._volumen <= 7 and self._estado is True :
            self._volumen -= 1

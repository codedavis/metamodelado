#PLEASE DO NOT EDIT THIS CODE
#This code was generated using the UMPLE 1.33.0.6934.a386b0a58 modeling language!
# line 39 "model.ump"
# line 81 "model.ump"
import os

class Pago():
    #------------------------
    # MEMBER VARIABLES
    #------------------------
    #Pago Attributes
    #Pago Associations
    #------------------------
    # CONSTRUCTOR
    #------------------------
    def __init__(self, aNumero, aFecha, aMonto, aEstado):
        self._reservas = None
        self._estado = None
        self._Monto = None
        self._fecha = None
        self._numero = None
        self._numero = aNumero
        self._fecha = aFecha
        self._Monto = aMonto
        self._estado = aEstado
        self._reservas = []

    #------------------------
    # INTERFACE
    #------------------------
    def setNumero(self, aNumero):
        wasSet = False
        self._numero = aNumero
        wasSet = True
        return wasSet

    def setFecha(self, aFecha):
        wasSet = False
        self._fecha = aFecha
        wasSet = True
        return wasSet

    def setMonto(self, aMonto):
        wasSet = False
        self._Monto = aMonto
        wasSet = True
        return wasSet

    def setEstado(self, aEstado):
        wasSet = False
        self._estado = aEstado
        wasSet = True
        return wasSet

    def getNumero(self):
        return self._numero

    def getFecha(self):
        return self._fecha

    def getMonto(self):
        return self._Monto

    def getEstado(self):
        return self._estado

    # Code from template association_GetMany 
    def getReserva(self, index):
        aReserva = self._reservas[index]
        return aReserva

    def getReservas(self):
        newReservas = tuple(self._reservas)
        return newReservas

    def numberOfReservas(self):
        number = len(self._reservas)
        return number

    def hasReservas(self):
        has = len(self._reservas) > 0
        return has

    def indexOfReserva(self, aReserva):
        index = (-1 if not aReserva in self._reservas else self._reservas.index(aReserva))
        return index

    # Code from template association_MinimumNumberOfMethod 
    @staticmethod
    def minimumNumberOfReservas():
        return 0

    # Code from template association_AddManyToOne 
    def addReserva1(self, aFechaResera, aCosto, aPelicula, aUsuario):
        from Reserva import Reserva
        return Reserva(aFechaResera, aCosto, aPelicula, aUsuario, self)

    def addReserva2(self, aReserva):
        wasAdded = False
        if (aReserva) in self._reservas :
            return False
        existingPago = aReserva.getPago()
        isNewPago = not (existingPago is None) and not self == existingPago
        if isNewPago :
            aReserva.setPago(self)
        else :
            self._reservas.append(aReserva)
        wasAdded = True
        return wasAdded

    def removeReserva(self, aReserva):
        wasRemoved = False
        #Unable to remove aReserva, as it must always have a pago
        if not self == aReserva.getPago() :
            self._reservas.remove(aReserva)
            wasRemoved = True
        return wasRemoved

    # Code from template association_AddIndexControlFunctions 
    def addReservaAt(self, aReserva, index):
        wasAdded = False
        if self.addReserva(aReserva) :
            if index < 0 :
                index = 0
            if index > self.numberOfReservas() :
                index = self.numberOfReservas() - 1
            self._reservas.remove(aReserva)
            self._reservas.insert(index, aReserva)
            wasAdded = True
        return wasAdded

    def addOrMoveReservaAt(self, aReserva, index):
        wasAdded = False
        if (aReserva) in self._reservas :
            if index < 0 :
                index = 0
            if index > self.numberOfReservas() :
                index = self.numberOfReservas() - 1
            self._reservas.remove(aReserva)
            self._reservas.insert(index, aReserva)
            wasAdded = True
        else :
            wasAdded = self.addReservaAt(aReserva, index)
        return wasAdded

    def delete(self):
        i = len(self._reservas)
        while i > 0 :
            aReserva = self._reservas[i - 1]
            aReserva.delete()
            i -= 1

    def __str__(self):
        return str(super().__str__()) + "[" + "numero" + ":" + str(self.getNumero()) + "," + "Monto" + ":" + str(self.getMonto()) + "," + "estado" + ":" + str(self.getEstado()) + "]" + str(os.linesep) + "  " + "fecha" + "=" + (((self.getFecha().__str__().replaceAll("  ", "    ")) if not self.getFecha() == self else "this") if not (self.getFecha() is None) else "null")

    def addReserva(self, *argv):
        from Reserva import Reserva
        from Date import Date
        if len(argv) == 4 and isinstance(argv[0], Date) and isinstance(argv[1], (float, int)) and isinstance(argv[2], Pelicula) and isinstance(argv[3], Usuario) :
            return self.addReserva1(argv[0], argv[1], argv[2], argv[3])
        if len(argv) == 1 and isinstance(argv[0], Reserva) :
            return self.addReserva2(argv[0])
        raise TypeError("No method matches provided parameters")


#PLEASE DO NOT EDIT THIS CODE
#This code was generated using the UMPLE 1.33.0.6934.a386b0a58 modeling language!
# line 8 "model.ump"
# line 58 "model.ump"
import os

class Pelicula():
    #------------------------
    # MEMBER VARIABLES
    #------------------------
    #Pelicula Attributes
    #Pelicula Associations
    #------------------------
    # CONSTRUCTOR
    #------------------------
    def __init__(self, aNombre, aUrl, aEstado, aDuracion, aAdmin):
        self._reservas = None
        self._admin = None
        self._duracion = None
        self._estado = None
        self._url = None
        self._nombre = None
        self._nombre = aNombre
        self._url = aUrl
        self._estado = aEstado
        self._duracion = aDuracion
        didAddAdmin = self.setAdmin(aAdmin)
        if not didAddAdmin :
            raise RuntimeError ("Unable to create pelicula due to admin. See http://manual.umple.org?RE002ViolationofAssociationMultiplicity.html")
        self._reservas = []

    #------------------------
    # INTERFACE
    #------------------------
    def setNombre(self, aNombre):
        wasSet = False
        self._nombre = aNombre
        wasSet = True
        return wasSet

    def setUrl(self, aUrl):
        wasSet = False
        self._url = aUrl
        wasSet = True
        return wasSet

    def setEstado(self, aEstado):
        wasSet = False
        self._estado = aEstado
        wasSet = True
        return wasSet

    def setDuracion(self, aDuracion):
        wasSet = False
        self._duracion = aDuracion
        wasSet = True
        return wasSet

    def getNombre(self):
        return self._nombre

    def getUrl(self):
        return self._url

    def getEstado(self):
        return self._estado

    def getDuracion(self):
        return self._duracion

    # Code from template attribute_IsBoolean 
    def isEstado(self):
        return self._estado

    # Code from template association_GetOne 
    def getAdmin(self):
        return self._admin

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

    # Code from template association_SetOneToMany 
    def setAdmin(self, aAdmin):
        wasSet = False
        if aAdmin is None :
            return wasSet
        existingAdmin = self._admin
        self._admin = aAdmin
        if not (existingAdmin is None) and not existingAdmin == aAdmin :
            existingAdmin.removePelicula(self)
        self._admin.addPelicula(self)
        wasSet = True
        return wasSet

    # Code from template association_MinimumNumberOfMethod 
    @staticmethod
    def minimumNumberOfReservas():
        return 0

    # Code from template association_AddManyToOne 
    def addReserva1(self, aFechaResera, aCosto, aUsuario, aPago):
        from Reserva import Reserva
        return Reserva(aFechaResera, aCosto, self, aUsuario, aPago)

    def addReserva2(self, aReserva):
        wasAdded = False
        if (aReserva) in self._reservas :
            return False
        existingPelicula = aReserva.getPelicula()
        isNewPelicula = not (existingPelicula is None) and not self == existingPelicula
        if isNewPelicula :
            aReserva.setPelicula(self)
        else :
            self._reservas.append(aReserva)
        wasAdded = True
        return wasAdded

    def removeReserva(self, aReserva):
        wasRemoved = False
        #Unable to remove aReserva, as it must always have a pelicula
        if not self == aReserva.getPelicula() :
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
        placeholderAdmin = self._admin
        self._admin = None
        if not (placeholderAdmin is None) :
            placeholderAdmin.removePelicula(self)
        i = len(self._reservas)
        while i > 0 :
            aReserva = self._reservas[i - 1]
            aReserva.delete()
            i -= 1

    def __str__(self):
        return str(super().__str__()) + "[" + "nombre" + ":" + str(self.getNombre()) + "," + "url" + ":" + str(self.getUrl()) + "," + "estado" + ":" + str(self.getEstado()) + "]" + str(os.linesep) + "  " + "duracion" + "=" + str((((self.getDuracion().__str__().replaceAll("  ", "    ")) if not self.getDuracion() == self else "this") if not (self.getDuracion() is None) else "null")) + str(os.linesep) + "  " + "admin = " + ((format(id(self.getAdmin()), "x")) if not (self.getAdmin() is None) else "null")

    def addReserva(self, *argv):
        from Reserva import Reserva
        if len(argv) == 4 and isinstance(argv[0], Date) and isinstance(argv[1], (float, int)) and isinstance(argv[2], Usuario) and isinstance(argv[3], Pago) :
            return self.addReserva1(argv[0], argv[1], argv[2], argv[3])
        if len(argv) == 1 and isinstance(argv[0], Reserva) :
            return self.addReserva2(argv[0])
        raise TypeError("No method matches provided parameters")

    def imprimir_atributos(self):
        print(f"Nombre: {self._nombre}, URI:{self._url}, Estado:{self._estado}, Duracion:{self._duracion}")
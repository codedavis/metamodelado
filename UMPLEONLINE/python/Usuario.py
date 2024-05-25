#PLEASE DO NOT EDIT THIS CODE
#This code was generated using the UMPLE 1.33.0.6934.a386b0a58 modeling language!
# line 29 "model.ump"
# line 74 "model.ump"
import os

class Usuario():
    #------------------------
    # MEMBER VARIABLES
    #------------------------
    #Usuario Attributes
    #Usuario Associations
    #------------------------
    # CONSTRUCTOR
    #------------------------
    def __init__(self, aIdentificacion, aNombre, aApellidos, aFechaNacimiento, aTipoIdentificacion):
        self._tipoIdentificacion = None
        self._reservas = None
        self._fechaNacimiento = None
        self._apellidos = None
        self._nombre = None
        self._identificacion = None
        self._identificacion = aIdentificacion
        self._nombre = aNombre
        self._apellidos = aApellidos
        self._fechaNacimiento = aFechaNacimiento
        self._reservas = []
        didAddTipoIdentificacion = self.setTipoIdentificacion(aTipoIdentificacion)
        if not didAddTipoIdentificacion :
            raise RuntimeError ("Unable to create usuario due to tipoIdentificacion. See http://manual.umple.org?RE002ViolationofAssociationMultiplicity.html")

    #------------------------
    # INTERFACE
    #------------------------
    def setIdentificacion(self, aIdentificacion):
        wasSet = False
        self._identificacion = aIdentificacion
        wasSet = True
        return wasSet

    def setNombre(self, aNombre):
        wasSet = False
        self._nombre = aNombre
        wasSet = True
        return wasSet

    def setApellidos(self, aApellidos):
        wasSet = False
        self._apellidos = aApellidos
        wasSet = True
        return wasSet

    def setFechaNacimiento(self, aFechaNacimiento):
        wasSet = False
        self._fechaNacimiento = aFechaNacimiento
        wasSet = True
        return wasSet

    def getIdentificacion(self):
        return self._identificacion

    def getNombre(self):
        return self._nombre

    def getApellidos(self):
        return self._apellidos

    def getFechaNacimiento(self):
        return self._fechaNacimiento

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

    # Code from template association_GetOne 
    def getTipoIdentificacion(self):
        return self._tipoIdentificacion

    # Code from template association_MinimumNumberOfMethod 
    @staticmethod
    def minimumNumberOfReservas():
        return 0

    # Code from template association_AddManyToOne 
    def addReserva1(self, aFechaResera, aCosto, aPelicula, aPago):
        from Reserva import Reserva
        return Reserva(aFechaResera, aCosto, aPelicula, self, aPago)

    def addReserva2(self, aReserva):
        wasAdded = False
        if (aReserva) in self._reservas :
            return False
        existingUsuario = aReserva.getUsuario()
        isNewUsuario = not (existingUsuario is None) and not self == existingUsuario
        if isNewUsuario :
            aReserva.setUsuario(self)
        else :
            self._reservas.append(aReserva)
        wasAdded = True
        return wasAdded

    def removeReserva(self, aReserva):
        wasRemoved = False
        #Unable to remove aReserva, as it must always have a usuario
        if not self == aReserva.getUsuario() :
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

    # Code from template association_SetOneToMany 
    def setTipoIdentificacion(self, aTipoIdentificacion):
        wasSet = False
        if aTipoIdentificacion is None :
            return wasSet
        existingTipoIdentificacion = self._tipoIdentificacion
        self._tipoIdentificacion = aTipoIdentificacion
        if not (existingTipoIdentificacion is None) and not existingTipoIdentificacion == aTipoIdentificacion :
            existingTipoIdentificacion.removeUsuario(self)
        self._tipoIdentificacion.addUsuario(self)
        wasSet = True
        return wasSet

    def delete(self):
        i = len(self._reservas)
        while i > 0 :
            aReserva = self._reservas[i - 1]
            aReserva.delete()
            i -= 1

        placeholderTipoIdentificacion = self._tipoIdentificacion
        self._tipoIdentificacion = None
        if not (placeholderTipoIdentificacion is None) :
            placeholderTipoIdentificacion.removeUsuario(self)

    def __str__(self):
        return str(super().__str__()) + "[" + "identificacion" + ":" + str(self.getIdentificacion()) + "," + "nombre" + ":" + str(self.getNombre()) + "," + "apellidos" + ":" + str(self.getApellidos()) + "]" + str(os.linesep) + "  " + "fechaNacimiento" + "=" + str((((self.getFechaNacimiento().__str__().replaceAll("  ", "    ")) if not self.getFechaNacimiento() == self else "this") if not (self.getFechaNacimiento() is None) else "null")) + str(os.linesep) + "  " + "tipoIdentificacion = " + ((format(id(self.getTipoIdentificacion()), "x")) if not (self.getTipoIdentificacion() is None) else "null")

    def addReserva(self, *argv):
        from Reserva import Reserva
        from Date import Date
        if len(argv) == 4 and isinstance(argv[0], Date) and isinstance(argv[1], (float, int)) and isinstance(argv[2], Pelicula) and isinstance(argv[3], Pago) :
            return self.addReserva1(argv[0], argv[1], argv[2], argv[3])
        if len(argv) == 1 and isinstance(argv[0], Reserva) :
            return self.addReserva2(argv[0])
        raise TypeError("No method matches provided parameters")

    def imprimir_atributos(self):
        print(f"Identificacion: {self._identificacion}, Nombre:{self._nombre}, apellido:{self._apellidos}, tipo de indentificacion:{self._tipoIdentificacion}")
#PLEASE DO NOT EDIT THIS CODE
#This code was generated using the UMPLE 1.33.0.6934.a386b0a58 modeling language!
# line 16 "model.ump"
# line 64 "model.ump"
import os

class Reserva():
    #------------------------
    # MEMBER VARIABLES
    #------------------------
    #Reserva Attributes
    #Reserva Associations
    #------------------------
    # CONSTRUCTOR
    #------------------------
    def __init__(self, aFechaResera, aCosto, aPelicula, aUsuario, aPago):
        self._pago = None
        self._usuario = None
        self._pelicula = None
        self._costo = None
        self._fechaResera = None
        self._fechaResera = aFechaResera
        self._costo = aCosto
        didAddPelicula = self.setPelicula(aPelicula)
        if not didAddPelicula :
            raise RuntimeError ("Unable to create reserva due to pelicula. See http://manual.umple.org?RE002ViolationofAssociationMultiplicity.html")
        didAddUsuario = self.setUsuario(aUsuario)
        if not didAddUsuario :
            raise RuntimeError ("Unable to create reserva due to usuario. See http://manual.umple.org?RE002ViolationofAssociationMultiplicity.html")
        didAddPago = self.setPago(aPago)
        if not didAddPago :
            raise RuntimeError ("Unable to create reserva due to pago. See http://manual.umple.org?RE002ViolationofAssociationMultiplicity.html")

    #------------------------
    # INTERFACE
    #------------------------
    def setFechaResera(self, aFechaResera):
        wasSet = False
        self._fechaResera = aFechaResera
        wasSet = True
        return wasSet

    def setCosto(self, aCosto):
        wasSet = False
        self._costo = aCosto
        wasSet = True
        return wasSet

    def getFechaResera(self):
        return self._fechaResera

    def getCosto(self):
        return self._costo

    # Code from template association_GetOne 
    def getPelicula(self):
        return self._pelicula

    # Code from template association_GetOne 
    def getUsuario(self):
        return self._usuario

    # Code from template association_GetOne 
    def getPago(self):
        return self._pago

    # Code from template association_SetOneToMany 
    def setPelicula(self, aPelicula):
        wasSet = False
        if aPelicula is None :
            return wasSet
        existingPelicula = self._pelicula
        self._pelicula = aPelicula
        if not (existingPelicula is None) and not existingPelicula == aPelicula :
            existingPelicula.removeReserva(self)
        self._pelicula.addReserva(self)
        wasSet = True
        return wasSet

    # Code from template association_SetOneToMany 
    def setUsuario(self, aUsuario):
        wasSet = False
        if aUsuario is None :
            return wasSet
        existingUsuario = self._usuario
        self._usuario = aUsuario
        if not (existingUsuario is None) and not existingUsuario == aUsuario :
            existingUsuario.removeReserva(self)
        self._usuario.addReserva(self)
        wasSet = True
        return wasSet

    # Code from template association_SetOneToMany 
    def setPago(self, aPago):
        wasSet = False
        if aPago is None :
            return wasSet
        existingPago = self._pago
        self._pago = aPago
        if not (existingPago is None) and not existingPago == aPago :
            existingPago.removeReserva(self)
        self._pago.addReserva(self)
        wasSet = True
        return wasSet

    def delete(self):
        placeholderPelicula = self._pelicula
        self._pelicula = None
        if not (placeholderPelicula is None) :
            placeholderPelicula.removeReserva(self)
        placeholderUsuario = self._usuario
        self._usuario = None
        if not (placeholderUsuario is None) :
            placeholderUsuario.removeReserva(self)
        placeholderPago = self._pago
        self._pago = None
        if not (placeholderPago is None) :
            placeholderPago.removeReserva(self)

    def __str__(self):
        return str(super().__str__()) + "[" + "costo" + ":" + str(self.getCosto()) + "]" + str(os.linesep) + "  " + "fechaResera" + "=" + str((((self.getFechaResera().__str__().replaceAll("  ", "    ")) if not self.getFechaResera() == self else "this") if not (self.getFechaResera() is None) else "null")) + str(os.linesep) + "  " + "pelicula = " + str(((format(id(self.getPelicula()), "x")) if not (self.getPelicula() is None) else "null")) + str(os.linesep) + "  " + "usuario = " + str(((format(id(self.getUsuario()), "x")) if not (self.getUsuario() is None) else "null")) + str(os.linesep) + "  " + "pago = " + ((format(id(self.getPago()), "x")) if not (self.getPago() is None) else "null")


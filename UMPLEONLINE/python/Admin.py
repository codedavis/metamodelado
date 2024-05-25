#PLEASE DO NOT EDIT THIS CODE
#This code was generated using the UMPLE 1.33.0.6934.a386b0a58 modeling language!
# line 2 "model.ump"
# line 53 "model.ump"
from Usuario import Usuario

class Admin(Usuario):
    #------------------------
    # MEMBER VARIABLES
    #------------------------
    #Admin Attributes
    #Admin Associations
    #------------------------
    # CONSTRUCTOR
    #------------------------
    def __init__(self, aIdentificacion, aNombre, aApellidos, aFechaNacimiento, aTipoIdentificacion, aUsuario, aClave):
        self._peliculas = None
        self._clave = None
        self._usuario = None
        super().__init__(aIdentificacion, aNombre, aApellidos, aFechaNacimiento, aTipoIdentificacion)
        self._usuario = aUsuario
        self._clave = aClave
        self._peliculas = []

    #------------------------
    # INTERFACE
    #------------------------
    def setUsuario(self, aUsuario):
        wasSet = False
        self._usuario = aUsuario
        wasSet = True
        return wasSet

    def setClave(self, aClave):
        wasSet = False
        self._clave = aClave
        wasSet = True
        return wasSet

    def getUsuario(self):
        return self._usuario

    def getClave(self):
        return self._clave

    # Code from template association_GetMany 
    def getPelicula(self, index):
        aPelicula = self._peliculas[index]
        return aPelicula

    def getPeliculas(self):
        newPeliculas = tuple(self._peliculas)
        return newPeliculas

    def numberOfPeliculas(self):
        number = len(self._peliculas)
        return number

    def hasPeliculas(self):
        has = len(self._peliculas) > 0
        return has

    def indexOfPelicula(self, aPelicula):
        index = (-1 if not aPelicula in self._peliculas else self._peliculas.index(aPelicula))
        return index

    # Code from template association_MinimumNumberOfMethod 
    @staticmethod
    def minimumNumberOfPeliculas():
        return 0

    # Code from template association_AddManyToOne 
    def addPelicula1(self, aNombre, aUrl, aEstado, aDuracion):
        from Pelicula import Pelicula
        return Pelicula(aNombre, aUrl, aEstado, aDuracion, self)

    def addPelicula2(self, aPelicula):
        wasAdded = False
        if (aPelicula) in self._peliculas :
            return False
        existingAdmin = aPelicula.getAdmin()
        isNewAdmin = not (existingAdmin is None) and not self == existingAdmin
        if isNewAdmin :
            aPelicula.setAdmin(self)
        else :
            self._peliculas.append(aPelicula)
        wasAdded = True
        return wasAdded

    def removePelicula(self, aPelicula):
        wasRemoved = False
        #Unable to remove aPelicula, as it must always have a admin
        if not self == aPelicula.getAdmin() :
            self._peliculas.remove(aPelicula)
            wasRemoved = True
        return wasRemoved

    # Code from template association_AddIndexControlFunctions 
    def addPeliculaAt(self, aPelicula, index):
        wasAdded = False
        if self.addPelicula(aPelicula) :
            if index < 0 :
                index = 0
            if index > self.numberOfPeliculas() :
                index = self.numberOfPeliculas() - 1
            self._peliculas.remove(aPelicula)
            self._peliculas.insert(index, aPelicula)
            wasAdded = True
        return wasAdded

    def addOrMovePeliculaAt(self, aPelicula, index):
        wasAdded = False
        if (aPelicula) in self._peliculas :
            if index < 0 :
                index = 0
            if index > self.numberOfPeliculas() :
                index = self.numberOfPeliculas() - 1
            self._peliculas.remove(aPelicula)
            self._peliculas.insert(index, aPelicula)
            wasAdded = True
        else :
            wasAdded = self.addPeliculaAt(aPelicula, index)
        return wasAdded

    def delete(self):
        i = len(self._peliculas)
        while i > 0 :
            aPelicula = self._peliculas[i - 1]
            aPelicula.delete()
            i -= 1

        super().delete()

    def __str__(self):
        return str(super().__str__()) + "[" + "usuario" + ":" + str(self.getUsuario()) + "," + "clave" + ":" + str(self.getClave()) + "]"

    def addPelicula(self, *argv):
        from Pelicula import Pelicula
        if len(argv) == 4 and isinstance(argv[0], str) and isinstance(argv[1], str) and isinstance(argv[2], bool) and isinstance(argv[3], Time) :
            return self.addPelicula1(argv[0], argv[1], argv[2], argv[3])
        if len(argv) == 1 and isinstance(argv[0], Pelicula) :
            return self.addPelicula2(argv[0])
        raise TypeError("No method matches provided parameters")

    def imprimir_atributos(self):
        print(f"Identificacion: {self._identificacion}, Nombre:{self._nombre}, apellido:{self._apellidos}, tipo de indentificacion:{self._tipoIdentificacion} Usuario: {self._usuario}, Clave:{self._clave}")

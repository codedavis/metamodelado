#PLEASE DO NOT EDIT THIS CODE
#This code was generated using the UMPLE 1.33.0.6934.a386b0a58 modeling language!
# line 22 "model.ump"
# line 69 "model.ump"

class TipoIdentificacion():
    #------------------------
    # MEMBER VARIABLES
    #------------------------
    #TipoIdentificacion Attributes
    #TipoIdentificacion Associations
    #------------------------
    # CONSTRUCTOR
    #------------------------
    def __init__(self, aCodigo, aNombre, aDescripcion):
        self._usuarios = None
        self._descripcion = None
        self._nombre = None
        self._codigo = None
        self._codigo = aCodigo
        self._nombre = aNombre
        self._descripcion = aDescripcion
        self._usuarios = []

    #------------------------
    # INTERFACE
    #------------------------
    def setCodigo(self, aCodigo):
        wasSet = False
        self._codigo = aCodigo
        wasSet = True
        return wasSet

    def setNombre(self, aNombre):
        wasSet = False
        self._nombre = aNombre
        wasSet = True
        return wasSet

    def setDescripcion(self, aDescripcion):
        wasSet = False
        self._descripcion = aDescripcion
        wasSet = True
        return wasSet

    def getCodigo(self):
        return self._codigo

    def getNombre(self):
        return self._nombre

    def getDescripcion(self):
        return self._descripcion

    # Code from template association_GetMany 
    def getUsuario(self, index):
        aUsuario = self._usuarios[index]
        return aUsuario

    def getUsuarios(self):
        newUsuarios = tuple(self._usuarios)
        return newUsuarios

    def numberOfUsuarios(self):
        number = len(self._usuarios)
        return number

    def hasUsuarios(self):
        has = len(self._usuarios) > 0
        return has

    def indexOfUsuario(self, aUsuario):
        index = (-1 if not aUsuario in self._usuarios else self._usuarios.index(aUsuario))
        return index

    # Code from template association_MinimumNumberOfMethod 
    @staticmethod
    def minimumNumberOfUsuarios():
        return 0

    # Code from template association_AddManyToOne 
    def addUsuario1(self, aIdentificacion, aNombre, aApellidos, aFechaNacimiento):
        from Usuario import Usuario
        return Usuario(aIdentificacion, aNombre, aApellidos, aFechaNacimiento, self)

    def addUsuario2(self, aUsuario):
        wasAdded = False
        if (aUsuario) in self._usuarios :
            return False
        existingTipoIdentificacion = aUsuario.getTipoIdentificacion()
        isNewTipoIdentificacion = not (existingTipoIdentificacion is None) and not self == existingTipoIdentificacion
        if isNewTipoIdentificacion :
            aUsuario.setTipoIdentificacion(self)
        else :
            self._usuarios.append(aUsuario)
        wasAdded = True
        return wasAdded

    def removeUsuario(self, aUsuario):
        wasRemoved = False
        #Unable to remove aUsuario, as it must always have a tipoIdentificacion
        if not self == aUsuario.getTipoIdentificacion() :
            self._usuarios.remove(aUsuario)
            wasRemoved = True
        return wasRemoved

    # Code from template association_AddIndexControlFunctions 
    def addUsuarioAt(self, aUsuario, index):
        wasAdded = False
        if self.addUsuario(aUsuario) :
            if index < 0 :
                index = 0
            if index > self.numberOfUsuarios() :
                index = self.numberOfUsuarios() - 1
            self._usuarios.remove(aUsuario)
            self._usuarios.insert(index, aUsuario)
            wasAdded = True
        return wasAdded

    def addOrMoveUsuarioAt(self, aUsuario, index):
        wasAdded = False
        if (aUsuario) in self._usuarios :
            if index < 0 :
                index = 0
            if index > self.numberOfUsuarios() :
                index = self.numberOfUsuarios() - 1
            self._usuarios.remove(aUsuario)
            self._usuarios.insert(index, aUsuario)
            wasAdded = True
        else :
            wasAdded = self.addUsuarioAt(aUsuario, index)
        return wasAdded

    def delete(self):
        i = len(self._usuarios)
        while i > 0 :
            aUsuario = self._usuarios[i - 1]
            aUsuario.delete()
            i -= 1

    def __str__(self):
        return str(super().__str__()) + "[" + "codigo" + ":" + str(self.getCodigo()) + "," + "nombre" + ":" + str(self.getNombre()) + "," + "descripcion" + ":" + str(self.getDescripcion()) + "]"

    def addUsuario(self, *argv):
        from Usuario import Usuario
        if len(argv) == 4 and isinstance(argv[0], str) and isinstance(argv[1], str) and isinstance(argv[2], str) and isinstance(argv[3], Date) :
            return self.addUsuario1(argv[0], argv[1], argv[2], argv[3])
        if len(argv) == 1 and isinstance(argv[0], Usuario) :
            return self.addUsuario2(argv[0])
        raise TypeError("No method matches provided parameters")

    def imprimir_atributos(self):
        print(f"Codigo: {self._codigo}, Nombre:{self._nombre}, descripcion:{self._descripcion}")
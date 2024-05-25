from Usuario import Usuario
from Admin import Admin
from Pelicula import Pelicula
from TipoIdentificacion import TipoIdentificacion


tipoIdentificacion = TipoIdentificacion('CI','Cecula','Cedula')
print("======IDENTIFICACION=======")
print(tipoIdentificacion.imprimir_atributos())
inst = Usuario('1105644270','Carlos','Sanmartin Arevalo','1996-02-01',tipoIdentificacion)
print("======USUARIO======")
print(inst.imprimir_atributos())
admin = Admin('1234567890','Admin','ApeliidoAdmin','1999-01-02',tipoIdentificacion,'admin1','admin123')
print("======ADMIN======")
print(admin.imprimir_atributos())
pelicula=Pelicula('El viejo y el mar','https://wwww.elviejoyelmar.com',True,'2h15min',admin)
print("======PELICULA======")
print(pelicula.imprimir_atributos())

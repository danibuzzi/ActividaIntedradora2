from asyncio.windows_events import NULL
import modelo

def BuscarAlbumCodigo(cod):
    con=modelo.Conectar()
    return con.BuscarAlbumCodigo(cod)

def ListarInterpretes():
    con=modelo.Conectar()
    return con.ListarInterprete()

def ListarDiscograficas():
    con=modelo.Conectar()
    return con.ListarDiscografica()

def ListarFormatos():
    con=modelo.Conectar()
    return con.ListarFormato()

def ListarGeneros():
    con=modelo.Conectar()
    return con.ListarGenero()   



def ListarAlbumesPorArtistas():
    con = modelo.Conectar()
    return con.ListarAlbumes()

    
 
 

def ListarAlbumesPorGenero():
    con = modelo.Conectar()
    return con.ListarPorGenero()


def BuscarAlbumes(nombre):
    con = modelo.Conectar()
 
    return con.BuscarAlbum(nombre)  

def InsertarAlbum(cod_album,nombre,id_interprete,id_genero,cant_temas,
id_discografica,id_formato,fec_lanzamiento,precio,cantidad,caratula):
  

    con = modelo.Conectar()


    nuevoAlbum = modelo.Album(0,cod_album,nombre,id_interprete,id_genero,cant_temas,id_discografica,id_formato,fec_lanzamiento,precio,cantidad,caratula)
    con.InsertarAlbum(nuevoAlbum)
    #input("Presione ENTER para continuar")


#def ModificarAlbum(nombre,cod_album):

def ModificarAlbum(nombre,id_interprete,id_genero,_cant_temas,
    id_discografica,id_formato,fech_lanzamiento,precio,cantidad,caratula,cod_album,id):

    con=modelo.Conectar()
 
    edicionAlbum=modelo.Album(id,cod_album,nombre,id_interprete,id_genero,_cant_temas,
    id_discografica,id_formato,fech_lanzamiento,precio,cantidad,caratula)
    con.ModificarAlbum(edicionAlbum,id)
    #input("Presione ENTER para continuar")


def EliminarAlbum(id):
    con=modelo.Conectar()
  
    con.EliminarAlbum(id)
    #con.conexion.close() 
    #input("Presione ENTER para continuar")
    





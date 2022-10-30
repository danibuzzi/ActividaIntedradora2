
from asyncio.windows_events import NULL
import os
import controlador
import modelo
from flask import Flask
from flask import render_template,request,redirect
from flask import send_from_directory


app=Flask(__name__)

# definir ruta para las imagenes

@app.route('/img/<imagen>')
def imagenes(imagen):
    return send_from_directory(os.path.join('templates/sitio/img'),imagen)

#define ruta para las hojas de estilo (css)

@app.route('/css/<archivocss>')

def css(archivocss):
    return send_from_directory(os.path.join('templates/sitio/css'),archivocss)

#define rutas para archivos los javascript


@app.route('/js/<archivojs>')
def javajs(archivojs):
        return send_from_directory(os.path.join('templates/sitio/js'),archivojs)

#define rutas para archivos de bootstrap

@app.route('/bootstrap/<archivoboot>')
def boots(archivoboot):
        return send_from_directory(os.path.join('templates/sitio/bootstrap'),archivoboot)


#ruta para el archivo index

@app.route('/')

def inicio():
    return render_template('sitio/index.html')


#ruta para lista de albums por artista

@app.route('/listaalbumes')

def listaalbumes():
    albumes=controlador.ListarAlbumesPorArtistas() 
  
    return render_template('sitio/listaalbumes.html',albums=albumes)
  

# ruta para lista de albums por genero

@app.route('/listagenero')

def listagenero():
    albumes=controlador.ListarAlbumesPorGenero() 
  
    return render_template('sitio/listagenero.html',albums=albumes)
    

#ruta pta la busqueda por nombre de album

@app.route('/buscar',methods=['POST'])
def buscaralbum():
    nombrealbum=request.form['txtbuscar']
    print('Nombre del album ',nombrealbum)
    albumes=controlador.BuscarAlbumes(nombrealbum)
    if albumes is None:
        print('no encontrado')
    return render_template('sitio/listaalbumnombre.html',albums=albumes)
      
 #ruta para el alta de un album   

@app.route('/altaalbum')

def altaalbum():
    interprete=controlador.ListarInterpretes()
    discografica=controlador.ListarDiscograficas()
    formato= controlador.ListarFormatos()
    genero = controlador.ListarGeneros()

    return render_template('sitio/altaalbum.html',interpretes=interprete,
    discograficas=discografica,formatos=formato,generos=genero)    

#ruta intermedia para efectuar el guardado de nuevo album

@app.route('/altaalbum/guardar',methods=['POST'])

def guardar_album():

    print(request.form['txtcodigo'])
    _codalbum=request.form['txtcodigo']
    _nombre=request.form['txtnombre']
    _interprete=request.form['txtinterprete']
    _genero=request.form['txtgenero']
    _temas=request.form['txttemas']
    _discografica=request.form['txtdiscografica']
    _formato=request.form['txtformato']
    _fecha=request.form['txtfecha']
    _precio=request.form['txtprecio']
    _cantidad=request.form['txtcantidad']
    _caratula=request.files['txtcaratula']

    
    if _caratula.filename!="":
        _caratula.save("templates/sitio/img/"+_caratula.filename)   

    print("Interprete es ",_interprete)  
    controlador.InsertarAlbum(_codalbum,_nombre,_interprete,_genero,_temas,_discografica,
    _formato,_fecha,_precio,_cantidad,_caratula.filename)

    
    return redirect('/listaalbumes')


#ruta para  llevar los datos de la consulta de albums a la pantalla de modificacion

@app.route('/listaalbumes/modificar/<int:id>',methods=['POST'])
def modificar(id):
  
    album=controlador.BuscarAlbumCodigo(id)

    interprete=controlador.ListarInterpretes()
    discografica=controlador.ListarDiscograficas()
    formato= controlador.ListarFormatos()
    genero = controlador.ListarGeneros()

    return render_template('sitio/modificaalbum.html',interpretes=interprete,
    discograficas=discografica,formatos=formato,generos=genero,album=album) 


 #ruta para  efectuar la modificacion de datos de un album

@app.route('/update/<int:id>',methods=['POST'])

def update_album(id):


     cod_album=request.form['txtcodigo']
     nombre=request.form['txtnombre']
     id_interprete=request.form['txtinterprete2']
     id_genero=request.form['txtgenero2']
     cant_temas=request.form['txttemas']
     id_discografica=request.form['txtdiscografica2']
     id_formato=request.form['txtformato2']
     fech_lanzamiento=request.form['txtfecha']
     precio=request.form['txtprecio']

     cantidad=request.form['txtcantidad']
    
     caratula=request.files['txtcaratula']

    
     if caratula.filename!="":
        caratula.save("templates/sitio/img/"+caratula.filename) 

 

     con=modelo.Conectar()
     edicionAlbum=modelo.Album(0,cod_album,nombre,id_interprete,id_genero,cant_temas,
     id_discografica,id_formato,fech_lanzamiento,precio,cantidad,caratula.filename)
     con.ModificarAlbum(edicionAlbum,id)
 
 
     print('Album modficado')
     return redirect('/listaalbumes')



@app.route('/modificaalbum')
def modificaalbum():
 
    return redirect('sitio/index.html') 


#ruta para el borrado de un album desde el listado de albums

@app.route('/listaalbumes/borrar/<int:id>',methods=['POST'])

def borrraralbum(id):
  
    print(id)
    controlador.EliminarAlbum(id)
    return redirect('/listaalbumes')




if __name__ =='__main__':
    app.run(debug=True)




from asyncio.windows_events import NULL
import controlador
from flask import Flask
from flask import render_template,request,redirect


app=Flask(__name__)



@app.route('/')

def inicio():
    return render_template('sitio/index.html')



@app.route('/listaalbumes')

def listaalbumes():
    albumes=controlador.ListarAlbumesPorArtistas() 
  
    return render_template('sitio/listaalbumes.html',albums=albumes)
  


@app.route('/listagenero')

def listagenero():
    generos=controlador.ListarAlbumesPorGenero() 
  
    return render_template('sitio/listagenero.html',generos=generos)
    #return render_template('sitio/listaalbumes.html')


@app.route('/buscar',methods=['POST'])
def buscaralbum():
    nombrealbum=request.form['txtbuscar']
    print('Nombre del album ',nombrealbum)
    albumes=controlador.BuscarAlbumes(nombrealbum)
    if albumes is None:
        print('no encontrado')
    return render_template('sitio/listaalbumnombre.html',albums=albumes)
      
    

@app.route('/altaalbum')

def altaalbum():
    interprete=controlador.ListarInterpretes()
    discografica=controlador.ListarDiscograficas()
    formato= controlador.ListarFormatos()
    genero = controlador.ListarGeneros()

    return render_template('sitio/altaalbum.html',interpretes=interprete,
    discograficas=discografica,formatos=formato,generos=genero)    


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
    _caratula=request.form['txtcaratula']
    print("Interprete es ",_interprete)  
    controlador.InsertarAlbum(_codalbum,_nombre,_interprete,_genero,_temas,_discografica,
    _formato,_fecha,_precio,_cantidad,_caratula)

    
    return redirect('/listaalbumes')

@app.route('/listaalbumes/modificar',methods=['POST'])
def modificar():
    _id=request.form['txtid2']
    album=controlador.BuscarAlbumCodigo(_id)
    #controlador.
    #return redirect('/')
    return render_template('sitio/modificaalbum.html',album=album)

@app.route('/update',methods=['POST'])

def update_album():
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
    _caratula=request.form['txtcaratula']
  #con.ModificarAlbum(nombre,id_interprete,id_genero,id_discografica,cod_album)
    controlador.ModificarAlbum(_nombre,_interprete,_genero,_discografica,_codalbum)
    #controlador .InsertarAlbum(_codalbum,_nombre,_interprete,_genero,_temas,_discografica,
     #_formato,_fecha,_precio,_cantidad,_caratula)
    print('modficado')
    return redirect('/listaalbumes')


@app.route('/modificaalbum')
def modificaalbum():
    return render_template('sitio/modificaalbum.html') 


@app.route('/listaalbumes/borrar',methods=['POST'])

def borrraralbum():
    _id=request.form['txtid']
    print(_id)
    controlador.EliminarAlbum(_id)
    return redirect('/listaalbumes')




if __name__ =='__main__':
    app.run(debug=True)




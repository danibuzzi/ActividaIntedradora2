import mysql.connector

def conectarBD():
    try:

        conexion= mysql.connector.connect(

        host='localhost',
        port=3306,
        user='root',
        password='',
        db='disqueria'
        )

        if conexion.is_connected():
            print('La conexion se ha establecido con exito')
            #imprimo informacion del servidor
            info_server=conexion.get_server_info() 
            print(info_server)

            #objeto (cursor) que hace de nexo en la la db y nuestro programa

            cursor= conexion.cursor()
            cursor.execute("select * from interprete")

            # traigo los datos de interprete en una lista
            lista=cursor.fetchall()

            # recorro la lista y muestro los datos

            for dato in lista:
                print(dato)
        
    
    except mysql.connector.Error as ex:
        print('No se conectó')
        return
        #print(ex)
        
        

    ''' finally:
        if conexion.is_connected():

            conexion.close()
            print('Se cerró la conexion')
'''
conectarBD()
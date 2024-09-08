import os
import sqlite3
from datetime import datetime as dt
from cryptography.fernet import Fernet

class EncrypDecrypt:
    def __init__(self, Clave, PassEncript) -> None:
        self._key = None
        self._enc = None

        if len(Clave) == 0:
            self._clave = Fernet.generate_key()
        else:
            if Clave == "2":
                self._clave = b'6Xw2QXkq8dGmA9MvZCmmCMICwWGQvAbqdAHwsx0IhHk='
            else:
                self._clave = Clave
            
        self._PassEncript = PassEncript
    
    @property
    def TexToencript(self):
        return self._TexToencript

    @TexToencript.setter
    def TexToencript(self, value):
        self._TexToencript = value

    @property
    def key(self):
        return self._clave
    
    @property
    def enc(self):
        return(self._enc)

    def DesEncripto(self):
        # Crea un objeto Fernet con la clave
        fernet = Fernet(self._clave)
        password_desencriptada = fernet.decrypt(self._PassEncript)
        password = password_desencriptada.decode()
        return (password)
    
    def Encripto(self):
        self._key = Fernet(self._clave)
        password = self._TexToencript.encode()
        self._enc = self._key.encrypt(password)

pantallaprincipal = {
    "titulo": "Hamburguesas IT",
    "responsable": "Encargada/o -> ",
    "mensaje": "Recuerda, siempre hay que recibir al cliente," + "\n" + "con una sonrisa :)",
    "item1": "1 – Ingreso nuevo pedido",
    "item2": "2 – Cambio de turno",
    "item3": "3 – Apagar sistema"
    }

def clscr():
    """
    Funcion que limpia pantalla
    """    
    os.system("cls")

def fib(valor):
    """
    Función que genera secuencia de 
    números siguiendo suseción Fibonachi

    Args:
        valor (int): Valor que indica la cantidad 
                     elementos dentro del conjunto
                     de la secuencia.
    """    
    fibonachi = []
    for i in range(0,valor):
        if i == 0:
            fibonachi.append(i)
        if i == 1:
            fibonachi.append(i)
        if i > 1:
            fibonachi.append(fibonachi[i-1]+fibonachi[i-2])
    return(fibonachi)

def is_number(num):
    """
    Funcion que verifica si un valor ingresado por el usuario es numero
    Args:
        num (str): Dato ingresado

    Returns:
        bool: True o False
    """    
    numero = 0
    try:
        numero = float(num)
        return True
    except:
        return False

def datos(ruta):
    contador = 0
    lista = []
    with open(ruta) as f:
        while True:
            linea = f.readline().rstrip().lstrip()
        
            if linea != "":
                contador += 1
                lista.append(linea)
            else:
                return lista
                break

def buscoenlista(lista,datoabuscar):
    for d in lista:
        if datoabuscar == d.upper():
            return d.upper()
    return ''

def mainmenu(personal):
    print("-" * 45)
    print(pantallaprincipal['titulo'])
    print(f"{pantallaprincipal['responsable']} '{personal}' {dt.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print(pantallaprincipal['mensaje'])
    print("-" * 45)
    print(f"\t{pantallaprincipal['item1']}")
    print(f"\t{pantallaprincipal['item2']}")
    print(f"\t{pantallaprincipal['item3']}")
    print("")
    return None

def factorial(n):
    c = n
    f = 1

    print(f"{c} ! = ",end='')
    while (c > 0):
        if c > 1:
            print(f"{c} x ", end='')
        else:
            print(f"{c} = ", end='')
        
        f *= c
        c -= 1
    print(f)

    return(f)

class MenuONU:
    def __init__(self):
        self._ltext = f'''
**********************************
*** DATOS DE POBLACION MUNDIAL ***
**********************************
* Ingrese nombre del país
* Retenga su código
* Ingréselo cuando sea solicitado
**********************************'''

    @property
    def Ltext(self):
        return self._ltext

    @Ltext.setter
    def Ltext(self, value):
        self._ltext = value

def ConvSegundos(Segundos):
    import pandas as pd
    n = Segundos

    # ENUNCIADO DE VARIABLES
    sxm = 60 
    sxh = sxm * 60
    sxd = sxh * 24
    sxme = sxd * 30
    sxa = sxd * 365

    a = 0
    mes = 0
    d = 0
    h = 0
    m = 0
    s = 0

    ra = 0
    rmes = 0
    rd = 0
    rh = 0
    rm = 0
    rs = 0
    # FIN ENUNCIADO

    a = n // sxa
    ra = n % sxa


    mes = ra // sxme
    rmes = ra % sxme


    d = rmes // sxd
    rd = rmes % sxd

    h = rd // sxh
    rh = rd % sxh 


    m = rh // 60
    rm = rh % 60


    s = rm // 60
    rs = rm % 60
    rs = round(rs,2)


    result = []

    result.append(a)
    result.append(mes)
    result.append(d)
    result.append(h)
    result.append(m)
    result.append(rs)

    indice = ["Años","Meses","Días","horas","Minutos","Segundos"]

    ds = pd.Series(result,indice,name=None, dtype=None)

    mask = ds != 0

    ds = ds[mask]

    ds = ds.to_string(index=True, name="Resultados", dtype=None)

    return(ds)

def randonpassword(caracteres):
    import random
    import string

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    numer = string.digits
    symbo = string.punctuation

    chars = lower + upper + numer + symbo

    temp = random.sample(chars,caracteres)

    return("".join(temp))

def espacios(**kwargs):

    """
    Descripción de la función.

    Args:
        Caracter (Texto): Carácter que se desplega.
        nLineas  (Int): Veces que se repite el parametro Caracter.

    Returns:
        **kwargs: Puedo enviar uno, dos o ningun parámetro.
        Nada: Solo desplega un \\n.
        Caracter: Se deplega dicho parámetro una vez.
        nLineas: Se desplega \\n nLineas veces.
        Caracter + nLineas: Desplega el caracter enviado nLineas veces.
    """

    if not kwargs:
        return("\n")
    
    if not "Caracter" in kwargs:
        Cter = "\n"
    else: 
        Cter = kwargs['Caracter']
    
    if not "nLineas" in kwargs:
        nLi = 1
    else:
        nLi =  kwargs['nLineas']

    return(Cter * nLi)

def ConvSegundos(Segundos):
    import pandas as pd
    n = Segundos

    # ENUNCIADO DE VARIABLES
    sxm = 60 
    sxh = sxm * 60
    sxd = sxh * 24
    sxme = sxd * 30
    sxa = sxd * 365

    a = 0
    mes = 0
    d = 0
    h = 0
    m = 0
    s = 0

    ra = 0
    rmes = 0
    rd = 0
    rh = 0
    rm = 0
    rs = 0
    # FIN ENUNCIADO

    a = n // sxa
    ra = n % sxa


    mes = ra // sxme
    rmes = ra % sxme


    d = rmes // sxd
    rd = rmes % sxd

    h = rd // sxh
    rh = rd % sxh 


    m = rh // 60
    rm = rh % 60


    s = rm // 60
    rs = rm % 60
    rs = round(rs,2)


    result = []

    result.append(a)
    result.append(mes)
    result.append(d)
    result.append(h)
    result.append(m)
    result.append(rs)

    indice = ["Años","Meses","Días","horas","Minutos","Segundos"]

    ds = pd.Series(result,indice,name=None, dtype=None)

    mask = ds != 0

    ds = ds[mask]

    ds = ds.to_string(index=True, name="Resultados", dtype=None)

    return(ds)

def VerificoSSO(*gAD):
    import pyad.adquery
    import getpass
    import sys, os

    userlogedin = getpass.getuser()
    userID = userlogedin
    userlogedin = f"'{userlogedin}'"
    
    if gAD:
        grupoAD = gAD[0]
    else:
        grupoAD =  "CN=DSI INFRAESTRUCTURA WIFI"

    query = (f'sAMAccountName = {userlogedin}')

    # Establecer la conexión con el servidor AD
    pyad.pyad_setdefaults(ldap_server="SWPBUETYYPF01")

    try:
        # Realizar una consulta para buscar un usuario específico
        q = pyad.adquery.ADQuery()
        q.execute_query(
            attributes=["cn", "sAMAccountName", "mail", "memberOf"],
            where_clause=f"{query}")

        # Obtener los resultados
        results = list(q.get_results())

        pertence = False

        if results:
            user = results[0]
            for g in user["memberOf"]:
                r = g.split(",")
                if grupoAD in r:
                    pertence = True
            if pertence:
                return(True,"OK",userID)
            else:
                return(False,"Not OK",userID)
        else:
            print("Usuario inexistente")
    except Exception as e:
        return(False,"Error al verificar SSO",userID)
            
def eliminoCaracteresNoValidos(variable):
    novalido = '/\:*?"<>|'
    a = variable
    for c in novalido:
        if c in a:
            a = a.replace(c,"").strip()
    return(a)

def EliminoArchivos(extencion, **kwargs):
    workfolder = os.getcwd()
    files_ = os.listdir(f"{workfolder}/TEMP-FILES")
    # Filtrar la lista para obtener solo los archivos segun el parámetro extencion
    archivos = [archivo for archivo in files_ if archivo.endswith(extencion)]

    if not archivos:
        print(f"ningún comparte criterio {extencion}")
        return
    
    if kwargs['clean'] == True:
        # Borrar los archivos segun extencion (parámetro)
        for archivo in archivos:
            file_path = os.path.join(workfolder, "TEMP-FILES", archivo)
            os.remove(file_path)
            print(f"Archivo borrado: {archivo}")
    else:
        for archivo in archivos:
            print(f"{archivo}")

    return

def buscoChar(valor):
    devuelvo = True
    for c in valor:
        if c in ["(","-"]:
            devuelvo = False

    return devuelvo

def GenCursor(sqlT,db,*args):
    print(db)

    if args:
        parametro3 = args[0]
    else:
        parametro3 = None  # Establecer un valor predeterminado si el tercer parámetro no se proporciona

    try:
        conn = sqlite3.connect(f'{db}')
        cursor = conn.cursor()
        cursor.execute(sqlT)
        resultados = cursor.fetchall()
        if resultados:
            conn.commit()
            cursor.close()
            conn.close()
            if not parametro3 or parametro3 == 'tupla':
                return(resultados)
            else:
                return(resultados,[descripcion[0] for descripcion in cursor.description])  
        return(None)
    except sqlite3.Error as e:
            clscr()
            print(f"Error de SQLite3: {e}")
            input("Cualquier tecla para salir del programa > ")
            exit(0)  


    
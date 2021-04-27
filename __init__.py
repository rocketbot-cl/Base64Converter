# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"

    pip install <package> -t .

"""
base_path = tmp_global_obj["basepath"]
cur_path = base_path + "modules" + os.sep + "Base64Converter" + os.sep + "libs" + os.sep
sys.path.append(cur_path)
from converter_service import *

"""
    Obtengo el modulo que fue invocado
"""

module = GetParams("module")

if module == "encode":
    path_file = GetParams("path_file")
    if not path_file:
        raise Exception("No se cargo el archivo")
    try:
        base64_text = encode_to_base64(path_file)
        result = GetParams("result")
        SetVar(result, base64_text)
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e

if module == "decode":
    base64_text = GetParams("base64_text")
    path_file = GetParams("path_file")
    type_decode = GetParams("type_decode")
    if not base64_text:
        raise Exception("No se cargo la variable o texto")
    if not path_file:
        raise Exception("No se cargo el archivo")
    try:
        base64_text = base64_text
        decode_to_base64(path_file, base64_text, type_decode)
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e
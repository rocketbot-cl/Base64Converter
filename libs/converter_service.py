import base64


def encode_to_base64(path_file):
    with open(path_file, "rb") as file:
        base64_text = base64.b64encode(file.read())
        return base64_text.decode()


def decode_to_base64(path_file, base64_text, type_decode):
    with open(path_file, "wb") as file:
        base64_text = base64_text.encode(type_decode, "ignore")
        file.write(base64.b64decode(base64_text))

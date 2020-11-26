import base64


def encode_to_base64(path_file):
    with open(path_file, "rb") as file:
        base64_text = base64.b64encode(file.read())
        return base64_text

def decode_to_base64(path_file, base64_text):
    with open(path_file, "wb") as file:
        file.write(base64.b64decode(base64_text))

if __name__ == '__main__':
    path_file = "captura.png"
    text = encode_to_base64(path_file)
    path_file = "captura22.png"
    decode_to_base64(path_file, text)
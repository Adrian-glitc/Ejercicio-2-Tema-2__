from Texto import Texto

def main():
    texto_original = ("un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#"
                      "lo que se mueve es el viento -respondió otro monje#"
                      "ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro")

    texto_arreglado = Texto.arreglar_texto(texto_original)
    print(texto_arreglado)


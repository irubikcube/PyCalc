# Gracias a Rene por este gostando:

# https://gist.github.com/rene-d/9e584a7dd2935d0f461904b9f2950007

# Constantes de color SGR
# rene-d 2018

class Colores:
    """ Códigos de color ANSI """
    NEGRO = "\033[0;30m"
    ROJO = "\033[0;31m"
    VERDE = "\033[0;32m"
    MARRÓN = "\033[0;33m"
    AZUL = "\033[0;34m"
    PÚRPURA = "\033[0;35m"
    CIANO = "\033[0;36m"
    GRIS_CLARO = "\033[0;37m"
    GRIS_OSCURO = "\033[1;30m"
    ROJO_CLARO = "\033[1;31m"
    VERDE_CLARO = "\033[1;32m"
    AMARILLO = "\033[1;33m"
    AZUL_CLARO = "\033[1;34m"
    PÚRPURA_CLARO = "\033[1;35m"
    CIAN_CLARO = "\033[1;36m"
    BLANCO = "\033[1;37m"
    ATREVIDO = "\033[1m"
    FAINT = "\033[2m"
    ITÁLICO = "\033[3m"
    TESTADO = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVO = "\033[7m"
    CROSSED = "\033[9m"
    FIN = "\033[0m"
    # cancelar códigos SGR se nós não escrevermos no terminal
    if not __import__("sys").stdout.isatty():
        for _ in dir():
            if isinstance(_, str) and _[0] != "_":
                locals()[_] = ""
    else:
        # definir o console do Windows no modo VT (Virtual Terminal)
        if __import__("platform").system() == "Windows":
            kernel32 = __import__("ctypes").windll.kernel32
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
            del kernel32


if __name__ == '__main__':
    for i in dir(Colores):
        if i[0:1] != "_" and i != "FIN":
            print("{:>16} {}".format(i, getattr(Colores, i) + i + Colores.FIN))
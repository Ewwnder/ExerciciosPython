teclado = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./"

try:
    while True:
        linha = input()
        resultado = ""

        for char in linha:
            if char == ' ':
                resultado += ' '
            elif char == '\n':
                resultado += '\n'
            else:
                pos = teclado.find(char)
                if pos != -1:
                    if pos > 0:
                        resultado += teclado[pos-1]
                    else:
                        resultado += teclado[pos]
                else:
                    resultado += char

        print(resultado)
except EOFError:
    pass

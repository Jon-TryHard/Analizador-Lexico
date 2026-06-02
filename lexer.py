# lexer.py
from rich import print
import sly

class Lexer(sly.Lexer):
    # Todos los tokens que el parser necesitará reconocer
    tokens = {
        # Palabras Reservadas
        ARRAY, BOOLEAN, CHAR, ELSE, FALSE, FLOAT, FOR, FUNCTION, IF,
        INTEGER, PRINT, RETURN, STRING, TRUE, VOID, WHILE,
        CLASS, THIS, SUPER, NEW,

        # Operadores de Relación
        LT, LE, GT, GE, EQ, NE, LAND, LOR,

        # Operadores de Asignación y Aumento
        ADDEQ, SUBEQ, MULEQ, DIVEQ, MODEQ, INC, DEC, ASSIGN,

        # Identificadores y Literales
        ID,
        LITERAL_INTEGER, LITERAL_FLOAT, LITERAL_CHAR, LITERAL_STRING,
    }
    
    # Caracteres de un solo símbolo (incluidos los del ternario '?' y ':')
    literals = '+-*/%^=;,.:()[]{}?'

    # Caracteres a ignorar (espacios y tabulaciones)
    ignore = ' \t\r'

    # --- REGLAS prioritarias (Operadores compuestos primero) ---
    
    # Incremento / Decremento
    INC = r'\+\+'
    DEC = r'--'

    # Asignaciones compuestas
    ADDEQ = r'\+='
    SUBEQ = r'-='
    MULEQ = r'\*='
    DIVEQ = r'/='
    MODEQ = r'%='

    # Operadores de relación compuestos
    LE = r'<='
    GE = r'>='
    EQ = r'=='
    NE = r'!='

    # Operadores lógicos
    LAND = r'&&'
    LOR  = r'\|\|'

    # Operadores simples que podrían colisionar si no se separan bien
    LT = r'<'
    GT = r'>'
    ASSIGN = r'='

    # Literales (El float va antes que el integer para no ser devorado)
    LITERAL_FLOAT   = r'\d+\.\d+'
    LITERAL_INTEGER = r'\d+'
    
    # Cadenas de texto y caracteres
    LITERAL_STRING  = r'\"([^\\\n]|(\\.))*?\"'
    LITERAL_CHAR    = r'\'([^\\\n]|(\\.))?\''

    # Identificadores y Palabras Reservadas
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'

    # Diccionario explícito de Palabras Reservadas (Mapeo de ID)
    # SLY requiere que las palabras reservadas se verifiquen dentro de los ID
    reserved_words = {
        'array': ARRAY,
        'boolean': BOOLEAN,
        'char': CHAR,
        'else': ELSE,
        'false': FALSE,
        'float': FLOAT,
        'for': FOR,
        'function': FUNCTION,
        'if': IF,
        'integer': INTEGER,
        'print': PRINT,
        'return': RETURN,
        'string': STRING,
        'true': TRUE,
        'void': VOID,
        'while': WHILE,
        'class': CLASS,
        'this': THIS,
        'super': SUPER,
        'new': NEW
    }

    def ID(self, t):
        # Si el ID coincide con una palabra reservada, cambia su tipo
        t.type = self.reserved_words.get(t.value, 'ID')
        return t

    # --- Manejo de comentarios y saltos de línea ---

    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    @_(r'/\*(.|\n)*?\*/')
    def ignore_comment(self, t):
        self.lineno += t.value.count('\n')

    @_(r'//.*\n')
    def ignore_cppcomment(self, t):
        self.lineno += 1

    # Manejo de errores léxicos
    def error(self, t):
        print(f"[bold red]Línea {self.lineno}: Caracter ilegal '{t.value[0]}'[/bold red]")
        self.index += 1

def tokenize(txt):
    lex = Lexer()
    tokens = []
    for tok in lex.tokenize(txt):
        tokens.append((tok.type, tok.value, tok.lineno))
    
    # Impresión bonita con rich
    print(tokens)

if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        print('[bold yellow]Uso: python lexer.py <filename>[/bold yellow]')
        sys.exit(1)

    try:
        with open(sys.argv[1], encoding='utf-8') as f:
            txt = f.read()
        tokenize(txt)
    except FileNotFoundError:
        print(f"[bold red]Error: El archivo '{sys.argv[1]}' no existe.[/bold red]")
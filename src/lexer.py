from ply.lex import lex
from prettytable import PrettyTable

literals = [
  "+",
  "-",
  "*",
  "/",
  "%",
  "(",
  ")",
  "[",
  "]",
  "{",
  "}",
  "=",
  ";",
  ":",
  ",",
  "'",
  '"',
]

reserved = {
  'if': 'IF',
  'else': 'ELSE',
  'for': 'FOR',
  'while': 'WHILE',
  'break': 'BREAK',
  'continue': 'CONTINUE',
  'return': 'RETURN',
  'false': 'FALSE',
  'true': 'TRUE',
  'int': 'INT',
  'float': 'FLOAT',
  'bool': 'BOOL',
  'char': 'CHARTYPE',
  'string': 'STRINGTYPE',
  'void': 'VOID',
  'printf': 'PRINT',
  'case': 'CASE'
}

tokens = [
  'PLUSASSIGN',
  'SUBASSIGN',
  'MULASSIGN',
  'DIVASSIGN',
  'PLUSPLUS',
  'MINUSMINUS',
  'LESSER_THAN',
  'GREATER_THAN',
  'LESSER_EQUAL',
  'GREATER_EQUAL',
  'NOT_EQUAL',
  'EQUAL',
  'ID',
  'FLOATNUM',
  'INTNUM',
  'CHAR',
  'STRING',
] + list(reserved.values())


t_ignore = ' \t'
t_ignore_COMMENT = r'//.*'

t_PLUSASSIGN = r'\+='
t_SUBASSIGN = r'-='
t_MULASSIGN = r'\*='
t_DIVASSIGN = r'\/='

t_LESSER_THAN = r'\<'
t_GREATER_THAN = r'\>'
t_LESSER_EQUAL = r'\<='
t_GREATER_EQUAL = r'\>='
t_NOT_EQUAL = r'\!='
t_EQUAL = r'\=='

t_CHAR = r'\'([a-zA-Z_0-9\W])\''
t_STRING = r'\"([^\\\n]|(\\.))*?\"'


def t_ID(t):
  r'[a-zA-Z_][a-zA-Z_0-9]*'
  t.type = reserved.get(t.value, 'ID')

  for reserved_word in reserved:
    if reserved_word in t.value and reserved_word != t.value:
      if(t.value == "printf"):
        continue
      print("At line %d: Illegal identifier '%s'" % (t.lineno, t.value))
      t.lexer.skip(len(t.value))
      raise Exception("Lexical error")

  return t


def t_FLOATNUM(t):
  r'([0-9]*[\.][0-9]+|[0-9]+[\.][0-9]*)((E|e)(\+|-)?[0-9]+)?|([0-9]+)((E|e)(\+|-)?[0-9]+)'
  t.value = float(t.value)
  return t


def t_INTNUM(t):
  r'\d+(?![a-zA-Z])'
  t.value = int(t.value)
  return t


def t_PLUSPLUS(t):
  r'\+\++'
  if len(t.value) > 2:
    print("At line %d: Lexical error - increment length is greater than 2" % t.lineno)
    t.lexer.skip(len(t.value))
    raise Exception("Lexical error")
  return t


def t_MINUSMINUS(t):
  r'--+'
  if len(t.value) > 2:
    print("At line %d: Lexical error - decrement length is greater than 2 '%s'" % (t.lineno, t.value))
    t.lexer.skip(len(t.value))
    raise Exception("Lexical error")
  return t


def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)


def t_error(t):
  print("At line %d: Illegal character '%s'" % (t.lineno, t.value[0]))
  t.lexer.skip(1)
  raise Exception("Lexical error")


lexer = lex()

if __name__ == "__main__":
  table = PrettyTable()
  table.field_names = ["Line", "Token Type", "Token Value"]
  general_set = set()

  filename = 'select-sort.c'

  with open(filename, 'r') as f:
    lexer.input(f.read())
    for token in lexer:
      if token.value not in general_set:
        table.add_row([token.lineno, token.type, token.value])
        general_set.add(token.value)

  lexer.lineno = 1
  print(table)

  #============================Literals Table============================#
  literal_table = PrettyTable()
  literal_table.field_names = ["Line", "Literal"]

  literal_set = set()

  with open(filename, 'r') as f:
    lexer.input(f.read())
    for token in lexer:
      if token.type in literals and token.value not in literal_set:
        literal_table.add_row([token.lineno, token.value])
        literal_set.add(token.value)

  lexer.lineno = 1
  print("\nLiteral Table:")
  print(literal_table)
  #============================Reserved words Table=======================#
  reserved_table = PrettyTable()
  reserved_table.field_names = ["Line", "Reserved Word"]

  reserved_set = set()

  with open(filename, 'r') as f:
    lexer.input(f.read())
    for token in lexer:
      if token.type in reserved.values() and token.value not in reserved_set:
        reserved_table.add_row([token.lineno, token.value])
        reserved_set.add(token.value)

  lexer.lineno = 1
  print("\nReserved Words Table:")
  print(reserved_table)
  #============================Operators Table============================#
  operators_table = PrettyTable()
  operators_table.field_names = ["Line", "Operator"]

  operator_set = set()

  with open(filename, 'r') as f:
    lexer.input(f.read())
    for token in lexer:
      if token.type in ['PLUSASSIGN', 'SUBASSIGN', 'MULASSIGN', 'DIVASSIGN', 'PLUSPLUS',
                        'MINUSMINUS', 'LESSER_THAN', 'GREATER_THAN', 'LESSER_EQUAL',
                        'GREATER_EQUAL', 'NOT_EQUAL', 'EQUAL'] and token.value not in operator_set:
        operators_table.add_row([token.lineno, token.value])
        operator_set.add(token.value)

  lexer.lineno = 1
  print("\nOperators Table:")
  print(operators_table)
  #============================ID Table============================#
  id_table = PrettyTable()
  id_table.field_names = ["Line", "Identifier"]

  id_set = set()

  with open(filename, 'r') as f:
    lexer.input(f.read())
    for token in lexer:
      if token.type == 'ID' and token.value not in id_set:
        id_table.add_row([token.lineno, token.value])
        id_set.add(token.value)

  lexer.lineno = 1
  print("\nIdentifier Table:")
  print(id_table)
  #============================Numbers Table============================#
  numbers_table = PrettyTable()
  numbers_table.field_names = ["Line", "Type", "Value"]

  numbers_set = set()

  with open(filename, 'r') as f:
    lexer.input(f.read())
    for token in lexer:
      if token.type in ['INTNUM', 'FLOATNUM'] and token.value not in numbers_set:
        numbers_table.add_row([token.lineno, token.type, token.value])
        numbers_set.add(token.value)

  lexer.lineno = 1
  print("\nNumbers Table:")
  print(numbers_table)
  #============================Symbol Table============================#
  symbol_table = PrettyTable()
  symbol_table.field_names = ["Line", "CHAR or STRING"]

  symbol_set = set()

  with open(filename, 'r') as f:
    lexer.input(f.read())
    for token in lexer:
      if token.type in ['CHAR', 'STRING'] and token.value not in symbol_set:
        symbol_table.add_row([token.lineno, token.value])
        symbol_set.add(token.value)

  lexer.lineno = 1
  print("\nSymbol Table:")
  print(symbol_table)
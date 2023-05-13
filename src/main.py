import lexer
import myparser
import sys
from type_checker import TypeChecker


if __name__ == '__main__':

  if len(sys.argv) <= 1:
    print("Run program with a file name to be parsed")
    sys.exit(1)

  filename = sys.argv[1]

  with open(filename, 'r') as f:
    parser = myparser.parser
    text = f.read()
    ast = parser.parse(text, lexer=lexer.lexer)
    if ast is not None:
      ast.printTree()
    if not myparser.error:
      type_checker = TypeChecker()
      type_checker.visit(ast)

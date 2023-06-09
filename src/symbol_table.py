class Symbol:
  def __init__(self, name, type):
    self.name = name
    self.type = type


class VariableSymbol(Symbol):
  def __init__(self, name, type):
    super().__init__(name, type)


class SymbolTable(object):
  def __init__(self, parent, name):
    self.parent = parent
    self.name = name
    self.all_symbols = {}


  def put(self, name, symbol):
    self.all_symbols[name] = symbol


  def get(self, name):
    if self.all_symbols.__contains__(name):
      return self.all_symbols[name]
    elif self.parent:
      return self.parent.get(name)
    else:
      return None


  def getParentScope(self):
    return self.parent


  def pushScope(self, name):
    return SymbolTable(self, name)


  def popScope(self):
    return self.parent

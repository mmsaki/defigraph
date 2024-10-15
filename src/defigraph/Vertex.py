class Vertex:
  def __init__(self, name: str, decimals: int):
    self.name = name
    self.decimals = decimals

  def __repr__(self):
    return f"{self.name}"
  
  

class Indicator(object):
  def __init__(self, name, data_src=None):
    self.__data = data_src
    self.__last_updated = 0
    self.__value = 0
    self.__change = 0
    self.__variance = 0
    self.__impact= {}
    print("Economic indicator initiated:", name)

  def refreshData(self):
    if self.__data:
      #check data is newer then update it
      self.__last_updated = time.time()
      print("data refreshed to:", self.__last_updated)

  def simulate(self):
    # manually adjust the value to see the collateral effects
    ...

  def affectPod(self, target, weight):
    # we will try to map A-> B to associate the influence
    # e.g. if A changed(5%), would change -0.1% to B(by the weight of -0.02)
    Ellipsis
      
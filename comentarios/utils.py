class Utils:
  ratio = 9 / 5

  @staticmethod
  def convert(c):
    '''
      Converts the value
      Parameters:
        c - the value to convert
        scientific: whether to convert to scientifi measurements
    '''
    return (c * Utils.ratio) + 32; # Convert
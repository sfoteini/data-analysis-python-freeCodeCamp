import numpy as np

def calculate(list):
  # Raise an exception if the size of the list is not 9
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
  
  # Create a 3x3 matrix
  matrix = np.array(list).reshape((3,3))

  # Create a dictionary
  calculations = {}

  # Mean
  calculations['mean'] = [matrix.mean(axis=0).tolist(), 
                        matrix.mean(axis=1).tolist(),
                        matrix.mean()]
  
  # Variance
  calculations['variance'] = [matrix.var(axis=0).tolist(), 
                          matrix.var(axis=1).tolist(),
                          matrix.var()]

  # Standard Deviation
  calculations['standard deviation'] = [matrix.std(axis=0).tolist(), 
                        matrix.std(axis=1).tolist(),
                        matrix.std()]

  # Max
  calculations['max'] = [matrix.max(axis=0).tolist(), 
                        matrix.max(axis=1).tolist(),
                        matrix.max()]

  # Min
  calculations['min'] = [matrix.min(axis=0).tolist(), 
                        matrix.min(axis=1).tolist(),
                        matrix.min()]

  # Sum
  calculations['sum'] = [matrix.sum(axis=0).tolist(), 
                        matrix.sum(axis=1).tolist(),
                        matrix.sum()]

  return calculations
import numpy as np

def dominant_value(matrix):
  eigenvalues, _ = np.linalg.eig(matrix)
  dominant_value = eigenvalues[np.argmax(np.abs(eigenvalues))]
  return dominant_value

mat1=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(dominant_value(mat1))
def inverse_matrix(matrix):
  if np.linalg.det(matrix) == 0:
    raise ValueError("Matrix is singular and does not have an inverse.")
  else:
    return np.linalg.inv(matrix)

mat1=np.array([[8,9,3],[4,5,6],[7,8,9]])
print(inverse_matrix(mat1))
def identity_matrix(n):
  return np.eye(n)

print(identity_matrix(3))

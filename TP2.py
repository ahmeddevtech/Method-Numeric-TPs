import Functions as func

def set_vector(n):
  return [float(input(f'Enter vector element {{{i}}} : ')) for i in range(n)]

def display_vector(vect):
  print("Vector = [", ", ".join(str(v) for v in vect), "]")

def method_descente(matrix, vect_b):
    if not func.test_lower_triangular_matrix(matrix) or len(matrix) != len(vect_b):
        return -1
    x = [vect_b[0]/matrix[0][0]]
    for i in range(1,len(matrix)):
        sum = 0
        for j in range (i-1, -1, -1):
            sum = sum + matrix[i][j]*x[j]
        x.append((vect_b[i]-sum)/matrix[i][i])
    return x

def method_descente_recursive(matrix, vect_b, X):
    if not func.test_lower_triangular_matrix(matrix) or len(matrix) != len(vect_b):
        return -1
    if len(X) == len(matrix):
        return X
    if not X :
        X = [vect_b[0]/matrix[0][0]]
        return method_descente_recursive(matrix, vect_b, X)
    sum = 0
    for i in range(len(X) - 1, -1, -1):
        sum = sum + matrix[len(X)][i]*X[i]
    X.append((vect_b[len(X) -1]-sum)/matrix[len(X)][len(X)])
    return method_descente_recursive(matrix, vect_b, X)


def method_remontee(matrix, vect_b):
    if not func.test_upper_triangular_matrix(matrix) or len(matrix) != len(vect_b):
        return -1
    n = len(matrix)
    x = [0] * n
    x[n-1] = vect_b[n-1] / matrix[n-1][n-1]
    for i in range(n-2, -1, -1):
        sum = 0
        for k in range (i+1, n):
            sum = sum + matrix[i][k]*x[k]
        x[i] = ((vect_b[i]-sum)/matrix[i][i])
    return x

def method_remonte_recursive(matrix, vect_b, X=None):
    if X is None:
        X = []
    n = len(matrix)
    
    if len(X) == n:
        return X[::-1]
        
    if not X:
        X = [vect_b[n - 1] / matrix[n - 1][n - 1]]
        return method_remonte_recursive(matrix, vect_b, X)
        
    k = n - 1 - len(X)
    s = 0
    for i in range(len(X)):
        s += matrix[k][n - 1 - i] * X[i]
        
    X.append((vect_b[k] - s) / matrix[k][k])
    return method_remonte_recursive(matrix, vect_b, X)

def menu():
  matrices = []
  vectors = []
  while True:
    print('=============== Menu ==================')
    print('1- Read matrix.')
    print('2- Read vector.')
    print('3- Test descente and display result.')
    print('4- Test descente recursive and display result.')
    print('5- Test remonte and display result.')
    print('6- Test remonte recursive and display result.')
    print('7- Display matrices.')
    print('8- Display vectors.')
    print('0- Quit.')
    
    choice = int(input('Enter your choice : '))

    if choice == 1:
      rows = int(input('Enter the number of rows : '))
      cols = int(input('Enter the number of columns : '))
      matrices.append(func.set_matrix(rows, cols))
      print(f'Matrix created with index {len(matrices)}')

    elif choice == 2:
      size = int(input('Enter the size of the vector : '))
      vectors.append(set_vector(size))
      print(f'Vector created with index {len(vectors)}')

    elif choice == 3:
      if not matrices or not vectors:
        print('You need at least one matrix and one vector first!')
        continue
      print(f'Available matrices: 1 to {len(matrices)}')
      m_idx = int(input('Select matrix index : ')) - 1
      print(f'Available vectors: 1 to {len(vectors)}')
      v_idx = int(input('Select vector index : ')) - 1
      
      res = method_descente(matrices[m_idx], vectors[v_idx])
      if res == -1:
        print('Error: Matrix is not lower triangular or dimensions do not match!')
      else:
        print('Result vector X:')
        display_vector(res)

    elif choice == 4:
      if not matrices or not vectors:
        print('You need at least one matrix and one vector first!')
        continue
      print(f'Available matrices: 1 to {len(matrices)}')
      m_idx = int(input('Select matrix index : ')) - 1
      print(f'Available vectors: 1 to {len(vectors)}')
      v_idx = int(input('Select vector index : ')) - 1
      
      res = method_descente_recursive(matrices[m_idx], vectors[v_idx], [])
      if res == -1:
        print('Error: Matrix is not lower triangular or dimensions do not match!')
      else:
        print('Result vector X:')
        display_vector(res)

    elif choice == 5:
      if not matrices or not vectors:
        print('You need at least one matrix and one vector first!')
        continue
      print(f'Available matrices: 1 to {len(matrices)}')
      m_idx = int(input('Select matrix index : ')) - 1
      print(f'Available vectors: 1 to {len(vectors)}')
      v_idx = int(input('Select vector index : ')) - 1
      
      res = method_remontee(matrices[m_idx], vectors[v_idx])
      if res == -1:
        print('Error: Matrix is not upper triangular or dimensions do not match!')
      else:
        print('Result vector X:')
        display_vector(res)

    elif choice == 6:
      if not matrices or not vectors:
        print('You need at least one matrix and one vector first!')
        continue
      print(f'Available matrices: 1 to {len(matrices)}')
      m_idx = int(input('Select matrix index : ')) - 1
      print(f'Available vectors: 1 to {len(vectors)}')
      v_idx = int(input('Select vector index : ')) - 1
      
      res = method_remonte_recursive(matrices[m_idx], vectors[v_idx])
      if res == -1:
        print('Error: Matrix is not upper triangular or dimensions do not match!')
      else:
        print('Result vector X:')
        display_vector(res)

    elif choice == 7:
      if not matrices:
        print('No matrices stored yet.')
      else:
        for i, mat in enumerate(matrices):
          print(f'--- Matrix {i + 1} ---')
          func.display_matrix(mat)

    elif choice == 8:
      if not vectors:
        print('No vectors stored yet.')
      else:
        for i, vect in enumerate(vectors):
          print(f'--- Vector {i + 1} ---')
          display_vector(vect)

    elif choice == 0:
      break
    else:
      print('There is no operation with this input!')



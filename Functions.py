# ========================= square_matrix ========================= (lire et afficher)
def set_square_matrix(n):
  return [[int(input(f'Enter matrix {{{row}; {col}}} : ')) for col in range(n)] for row in range(n)]

# Solution 1
def display_square_matrix(matrix):
  print(f"Here is the square matrix {{N = {len(matrix)}}} : ")
  for i in range(0,len(matrix)):
    for j in range(0,len(matrix)):
      print(matrix[i][j], end=" ")
    print()

# Solution 2
def display_square_matrix_N(matrix, N):
  print(f"Here is the square matrix {{N = {N}}} : ")
  for i in range(0,N):
      for j in range(0,N):
        print(matrix[i][j], end=" ")
      print()

# ========================= identity_matrix ========================= (lire et afficher)

def set_identity_matrix(n):
  return [[0 if row != col else 1 for col in range(n)] for row in range(n)]

# Solution 1
def display_identity_matrix(matrix):
  print(f"Here is the identity matrix of order {{N = {len(matrix)}}} : ")
  for i in range(0,len(matrix)):
    for j in range(0,len(matrix)):
      print(matrix[i][j], end=" ")
    print()

# Solution 2
def display_identity_matrix_N(matrix, N):
  print(f"Here is the identity matrix of order {{N = {N}}} : ")
  for i in range(N):
      for j in range(N):
        print(matrix[i][j], end=" ")
      print()

# ================ addition of two matrices (same size) =============== 

def sum_two_matrices(matrix1, matrix2):
  if len(matrix1)!=len(matrix2):
    return ''
  return [[matrix1[row][col]+matrix2[row][col] for col in range(len(matrix1))] for row in range(len(matrix1))]

def sum_two_matrices_N(matrix1, matrix2, N):
  if len(matrix1)!=len(matrix2):
      return ''
  return [[matrix1[row][col]+matrix2[row][col] for col in range(N)] for row in range(N)]

def sum_two_matrices_N1_N2(matrix1, N1, matrix2, N2):
  if N1!=N2:
      return 'Matrices haven\'t the same size'
  return [[matrix1[row][col]+matrix2[row][col] for col in range(N1)] for row in range(N1)]

# ================ multiplication of two matrices ===============
def multiplication_two_matrices(matrix1, matrix2):
  if len(matrix1[0])!=len(matrix2):
    return ''
  matrix3 = [[]for row in range(0,len(matrix1))]
  for i in range(0,len(matrix1)):
      for j in range (0, len(matrix2[0])):
        multiplication = 0
        for k in range(0,len(matrix1[0])):
          multiplication += matrix1[i][k]*matrix2[k][j]
        matrix3[i].append(multiplication)
  return matrix3

def multiplication_two_matrices_dimensions(matrix1,row1,col1, matrix2,row2,col2):
  if col1!=row2:
    return ''
  matrix3 = [[]for row in range(0,row1)]
  for i in range(0,row1):
      for j in range (0, col2):
        multiplication = 0
        for k in range(0,col1):
          multiplication += matrix1[i][k]*matrix2[k][j]
        matrix3[i].append(multiplication)
  return matrix3


# ====================== Transpose of a matrix =====================
def matrix_transpose(matrix):
  matrix_t = [[] for row in range(len(matrix[0]))]
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      matrix_t[j].append(matrix[i][j])
  return matrix_t

def matrix_transpose_dimensions(matrix,rows,cols):
  matrix_t = [[] for row in range(cols)]
  for i in range(rows):
    for j in range(cols):
      matrix_t[j].append(matrix[i][j])
  return matrix_t

# ================= Test Upper Triangular Matrix =====================
def test_upper_triangular_matrix(matrix):
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      if i>j and matrix[i][j] != 0:
        return False
  return True

# ================= Test Lower Triangular Matrix =====================

def test_lower_triangular_matrix(matrix):
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      if i<j and matrix[i][j] != 0:
        return False
  return True

# ================= Test Diagonal Matrix =====================

def test_diagonal_matrix(matrix):
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      if i==j and matrix[i][j] == 0:
        counter += 1
        if counter == len(matrix):
          return False
      if i!=j and matrix[i][j] != 0:
        return False
  return True

# ================= Test Symmetric Matrix =====================

def test_symmetric_matrix(matrix):
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      if i!=j and matrix[i][j] != matrix[j][i]:
        return False
  return True

# =========================== additional functions ==============================

def set_matrix(rows, cols):
  return [[int(input(f'Enter matrix {{{row}; {col}}} : ')) for col in range(cols)] for row in range(rows)]

def set_null_matrix(rows, cols):
  return [[0 for col in range(cols)] for row in range(rows)]

def set_line_matrix(cols):
  return [int(input(f'Enter matrix {{{col}}} : ')) for col in range(cols)]

def set_colomn_matrix(rows):
  return [[int(input(f'Enter matrix {{{row}; {col}}} : ')) for col in range(1)] for row in range(rows) ]

def set_diagonal_matrix(n):
  return [[0 if row != col else int(input(f'Enter matrix {{{row}; {col}}} : ')) for col in range(n)] for row in range(n)]

def display_matrix(matrix):
  print(f"Here is the matrix {{{len(matrix)};{len(matrix[0])}}} : ")
  for i in range(0,len(matrix)):
    for j in range(0,len(matrix[0])):
      print(matrix[i][j], end=" ")
    print()

# =========================== menu ==============================

def menu():
  matrices = []
  while True:
    print('=============== Menu ==================')
    print('1- Read square matrix of order N.')
    print('2- Display square matrix of order N.')
    print('3- Display identity matrix of order N.')
    print('4- Calculat sum of two matrices.(same size)')
    print('5- Calculat multiplication of two matrices.')
    print('6- Calculat transpose of a matrix ')
    print('7- Test upper triangular matrix.')
    print('8- Test lower triangular matrix.')
    print('9- Test diagonal matrix.')
    print('10- Test symmetric matrix.')
    print('0- Quit.')
    choice = int(input('Enter your choice : '))
    if choice == 1:  #######################
      N = int(input('Enter the size of the matrix to fill it\nN = '))
      matrices.append(set_square_matrix(N))
    elif choice == 2: #######################
      if matrices:
        select = int(input(f'You have already create {len(matrices)} matrices, do you want to select one to display it or you can fill a new one ?\n1 -> select one\n2 -> fill a new one\nchoice -> '))
        if select == 1:
          index = int(input('Select the index of the matrix that you want to display\nmatrix number : '))-1
          display_square_matrix(matrices[index])
          continue
      N = int(input('Enter the size of the matrix to fill it\nN = '))
      display_square_matrix(set_square_matrix(N))
    elif choice == 3: ######################
      N = int(input('Enter the size of the identity matrix\nN = '))
      display_identity_matrix(set_identity_matrix(N))
    elif choice == 4: #######################
      if matrices:
        select = int(input(f'You have already create {len(matrices)} matrices, do you want to select two for calculate sum or you can fill a new mtrices ?\n1 -> select two\n2 -> fill a new matrices\nchoice -> '))
        if select == 1:
          index1 = int(input('Select the index of the first matrix\nfirst matrix number : '))-1
          index2 = int(input('Select the index of the second matrix\nsecond matrix number : '))-1
          res = sum_two_matrices(matrices[index1],matrices[index2])
          if res == '':
            print('Those matrices haven\'t the same size.')
          else:
            display_matrix(res)
          continue
      print('if the matrices have the same size just write the same rows and colomns number :')
      rows = int(input('Enter the rows of matrices\nrows = '))
      cols = int(input('Enter the ncolomns of matrices\ncolomns = '))
      print('Fill the first matrix : ')
      matrix1 = set_matrix(rows,cols)
      print('Fill the second matrix : ')
      matrix2 = set_matrix(rows,cols)
      res = sum_two_matrices(matrix1,matrix2)
      if res == '':
        print('Those matrices haven\'t the same size.')
      else:
        display_matrix(res)
    elif choice == 5: ####################
      if matrices:
        select = int(input(f'You have already create {len(matrices)} matrices, do you want to select two for calculate multiplication (you can select the same matrix) or you can fill a new mtrices ?\n1 -> select two\n2 -> fill a new matrices\nchoice -> '))
        if select == 1:
          index1 = int(input('Select the index of the first matrix\nfirst matrix number : '))-1
          index2 = int(input('Select the index of the second matrix\nsecond matrix number : '))-1
          res = multiplication_two_matrices(matrices[index1],matrices[index2])
          if res == '':
            print('Matrix(1) columns are different from matrix(2) rows!')
          else:
            display_matrix(res)
          continue
      rows1 = int(input('Enter the rows of the first matrix\nrows = '))
      cols1 = int(input('Enter the ncolomns of the first matrix\ncolomns = '))
      rows2 = int(input('Enter the rows of the second matrix\nrows = '))
      cols2 = int(input('Enter the ncolomns of the second matrix\ncolomns = '))
      print('Fill the first matrix : ')
      matrix1 = set_matrix(rows1,cols1)
      print('Fill the second matrix : ')
      matrix2 = set_matrix(rows2,cols2)
      res = multiplication_two_matrices(matrix1,matrix2)
      if res == '':
        print('Matrix(1) columns are different from matrix(2) rows!')
      else:
        display_matrix(res)
    elif choice == 6:  #############################
      if matrices:
        select = int(input(f'You have already create {len(matrices)} matrices, do you want to select one to calculate it transpose or you can fill a new one ?\n1 -> select one\n2 -> fill a new one\nchoice -> '))
        if select == 1:
          index = int(input('Select the index of the matrix\nmatrix number : '))-1
          display_square_matrix(matrix_transpose(matrices[index]))
          continue
      N = int(input('Enter the size of the matrix to fill it\nN = '))
      display_square_matrix(matrix_transpose(set_square_matrix(N)))
    elif choice == 7: ##################################
      if matrices:
        select = int(input(f'You have already create {len(matrices)} matrices, do you want to select one to apply upper triangular matrix test or you can fill a new one ?\n1 -> select one\n2 -> fill a new one\nchoice -> '))
        if select == 1:
          index = int(input('Select the index of the matrix\nmatrix number : '))-1
          if test_upper_triangular_matrix(matrices[index]):
            print('This matrix is an upper triangular matrix.')
          else:
            print('This matrix is not an upper triangular matrix.')
          continue
      N = int(input('Enter the size of the matrix to fill it\nN = '))
      if test_upper_triangular_matrix(set_square_matrix(N)):
        print('This matrix is an upper triangular matrix.')
      else:
        print('This matrix is not an upper triangular matrix.')
    elif choice == 8: #########################################
      if matrices:
        select = int(input(f'You have already create {len(matrices)} matrices, do you want to select one to apply lower triangular matrix test or you can fill a new one ?\n1 -> select one\n2 -> fill a new one\nchoice -> '))
        if select == 1:
          index = int(input('Select the index of the matrix\nmatrix number : '))-1
          if test_lower_triangular_matrix(matrices[index]):
            print('This matrix is an lower triangular matrix.')
          else:
            print('This matrix is not an lower triangular matrix.')
          continue
      N = int(input('Enter the size of the matrix to fill it\nN = '))
      if test_lower_triangular_matrix(set_square_matrix(N)):
        print('This matrix is an lower triangular matrix.')
      else:
        print('This matrix is not an lower triangular matrix.')
    elif choice == 9: ######################################
      if matrices:
        select = int(input(f'You have already create {len(matrices)} matrices, do you want to select one to apply diagonal matrix test or you can fill a new one ?\n1 -> select one\n2 -> fill a new one\nchoice -> '))
        if select == 1:
          index = int(input('Select the index of the matrix\nmatrix number : '))-1
          if test_diagonal_matrix(matrices[index]):
            print('This matrix is a diagonal matrix.')
          else:
            print('This matrix is not a diagonal matrix.')
          continue
      N = int(input('Enter the size of the matrix to fill it\nN = '))
      if test_diagonal_matrix(set_square_matrix(N)):
        print('This matrix is a diagonal matrix.')
      else:
        print('This matrix is not a diagonal matrix.')
    elif choice == 10: ############################################
      if matrices:
        select = int(input(f'You have already create {len(matrices)} matrices, do you want to select one to apply symmetric matrix test or you can fill a new one ?\n1 -> select one\n2 -> fill a new one\nchoice -> '))
        if select == 1:
          index = int(input('Select the index of the matrix\nmatrix number : '))-1
          if test_symmetric_matrix(matrices[index]):
            print('This matrix is a symmetric matrix.')
          else:
            print('This matrix is not a symmetric matrix.')
          continue
      N = int(input('Enter the size of the matrix to fill it\nN = '))
      if test_symmetric_matrix(set_square_matrix(N)):
        print('This matrix is a symmetric matrix.')
      else:
        print('This matrix is not a symmetric matrix.')
    elif choice == 0: ##########################################
      break
    else:
      print('There is no operation with this input!')
      break
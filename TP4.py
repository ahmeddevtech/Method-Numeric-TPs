from Functions import set_matrix, set_identity_matrix
from TP2 import method_remontee, method_descente, set_vector, display_vector
from TP3 import afficher_system

def afficher_matrix(matrix):
    for i in range(len(matrix)):
        x = [matrix[i][j] for j in range(len(matrix[i]))]
        print(x)

def decomposition_LU (matrix, n):
  print("  A  =  L  *  U")
  print()
  U = matrix
  L = set_identity_matrix(n)
  print("la Matrice U0 : ")
  afficher_matrix(U)
  print()
  print("la Matrice L0 : ")
  afficher_matrix(L)
  for k in range(n):
    pivot = matrix[k][k]
    for i in range(k+1, n):
      q = U[i][k]
      U[i][k] = 0
      L[i][k] = q/pivot
      for j in range(k+1, n):
        U[i][j] = U[i][j] - U[k][j]*(q/pivot)
    if k != n-1 :
      print()
      print(f"****** Iteration k = {k+1} *******")
      print(f"    * Pivot = {pivot} *")
      print(f"la Matrice U{k+1} : ")
      afficher_matrix(U)
      print()
      print(f"la Matrice L{k+1} : ")
      afficher_matrix(L)
    else:
      print()
      print(f"la Matrice U : ")
      print()
      afficher_matrix(U)
      print()
      print(f"la Matrice L : ")
      print()
      afficher_matrix(L)
  return U, L

def descente_L(matrix_L, vect_b):
  print("le system reduit : ")
  print()
  afficher_system(matrix_L, vect_b)
  print()
  vect_y = method_descente(matrix_L, vect_b)
  print(" vector Y :")
  display_vector(vect_y)
  return vect_y


def remontee_U(matrix_U, vect_Y):
  print("le system reduit : ")
  print()
  afficher_system(matrix_U, vect_Y)
  print()
  vect_x = method_remontee(matrix_U, vect_Y)
  print(" vector X :")
  display_vector(vect_x)
  return vect_x


def decomposition_LU_total(matrix, n, vect_b):
  print("-------------- 1- Decomposition -------------")
  U, L = decomposition_LU(matrix, n)
  print()
  print("-------------- 2- Resoudre Ly = b par desente -------------")
  vect_y = descente_L(L, vect_b)
  print()
  print("-------------- 3- Resoudre Ux = y par remontee -------------")
  remontee_U(U, vect_y)

# matrix = [[1,2,3],[1,1,2],[1,1,1]]
# vect_b = [2,0,1]

# decomposition_LU_total(matrix, 3, vect_b)

def menu():
    matrices = []
    vectors = []
    while True:
        print('=============== Menu TP4 ==================')
        print('1- Afficher system (matrix, vectB).')
        print('2- Lire system (matrix, vectB).')
        print('3- Decomposition LUet resudre le system.')
        print('0- Quit.')
        
        choice = int(input('Enter your choice : '))
        if choice == 1:
            if not matrices or not vectors:
                print('You need at least one matrix and one vector first!')
                continue
            print(f'Available matrices: 1 to {len(matrices)}')
            m_idx = int(input('Select matrix index : ')) - 1
            print(f'Available vectors: 1 to {len(vectors)}')
            v_idx = int(input('Select vector index : ')) - 1
            
            print('--- Le Système ---')
            afficher_system(matrices[m_idx], vectors[v_idx])

        elif choice == 2:
            rows = int(input('Enter the number of rows : '))
            cols = int(input('Enter the number of columns : '))
            print('--- Read Matrix A ---')
            matrices.append(set_matrix(rows, cols))
            print(f'Matrix created with index {len(matrices)}')
            
            size = int(input('Enter the size of vector B : '))
            print('--- Read Vector B ---')
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
            decomposition_LU_total(matrices[m_idx], len(matrices[m_idx]), vectors[v_idx])
        elif choice == 0:
            break
        else:
            print('There is no operation with this input!')


def menu_v2():
    matrices = []
    vectors = []
    Lower_matrices = []
    Upper_matrices = []
    Y_vectors = []
    while True:
        print('=============== Menu TP4 ==================')
        print('1- Afficher system (matrix, vectB).')
        print('2- Lire system (matrix, vectB).')
        print('3- Decomposition LU.')
        print('4- Resoudre Ly = b par desente. ')
        print('5- Resoudre Ux = y par remontee.')
        print('0- Quit.')
        
        choice = int(input('Enter your choice : '))
        if choice == 1:
            if not matrices or not vectors:
                print('You need at least one matrix and one vector first!')
                continue
            print(f'Available matrices: 1 to {len(matrices)}')
            m_idx = int(input('Select matrix index : ')) - 1
            print(f'Available vectors: 1 to {len(vectors)}')
            v_idx = int(input('Select vector index : ')) - 1
            
            print('--- Le Système ---')
            afficher_system(matrices[m_idx], vectors[v_idx])

        elif choice == 2:
            rows = int(input('Enter the number of rows : '))
            cols = int(input('Enter the number of columns : '))
            print('--- Read Matrix A ---')
            matrices.append(set_matrix(rows, cols))
            print(f'Matrix created with index {len(matrices)}')
            
            size = int(input('Enter the size of vector B : '))
            print('--- Read Vector B ---')
            vectors.append(set_vector(size))
            print(f'Vector created with index {len(vectors)}')
        elif choice == 3:
            if not matrices:
                print('You need at least one matrix first!')
                continue
            print(f'Available matrices: 1 to {len(matrices)}')
            m_idx = int(input('Select matrix index : ')) - 1
            U, L = decomposition_LU(matrices[m_idx], len(matrices[m_idx]))
            Lower_matrices.append(L)
            Upper_matrices.append(U)
            print(f'Lower matrices arr has stored on the L matrix with index {len(Lower_matrices)}')
            print(f'Upper matrices arr has stored on the U matrix with index {len(Upper_matrices)}')
        elif choice == 4:
            if not Lower_matrices or not vectors:
                print('You need at least one L matrix and one B vector first!')
                continue
            print('make sure to chose the same indexes for the L matrix and b vector : ')
            print(f'Available Lower matrices: 1 to {len(Lower_matrices)}')
            L_idx = int(input('Select L matrix index : ')) - 1
            print(f'Available vectors: 1 to {len(vectors)}')
            v_idx = int(input('Select vector index : ')) - 1
            vect_Y = descente_L(Lower_matrices[L_idx], vectors[v_idx])
            Y_vectors.append(vect_Y)
            print(f'Y vector has stored on the Y vectors with index {len(Y_vectors)}')

        elif choice == 5:
            if not Upper_matrices or not Y_vectors:
                print('You need at least one U matrix and one Y vector first!')
                continue
            print('make sure to chose the same indexes for the U matrix and Y vector : ')
            print(f'Available Upper matrices: 1 to {len(Upper_matrices)}')
            U_idx = int(input('Select U matrix index : ')) - 1
            print(f'Available Y vectors: 1 to {len(Y_vectors)}')
            Y_idx = int(input('Select vector index : ')) - 1
            remontee_U(Upper_matrices[U_idx], Y_vectors[Y_idx])

        elif choice == 0:
            break
        else:
            print('There is no operation with this input!')

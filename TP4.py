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


def remontee_L(matrix_U, vect_Y):
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
  remontee_L(U, vect_y)

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
        print('3- Decomposition LU.')
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


menu()
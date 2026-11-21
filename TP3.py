from TP2 import method_remontee, set_vector
from Functions import test_upper_triangular_matrix, set_matrix

def afficher_system(matrix, vectB):
    for i in range(len(matrix)):
        x = [matrix[i][j] for j in range(len(matrix[i]))]
        print(x, f"   [{vectB[i]}]")

def triangularisation(matrix, vectB):
    n = len(matrix)
    if n != len(vectB) or len(matrix) != len(matrix[0]):
        return -1
    print(f"le system :")
    print()
    afficher_system(matrix, vectB)
    print()
    for k in range (n-1):
        pivot = matrix[k][k]
        if pivot != 0 :
            for i in range(k+1, n):
                q = matrix[i][k]
                matrix[i][k] = 0
                vectB[i] = vectB[i] - (q/pivot)*vectB[k]
                for j in range(k+1, n):
                    matrix[i][j] = matrix[i][j] - matrix[k][j]*(q/pivot)
        else:
            return -1
        print(f"iteration number K = {k+1}")
        print()
        afficher_system(matrix, vectB)
        print()
    print("--------GAUSS----------")
    print()
    afficher_system(matrix, vectB)
    return method_remontee(matrix, vectB)

def pivot_partial(matrix, vectB):
    n = len(matrix)
    if n != len(vectB) or len(matrix) != len(matrix[0]):
        return -1
    print(f"le system :")
    print()
    afficher_system(matrix, vectB)
    print()
    for k in range (n-1):
        i_pivot = k
        pivot = matrix[k][k]
        for i in range(k+1, n):
            if abs(matrix[i][k]) > abs(pivot):
                pivot = matrix[i][k]
                i_pivot = i
        if i_pivot != k:
            matrix[k], matrix[i_pivot] = matrix[i_pivot], matrix[k]
            vectB[k], vectB[i_pivot] = vectB[i_pivot], vectB[k]
        for i in range(k+1, n):
            q = matrix[i][k]
            matrix[i][k] = 0
            for j in range(k+1, n):
                matrix[i][j] = matrix[i][j] - (q/pivot)*matrix[k][j]
            vectB[i] = vectB[i] - (q/pivot)*vectB[k]
        print(f"iteration number K = {k+1}")
        print()
        afficher_system(matrix, vectB)
        print()
    print("--------GAUSS----------")
    print()
    afficher_system(matrix, vectB)
    return method_remontee(matrix, vectB)

def pivot_total(matrix, vectB):
    n = len(matrix)
    if n != len(vectB) or len(matrix) != len(matrix[0]):
        return -1
    print(f"le system :")
    print()
    afficher_system(matrix, vectB)
    print()
    pivot_col= list(range(n))
    for k in range(n-1):
        pivot = 0
        for i in range(k, n):
            for j in range(k, n):
                if abs(matrix[i][j]) > abs(pivot):
                    pivot = matrix[i][j]
                    i_pivot = i
                    j_pivot = j
        if i_pivot != k:
            matrix[k], matrix[i_pivot] = matrix[i_pivot], matrix[k]
            vectB[k], vectB[i_pivot] = vectB[i_pivot], vectB[k]
        if j_pivot != k:
            for j in range(k, n):
                matrix[j][k], matrix[j][j_pivot] = matrix[j][j_pivot], matrix[j][k]
            pivot_col[k], pivot_col[j_pivot] = pivot_col[j_pivot], pivot_col[k]
        for i in range(k+1, n):
            q = matrix[i][k]
            matrix[i][k] = 0
            for j in range(k+1, n):
                matrix[i][j] = matrix[i][j] - (q/pivot)*matrix[k][j]
            vectB[i] = vectB[i] - (q/pivot)*vectB[k]
        print(f"iteration number K = {k+1}")
        print()
        afficher_system(matrix, vectB)
        print()
    print("--------GAUSS----------")
    print()
    afficher_system(matrix, vectB)
    if method_remontee(matrix, vectB) == -1:
        return -1
    else:
        x = method_remontee(matrix, vectB)
        x_final = [0]*len(x)
        for i in range(n):
            x_final[pivot_col[i]] = x[i]
        return x_final

#------------------- additionneles --------------------
def switch_line(matrix, vectB, index1, index2):
    matrix[index1], matrix[index2] = matrix[index2], matrix[index1]
    vectB[index1], vectB[index2] = vectB[index2], vectB[index1]


def switch_colomn(matrix, pivot_col, index1, index2):
    n = len(matrix)
    for element_in_col in range(index1, n):
        matrix[element_in_col][index1], matrix[element_in_col][index2] = matrix[element_in_col][index2], matrix[element_in_col][index1]
    pivot_col[index1], pivot_col[index2] = pivot_col[index2], pivot_col[index1]

def pivot_partial_v2(matrix, vectB):
    n = len(matrix)
    if n != len(vectB) or len(matrix) != len(matrix[0]):
        return -1
    print(f"le system :")
    print()
    afficher_system(matrix, vectB)
    print()
    for k in range (n-1):
        i_pivot = k
        pivot = matrix[k][k]
        for i in range(k+1, n):
            if abs(matrix[i][k]) > abs(pivot):
                pivot = matrix[i][k]
                i_pivot = i
        if i_pivot != k:
            switch_line(matrix, vectB, k, i_pivot)
        for i in range(k+1, n):
            q = matrix[i][k]
            matrix[i][k] = 0
            for j in range(k+1, n):
                matrix[i][j] = matrix[i][j] - (q/pivot)*matrix[k][j]
            vectB[i] = vectB[i] - (q/pivot)*vectB[k]
        print(f"iteration number K = {k+1}")
        print()
        afficher_system(matrix, vectB)
        print()
    print("--------GAUSS----------")
    print()
    afficher_system(matrix, vectB)
    return method_remontee(matrix, vectB)

def pivot_total_v2(matrix, vectB):
    n = len(matrix)
    if n != len(vectB) or len(matrix) != len(matrix[0]):
        return -1
    print(f"le system :")
    print()
    afficher_system(matrix, vectB)
    print()
    pivot_col= list(range(n))
    for k in range(n-1):
        pivot = 0
        for i in range(k, n):
            for j in range(k, n):
                if abs(matrix[i][j]) > abs(pivot):
                    pivot = matrix[i][j]
                    i_pivot = i
                    j_pivot = j
        if i_pivot != k:
            switch_line(matrix, vectB, k, i_pivot)
        if j_pivot != k:
            switch_colomn(matrix, pivot_col, k, j_pivot)
        for i in range(k+1, n):
            q = matrix[i][k]
            matrix[i][k] = 0
            for j in range(k+1, n):
                matrix[i][j] = matrix[i][j] - (q/pivot)*matrix[k][j]
            vectB[i] = vectB[i] - (q/pivot)*vectB[k]
        print(f"iteration number K = {k+1}")
        print()
        afficher_system(matrix, vectB)
        print()
    print("--------GAUSS----------")
    print()
    afficher_system(matrix, vectB)
    if method_remontee(matrix, vectB) == -1:
        return -1
    else:
        x = method_remontee(matrix, vectB)
        x_final = [0]*len(x)
        for i in range(n):
            x_final[pivot_col[i]] = x[i]
        return x_final

def menu():
    matrices = []
    vectors = []
    while True:
        print('=============== Menu TP3 ==================')
        print('1- Afficher system (matrix, vectB).')
        print('2- Lire system (matrix, vectB).')
        print('3- Pivot non null (triangularisation).')
        print('4- Pivot partial.')
        print('5- Pivot total.')
        print('6- Pivot partial (version 2).')
        print('7- Pivot total (version 2).')
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
            
            res = triangularisation(matrices[m_idx], vectors[v_idx])
            if res == -1:
                print('Error: Pivot is null or dimensions do not match!')
            else:
                print('Result vector X:', res)

        elif choice == 4:
            if not matrices or not vectors:
                print('You need at least one matrix and one vector first!')
                continue
            print(f'Available matrices: 1 to {len(matrices)}')
            m_idx = int(input('Select matrix index : ')) - 1
            print(f'Available vectors: 1 to {len(vectors)}')
            v_idx = int(input('Select vector index : ')) - 1
            
            res = pivot_partial(matrices[m_idx], vectors[v_idx])
            if res == -1:
                print('Error: Dimensions do not match!')
            else:
                print('Result vector X:', res)

        elif choice == 5:
            if not matrices or not vectors:
                print('You need at least one matrix and one vector first!')
                continue
            print(f'Available matrices: 1 to {len(matrices)}')
            m_idx = int(input('Select matrix index : ')) - 1
            print(f'Available vectors: 1 to {len(vectors)}')
            v_idx = int(input('Select vector index : ')) - 1
            res = pivot_total(matrices[m_idx], vectors[v_idx])
            if res == -1:
                print('Error: Dimensions do not match!')
            else:
                print('Result vector X:', res)

        elif choice == 6:
            if not matrices or not vectors:
                print('You need at least one matrix and one vector first!')
                continue
            print(f'Available matrices: 1 to {len(matrices)}')
            m_idx = int(input('Select matrix index : ')) - 1
            print(f'Available vectors: 1 to {len(vectors)}')
            v_idx = int(input('Select vector index : ')) - 1
            
            res = pivot_partial_v2(matrices[m_idx], vectors[v_idx])
            if res == -1:
                print('Error: Dimensions do not match!')
            else:
                print('Result vector X:', res)

        elif choice == 7:
            if not matrices or not vectors:
                print('You need at least one matrix and one vector first!')
                continue
            print(f'Available matrices: 1 to {len(matrices)}')
            m_idx = int(input('Select matrix index : ')) - 1
            print(f'Available vectors: 1 to {len(vectors)}')
            v_idx = int(input('Select vector index : ')) - 1
            res = pivot_total_v2(matrices[m_idx], vectors[v_idx])
            if res == -1:
                print('Error: Dimensions do not match!')
            else:
                print('Result vector X:', res)

        elif choice == 0:
            break
        else:
            print('There is no operation with this input!')

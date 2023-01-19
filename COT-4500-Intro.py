##Jonathan Washuta
##COT4500
##Introduction to Python/Github

import numpy as np

def intro_array():
    array = np.array([[0,0,0],[0,0,0],[0,0,0]])
##Example 1
    for i in range(0, 3):
        for j in range(0, 3):
            if i == j:
                array[i][j] = 1
            else:
                array[i][j] = 0
    
    print(array)
    print("\n")
##Example 2
    for i in range(0,3):
        for j in range(0,3):
            if i == j:
                array[i][j] = 1
            else:
                array[i][j] = 3
    
    print(array)
    print("\n")
##Example 3
    array = np.delete(array, 2, 1)

    print(array)
    print("\n")

if __name__ == "__main__":
    intro_array()
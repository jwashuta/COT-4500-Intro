import numpy as np

def intro_array():
    array = np.array([[0,0,0],[0,0,0],[0,0,0]])
    
    for i in range(0, 3):
        for j in range(0, 3):
            if i == j:
                array[i][j] = 1
            else:
                array[i][j] = 0
    
    print(str(array).replace(' [','').replace('[', '').replace(']',''))
    print("\n")

    for i in range(0,3):
        for j in range(0,3):
            if i == j:
                array[i][j] = 1
            else:
                array[i][j] = 3
    
    print(str(array).replace(' [','').replace('[', '').replace(']',''))
    print("\n")

    array = np.delete(array, 2, 1)

    print(str(array).replace(' [','').replace('[', '').replace(']',''))
    print("\n")
if __name__ == "__main__":
    intro_array()

# Pyramid shape/ Triangle shape

"""
    *
   * *
  * * *
 * * * *
* * * * *
"""

"""
    *
   ***
  *****
 *******
*********
"""

num = int(input("Ente the number of rows : "))
for i in range(0, num):
    for j in range(0, num-i-1):
        print(end=" ")
    for j in range(0, i+1):
        print("*", end=" ")
    # for j in range(0, 2*i+1):
    #     print("*", end="")
    print()

def pyramid(rows):
    for i in range(rows):
        print(' '*(rows-i-1)+"*"*(2*i+1))

print();print()

pyramid(num)
import math

#
field = list(input("Enter cells:"))

matrix = []

for i in range(3):
    matrix.append([])
    for j in range(3):
        matrix[i].append(field.pop(0))


def print_matrix():
    print("---------")
    print("|", matrix[0][0], matrix[0][1], matrix[0][2], "|")
    print("|", matrix[1][0], matrix[1][1], matrix[1][2], "|")
    print("|", matrix[2][0], matrix[2][1], matrix[2][2], "|")
    print("---------")


def is_winner(k):
    return \
        (matrix[0][0] == k and matrix[0][1] == k and matrix[0][2] == k) or \
        (matrix[1][0] == k and matrix[1][1] == k and matrix[1][2] == k) or \
        (matrix[2][0] == k and matrix[2][1] == k and matrix[2][2] == k) or \
        (matrix[0][0] == k and matrix[1][0] == k and matrix[2][0] == k) or \
        (matrix[0][1] == k and matrix[1][1] == k and matrix[2][1] == k) or \
        (matrix[0][2] == k and matrix[1][2] == k and matrix[2][2] == k) or \
        (matrix[0][0] == k and matrix[1][1] == k and matrix[2][2] == k) or \
        (matrix[0][2] == k and matrix[1][1] == k and matrix[2][0] == k)


count_x = 0
count_o = 0
for i in range(3):
    matrix.append([])
    for j in range(3):
        if matrix[i][j] == 'X':
            count_x += 1
        elif matrix[i][j] == 'O':
            count_o += 1

print_matrix()

while True:
    a, b = list(input("Enter the coordinates:").split(' '))
    numbers = ['1', '2', '3']
    if (a or b) not in numbers and a.isdigit() and b.isdigit():
        print('Coordinates should be from 1 to 3!')
    elif not a.isdigit() or not b.isdigit():
        print("You should enter numbers!")
    elif a in numbers and b in numbers:
        c = matrix[3-int(b)][int(a)-1]
        if c == 'X' or c == 'O':
            print("This cell is occupied! Choose another one!")
        else:
            matrix[3-int(b)][int(a)-1] = 'X'
            print_matrix()
            break
    else:
        break
# if (is_winner('X') is True and is_winner('O') is True) or (math.fabs(count_x - count_o) >= 2):
#     print("Impossible")
# elif is_winner('X') is True and is_winner('O') is False:
#     print("X wins")
# elif is_winner('O') is True and is_winner('X') is False:
#     print("O wins")
# elif is_winner('X') is False and is_winner('O') is False and (count_x + count_o) < 9:
#     print("Game not finished")
# else:
#     print("Draw")
#

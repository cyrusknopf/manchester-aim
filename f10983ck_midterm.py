"""
This is a stub for the comp16321 midterm.
Do not edit or delete any lines given in this file that are marked with a "(s)".
(you can move them to different lines as long as you do not change the overall structure)

Place your code below the comments marked "#Your code here".

Each method is documented to explain what work is to be placed within it.
"""


def read_mazes():#(s)
    """
        Read in the text file and save the mazes into a python list

        :return: A list of strings denoting each maze
    """

    # Your code here
    f = open("mazes.txt", "r")
    maze_strings = f.readlines()

    for L in range(len(maze_strings)):
        try:
            if maze_strings[L] == '\n':
                maze_strings.remove(maze_strings[L])
        except:
            pass
    for i in range(len(maze_strings)):
        maze_strings[i] = maze_strings[i].strip('\n')


    return (maze_strings)#(s)

def validate_mazes(maze_strings):#(s)
    """
        Validate if the input from the text file is correct based on the rules defined

        :param: list maze_strings: The list of strings denoting each maze
        :return: A list of string values in order denoting if the input
            is invalid as defined in the specification
    """

    # Your code here

    VALID = ['0', '1', 'S', 'E', ',']

    for i in maze_strings:
        for a in range(len(i)):
            if i[a] in VALID:
                continue
            else:
                index = maze_strings.index(i)
                maze_strings[index] = 'invalid'
                break
    maze_validation = maze_strings


    return (maze_validation)#(s)


def transform_input(maze_strings, maze_validation):#(s)
    """
        Transform the valid mazes into a 2d array and combine the list with the maze valid
        list as defined in the specification

        :param: list maze_strings: The list of strings denoting each maze
        :param: list maze_strings: The list of string values in order denoting if the input
            is incorrect based on the described rules
        :return: A list of 2d arrays and string values in order denoting mazes and invalid inputs as
            defined in the specification
    """

    # Your code here
    transformed_maze_validation = []
    for i in maze_validation:
        daList=[]
        if i == "invalid":
            transformed_maze_validation.append(i)
        else:
            I = i.split(",")
            for x in I:
                xiaoList=[]
                for char in x:
                    if char == "S" or char == "E":
                        xiaoList.append(char)
                    elif char == "0" or char == "1":
                        y = int(char)
                        xiaoList.append(y)
                daList.append(xiaoList)
            transformed_maze_validation.append(daList)

    return (transformed_maze_validation)#(s)


def solve_mazes(transformed_maze_validation):#(s)
    """
        Determine if each valid maze is solvable and then solve them by providing the coordinates
        in the order required to traverse the maze from start to end

        :param: The list of 2d arrays and string values in order denoting mazes and invalid inputs
        :return: A list of coordinate lists and string values in order denoting solutions, invalid inputs
            and unsolvable mazes as defined in the specification

    """

    # Your code here

    solved_transformed_maze_validation = []
    for mazeList in transformed_maze_validation:
        
        col = len(mazeList[0])

        start = [0,0]
        
        valid = True
        
        row = len(mazeList)

        for r in range(row):
            for c in range(col):
                if mazeList[r][c] == 'S':
                    if r in range(1, row) and c in range(1, col):
                        solved_transformed_maze_validation.append('unsolvable')
                        valid = False
                    
                    else:
                        start = [r, c]
                    
                    break
            
            else:
                continue
            
            break 
        
        else:
            solved_transformed_maze_validation.append(mazeList)
            valid = False
            
        if valid:
            stack = []
            rlud = [[0,1],[0,-1],[1,0],[-1,0]]
            visitedList = []
            stack.append((start[0], start[1], 0, [start[0] * col + start[1]]))
            
            for rows in range(row):
                visited = [False]*col 
                visitedList.append(visited)
            
            while len(stack) != 0:
                validPos = stack.pop(0)
                visitedList[validPos[0]][validPos[1]] = True
                
                if mazeList[validPos[0]][validPos[1]] == 'E':
                    solved_transformed_maze_validation.append(([[i//col, i%col] for i in validPos[3]]))
                    break
                
                for currentDirection in rlud:
                    nrow, ncol = validPos[0] + currentDirection[0], validPos[1] + currentDirection[1]
                    
                    if (nrow < 0 or nrow > row or ncol < 0 or ncol > col or mazeList[nrow][ncol] == 1 or visitedList[nrow][ncol]): 
                        continue
                    stack.append((nrow, ncol, validPos[2]+1, validPos[3] + [nrow * col + ncol]))
                
                else:
                    
                    if len(stack) == 0:
                        solved_transformed_maze_validation.append('unsolvable')

    return (solved_transformed_maze_validation)#(s)

if __name__ == '__main__':
    # You can place any ad-hoc testing here
    # i.e mazes = read_mazes()
    # i.e print(mazes)
    # mazes = read_mazes()
    # valid = validate_mazes(mazes)
    # transform = transform_input(mazes, valid)
    # solve = solve_mazes(transform)
    # print(solve)
    pass

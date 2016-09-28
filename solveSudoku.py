# List with "0".
zero = ["0"]

# List of digits except 0.
one2nine = ['1','2','3','4','5','6','7','8','9']

# Structure of Sudoku puzzle from top to bottom as vars string type with digits.
line0 = "908501703"
line1 = "025900641"
line2 = "700023008"
line3 = "601050374"
line4 = "053714090"
line5 = "409008512"
line6 = "897032065"
line7 = "030406080"
line8 = "140070209"

# Candidates to lines
cand_line0 = list(set(one2nine) - (set(line0) - set(zero)))
cand_line1 = list(set(one2nine) - (set(line1) - set(zero)))
cand_line2 = list(set(one2nine) - (set(line2) - set(zero)))
cand_line3 = list(set(one2nine) - (set(line3) - set(zero)))
cand_line4 = list(set(one2nine) - (set(line4) - set(zero)))
cand_line5 = list(set(one2nine) - (set(line5) - set(zero)))
cand_line6 = list(set(one2nine) - (set(line6) - set(zero)))
cand_line7 = list(set(one2nine) - (set(line7) - set(zero)))
cand_line8 = list(set(one2nine) - (set(line8) - set(zero)))

#print(cand_line0)
# List of digits in lines
list_line0 = list(line0)
list_line1 = list(line1)
list_line2 = list(line2)
list_line3 = list(line3)
list_line4 = list(line4)
list_line5 = list(line5)
list_line6 = list(line6)
list_line7 = list(line7)
list_line8 = list(line8)

# Elements in 3x3 squares
# a b c
# d e f
# g h i
a = line0[0:3] + line1[0:3] + line2[0:3]
b = line0[3:6] + line1[3:6] + line2[3:6]
c = line0[6:9] + line1[6:9] + line2[6:9]
d = line3[0:3] + line4[0:3] + line5[0:3]
e = line3[3:6] + line4[3:6] + line5[3:6]
f = line3[6:9] + line4[6:9] + line5[6:9]
g = line6[0:3] + line7[0:3] + line8[0:3]
h = line6[3:6] + line7[3:6] + line8[3:6]
i = line6[6:9] + line7[6:9] + line8[6:9]

# List of candidates to cells 3x3
cand_a = list(set(one2nine) - (set(a) - set(zero)))
cand_b = list(set(one2nine) - (set(b) - set(zero)))
cand_c = list(set(one2nine) - (set(c) - set(zero)))
cand_d = list(set(one2nine) - (set(d) - set(zero)))
cand_e = list(set(one2nine) - (set(e) - set(zero)))
cand_f = list(set(one2nine) - (set(f) - set(zero)))
cand_g = list(set(one2nine) - (set(g) - set(zero)))
cand_h = list(set(one2nine) - (set(h) - set(zero)))
cand_i = list(set(one2nine) - (set(i) - set(zero)))

# List of digits in columns
col0 = a[0:9:3] + d[0:9:3] + g[0:9:3]
col1 = a[1:9:3] + d[1:9:3] + g[1:9:3]
col2 = a[2:9:3] + d[2:9:3] + g[2:9:3]
col3 = b[0:9:3] + e[0:9:3] + h[0:9:3]
col4 = b[1:9:3] + e[1:9:3] + h[1:9:3]
col5 = b[2:9:3] + e[2:9:3] + h[2:9:3]
col6 = c[0:9:3] + f[0:9:3] + i[0:9:3]
col7 = c[1:9:3] + f[1:9:3] + i[1:9:3]
col8 = c[2:9:3] + f[2:9:3] + i[2:9:3]

# List of candidates to columns
cand_col0 = list(set(one2nine) - set(col0))
cand_col1 = list(set(one2nine) - set(col1))
cand_col2 = list(set(one2nine) - set(col2))
cand_col3 = list(set(one2nine) - set(col3))
cand_col4 = list(set(one2nine) - set(col4))
cand_col5 = list(set(one2nine) - set(col5))
cand_col6 = list(set(one2nine) - set(col6))
cand_col7 = list(set(one2nine) - set(col7))
cand_col8 = list(set(one2nine) - set(col8))

# Variables used to print the Sudoku puzzle into the terminal
puzzleTop = "╓---┬---┬---╦---┬---┬---╦---┬---┬---╖"
puzzleMidCell = "├---┼---┼---┼---┼---┼---┼---┼---┼---┤"
puzzle3Border = "╟---┼---┼---╬---┼---┼---╬---┼---┼---╢"
puzzleBottom = "╙---┴---┴---╨---┴---┴---╨---┴---┴---╜"

#dict_a = {"a0": line0[0:1]}
#print(dict_a)

#print(str(col0))
#list(col0)
#print(cand_col1)
#print(str(*cand_col2[0:1]) + " test")#,sep='')
#a[0:1] in list(set(col0))
"""print(list_line0)
print(cand_a)
print(cand_line0)
print(col0)"""

cand_e0 = list((set(one2nine) - set(col3)) & set(cand_e) & set(cand_line3))
cand_e7 = list((set(one2nine) - set(col4)) & set(cand_e) & set(cand_line5))
"""
cell_a = a
cell_b = b
cell_c = c
cell_d = d
cell_e = e
cell_f = f
cell_g = g
cell_h = h
cell_i = i
"""
def cellCandG(ID,cand_line):
    cand_cell_solve = list(set(one2nine) & set(cand_g) & set(cand_line))
    print(ID + " " + str(cand_cell_solve))

    
# (B) Function used to populate dictionary with pairs {'cell':'index of zero value in the cell'}
# Define an empty dict 'solve' = {'cellID':'index of cells with 0 (not solved) values'}
solve = {'a':'','b':'','c':'','d':'','e':'','f':'','g':'','h':'','i':''}
# List of 3x3 cellIDs in string format
zip_cell = ['a','b','c','d','e','f','g','h','i']
# List of 3x3 cellIDs
zip_d = [a,b,c,d,e,f,g,h,i]

def checkZero():
    for cellID,d in zip(zip_cell,zip_d):
        for i in range(9):
            if d[i:i + 1] == '0':
                solve[cellID] += str(i)

checkZero()
#print(solve)
# (E)

# (B)Function to find candidates to lines and columns for cells with '0' (unknown) values.
cand_line = []
cand_col = []

#def solveCell(ID,cell):
def solveCell(ID,cell):
    global cand_line
    global cand_col
    # Candidates for lines
    if ID in ('a','b','c'):
        for i in range(len(cell)):
            if cell[i:i + 1] in ('0','1','2'):
                cand_line = cand_line0
            elif cell[i:i + 1] in ('3','4','5'):
                cand_line = cand_line1
            else:
                cand_line = cand_line2
    elif ID in ('d','e','f'):
        for i in range(len(cell)):
            if cell[i:i + 1] in ('0','1','2'):
                cand_line = cand_line3
            elif cell[i:i + 1] in ('3','4','5'):
                cand_line = cand_line4
            else:
                cand_line = cand_line5
    elif ID in ('g','h','i'):
        for i in range(len(cell)):
            if cell[i:i + 1] in ('0','1','2'):
                cand_line = cand_line6
            elif cell[i:i + 1] in ('3','4','5'):
                cand_line = cand_line7
            else:
                cand_line = cand_line8

    # Candidates for columns
    if ID in ('a','d','g'):
        for i in range(len(cell)):
            if cell[i:i + 1] in ('0','3','6'):
                cand_col = cand_col0
            elif cell[i:i + 1] in ('1','4','7'):
                cand_col = cand_col1
            else:
                cand_col = cand_col2
    if ID in ('b','e','h'):
        for i in range(len(cell)):
            if cell[i:i + 1] in ('0','3','6'):
                cand_col = cand_col3
            elif cell[i:i + 1] in ('1','4','7'):
                cand_col = cand_col4
            else:
                cand_col = cand_col5
    if ID in ('c','f','i'):
        for i in range(len(cell)):
            if cell[i:i + 1] in ('0','3','6'):
                cand_col = cand_col6
            elif cell[i:i + 1] in ('1','4','7'):
                cand_col = cand_col7
            else:
                cand_col = cand_col8
    return [cand_line,cand_col]
    #print("cand_line")
    #print(cand_line)
    #print("cand_col")
    #print(cand_col)

#solveCell('a','1')
#newA,newB = solveCell('e','6')
#print(newA)
#print(newB)    
    
"""    >>> def func():
...    return [1,2,3]
...
>>> a,b,c = func()
>>> a
1
>>> b
2
>>> c
3"""
    #print(cand_line)
    #print(cand_col)
"""
cand_line = []
print(cand_line)
def solve_cell(cell,ID):
    global cand_line
    if ID == 'a':
        for i in range(len(cell)):
            if cell[i:i + 1] in ('0','1','2'):
                cand_line = cand_line0
            else:
                print(cell[i:i + 1])

solve_cell(solve_a,'a')
print(cand_line)
# (E)
"""

# (B) Function that prints lines of Sudku puzzle formed out of 3x3 squares
zip_col = [col0,col1,col2,col3,col4,col5,col6,col7,col8]

def print3x3():
    line_print = ""
    for index in range(9):
        for col in (zip_col):
            line_print += col[index:index + 1]
            if col == col8:
                line_print += "\n"
    print(line_print)
# (E)

#for k,v in solve.items():
    #print(k + " " + v)
#    solveCell(k,v)

#def cellCand(ID,cand_line):
#    cand_cell_solve = list(set(one2nine) & set(cand_e) & set(cand_line))
#    print(ID + " " cand_cell_solve)


solveCell('i','0357')
#solveCell()


# !!!!
# Formula to calculate the unknown value inside the cell (c6 for example)
cand_e0 = list((set(one2nine) - set(col3)) & set(cand_e) & set(cand_line3))



def solution(ID,cell):
    #for ID,cell in zip(zip_cell,zip_d):
    sol_line,sol_col = solveCell(ID,cell)
    cellSolution = list((set(one2nine) - set(cell)) & set(sol_col) & set(sol_line))
    print(cellSolution)


#while len(cand_cell) != 1:
    # do smth
    
#solution(a,'1')
#print(cand_c6)
# If candidate to cell is the only one - remove its value from candidates lists
"""
if len(cand_c6) == 1:
    cand_col = list(set(cand_col) - set(cand_c6))
    cand_line = list(set(cand_line) - set(cand_c6))
    print(cand_col)
    print(cand_line)"""
    
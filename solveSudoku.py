#!/usr/bin/python3

# NB! If the name of the function contains the word like 'lineD' with capital 'D' in the end,
# it means that the variable vith Digital index in its name will be used for some calculations.
# Capital 'L' in function name means 'Letter' of alphabet.


# !!!
# For testing purposes all input from the user is substituted by static values.
# This is a temporary solution!
linesInput = {
        '0':['line0',"908501703"],
        '1':['line1',"025900641"],
        '2':['line2',"700023008"],
        '3':['line3',"601050374"],
        '4':['line4',"053714090"],
        '5':['line5',"409008512"],
        '6':['line6',"897032065"],
        '7':['line7',"030406080"],
        '8':['line8',"140070209"]
}
# !!!


# List with "0".
zero = ["0"]

# List of digits except 0.
one2nine = ['1','2','3','4','5','6','7','8','9']

#line0 = line1 = line2 = line3 = line4 = line5 = line6 = line7 = line8 = ""
line0 = linesInput['0'][-1]
line1 = linesInput['1'][-1]
line2 = linesInput['2'][-1]
line3 = linesInput['3'][-1]
line4 = linesInput['4'][-1]
line5 = linesInput['5'][-1]
line6 = linesInput['6'][-1]
line7 = linesInput['7'][-1]
line8 = linesInput['8'][-1]


# (B) var_lineD()
def var_lineD():
    global line0,line1,line2,line3,line4,line5,line6,line7,line8
    line0 = linesInput['0'][-1]
    line1 = linesInput['1'][-1]
    line2 = linesInput['2'][-1]
    line3 = linesInput['3'][-1]
    line4 = linesInput['4'][-1]
    line5 = linesInput['5'][-1]
    line6 = linesInput['6'][-1]
    line7 = linesInput['7'][-1]
    line8 = linesInput['8'][-1]
# (E) var_lineD()


print("Line2 before changes: " + str(line2))


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

# (B) var_cand_lineD()
def var_cand_lineD():
    global cand_line0,cand_line1,cand_line2,cand_line3,cand_line4,cand_line5,cand_line6,cand_line7,cand_line8
    cand_line0 = list(set(one2nine) - (set(line0) - set(zero)))
    cand_line1 = list(set(one2nine) - (set(line1) - set(zero)))
    cand_line2 = list(set(one2nine) - (set(line2) - set(zero)))
    cand_line3 = list(set(one2nine) - (set(line3) - set(zero)))
    cand_line4 = list(set(one2nine) - (set(line4) - set(zero)))
    cand_line5 = list(set(one2nine) - (set(line5) - set(zero)))
    cand_line6 = list(set(one2nine) - (set(line6) - set(zero)))
    cand_line7 = list(set(one2nine) - (set(line7) - set(zero)))
    cand_line8 = list(set(one2nine) - (set(line8) - set(zero)))
# (E) var_cand_lineD()


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

# (B) var_list_lineD()
def var_list_lineD():
    global list_line0,list_line_1,list_line2,list_line3,list_line_4,list_line5,list_line_6,list_line7,list_line8
    list_line0 = list(line0)
    list_line1 = list(line1)
    list_line2 = list(line2)
    list_line3 = list(line3)
    list_line4 = list(line4)
    list_line5 = list(line5)
    list_line6 = list(line6)
    list_line7 = list(line7)
    list_line8 = list(line8)
# (E) var_list_lineD()


# Elements in 3x3 cell blocks
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

# (B) var_L()
def var_L():
    global a,b,c,d,e,f,g,h,i
    a = line0[0:3] + line1[0:3] + line2[0:3]
    b = line0[3:6] + line1[3:6] + line2[3:6]
    c = line0[6:9] + line1[6:9] + line2[6:9]
    d = line3[0:3] + line4[0:3] + line5[0:3]
    e = line3[3:6] + line4[3:6] + line5[3:6]
    f = line3[6:9] + line4[6:9] + line5[6:9]
    g = line6[0:3] + line7[0:3] + line8[0:3]
    h = line6[3:6] + line7[3:6] + line8[3:6]
    i = line6[6:9] + line7[6:9] + line8[6:9]
# (E) var_L()


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

# (B) var_cand_L()
def var_cand_L():
    global cand_a,cand_b,cand_c,cand_d,cand_e,cand_f,cand_g,cand_h,cand_i
    cand_a = list(set(one2nine) - (set(a) - set(zero)))
    cand_b = list(set(one2nine) - (set(b) - set(zero)))
    cand_c = list(set(one2nine) - (set(c) - set(zero)))
    cand_d = list(set(one2nine) - (set(d) - set(zero)))
    cand_e = list(set(one2nine) - (set(e) - set(zero)))
    cand_f = list(set(one2nine) - (set(f) - set(zero)))
    cand_g = list(set(one2nine) - (set(g) - set(zero)))
    cand_h = list(set(one2nine) - (set(h) - set(zero)))
    cand_i = list(set(one2nine) - (set(i) - set(zero)))
# (E) var_cand_L()


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

# (B) var_colD()
def var_colD():
    global col0,col1,col2,col3,col4,col5,col6,col7,col8
    col0 = a[0:9:3] + d[0:9:3] + g[0:9:3]
    col1 = a[1:9:3] + d[1:9:3] + g[1:9:3]
    col2 = a[2:9:3] + d[2:9:3] + g[2:9:3]
    col3 = b[0:9:3] + e[0:9:3] + h[0:9:3]
    col4 = b[1:9:3] + e[1:9:3] + h[1:9:3]
    col5 = b[2:9:3] + e[2:9:3] + h[2:9:3]
    col6 = c[0:9:3] + f[0:9:3] + i[0:9:3]
    col7 = c[1:9:3] + f[1:9:3] + i[1:9:3]
    col8 = c[2:9:3] + f[2:9:3] + i[2:9:3]
# (E) var_colD()


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

# (B) var_cand_colD()
def var_cand_colD():
    cand_col0 = list(set(one2nine) - set(col0))
    cand_col1 = list(set(one2nine) - set(col1))
    cand_col2 = list(set(one2nine) - set(col2))
    cand_col3 = list(set(one2nine) - set(col3))
    cand_col4 = list(set(one2nine) - set(col4))
    cand_col5 = list(set(one2nine) - set(col5))
    cand_col6 = list(set(one2nine) - set(col6))
    cand_col7 = list(set(one2nine) - set(col7))
    cand_col8 = list(set(one2nine) - set(col8))
# (E) var_cand_colD()


#
dictCand_cell = {'a':cand_a,'b':cand_b,'c':cand_c,'d':cand_d,'e':cand_e,'f':cand_f,'g':cand_g,'h':cand_h,'i':cand_i}


#tries = 0
#for cand_i in (cand_a,cand_b,cand_c,cand_d,cand_e,cand_f,cand_g,cand_h,cand_i):
#    tries += len(cand_i)

print("Start.......")
#print(tries)
#print(dictCand_cell['a'])
#print(len(cand_a))


# (B) checkZero()
# Function used to populate dictionary with pairs {'cell':'index of zero value in the cell'}
# Define an empty dict 'solve' = {'cellID':'index of cells with 0 (not solved) values'}
solve = {'a':'','b':'','c':'','d':'','e':'','f':'','g':'','h':'','i':''}
# List of 3x3 cellIDs in string format
zip_cell = ['a','b','c','d','e','f','g','h','i']

# List of 3x3 cellIDs
zip_d = [a,b,c,d,e,f,g,h,i]

# Number of cycles to run the solving algorithm.
# It should be a dynamic value because within one cycle we can find solution
# for several cells at once. 'cycleNumber' is updated automatically
# using function massupdate() later to the bottom.
cycleNumber = 0

def checkZero():
    global cycleNumber
    for cellID,d in zip(zip_cell,zip_d):
        for i in range(9):
            if d[i:i + 1] == '0':
                cycleNumber += 1
                return cycleNumber
                solve[cellID] += str(i)
# (E) checkZero()


checkZero()
print(cycleNumber)
print(solve)
#for key,value in solve.items():
#    print(key, value)
#print(solve)
# (E)


# (B) solveCell(ID,cell)
# Function to find candidates to lines and columns for cells with '0' (unknown) values.
cand_line = []
cand_col = []

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
# (E) solveCell(ID,cell)


# (B) solution(ID,cell)
# Function that looks for the candidates to cell with cellID = ID and index = cell
def solution(ID,cell):
    sol_line,sol_col = solveCell(ID,cell)
    sol_cand = dictCand_cell[ID]
    cellSolution = list((set(sol_line) & set(sol_col)) & set(sol_cand))
    # We need to convert a list to a string.
    cellSolution = ''.join(cellSolution)
    #print("Candidate(s) for cell " + ID + ":" + cell + " is(are) " + str(cellSolution))
    return cellSolution
    #print(cellSolution)
# (E) solution(ID,cell)


#solution('e','2')


###
#cycleNumber = 0
#for key in solve.keys()
#    print(len())
#print("number of cycles equals to " + )
###
"""
for ID in cellID:
    for cell in cellIndex:
        solution(ID,cell)

ID = 'e'
print(dictCand_cell[ID])


cycleCount = 0
while cycleCount <= tries:
    try to solve the puzzle using solution(ID,cell) & for loop
    cycleCount += 1

"""


# (B) lineD_find(ID,cell)
# Function used to update the content of the cell with solved value using logic explained below.
# Logic of 3x3 cell blocks and their numeric index:
#         a          b          c
#   +==========+==========+==========+
#   | 00 01 02 | 03 04 05 | 06 07 08 |
# a | 10 11 12 | 13 14 15 | 16 17 18 | c
#   | 20 21 22 | 23 24 25 | 26 27 28 |
#   +----------+----------+----------+
#   | 30 31 32 | 33 34 35 | 36 37 38 |
# d | 40 41 42 | 43 44 45 | 46 47 48 | f
#   | 50 51 52 | 53 54 55 | 56 57 58 |
#   +----------+----------+----------+
#   | 60 61 62 | 63 64 65 | 66 67 68 |
# g | 70 71 72 | 73 74 75 | 76 77 78 | i
#   | 80 81 82 | 83 84 85 | 86 87 88 |
#   +==========+==========+==========+
#         g          h          i
#

# Dictionary cellBasis describes the elements in 3x3 cells -> a-i <- using simple arithmetic module 3 based
cellBasis =    {'a':'00',
                'b':'03',
                'c':'06',
                'd':'30',
                'e':'33',
                'f':'36',
                'g':'60',
                'h':'63',
                'i':'66'}

#print(str(cellBasis['f']))
# Function returns as a result a digital code for element in cell(ID) and index = cell
# for example, cell 'g5' will have a digital index '72' split into '7' and '2' for further use.
def lineD_find(ID,cell):
    in_line_index = int(cellBasis[ID]) + int(cell) % 3 + 10 * (int(cell) // 3)
    #print(in_line_index)
    lineDindex = str(in_line_index)[:1]
    symbolIndex = str(in_line_index)[-1]
    if len(str(in_line_index)) > 2:
        print("Something has gone wrong with function 'lineD_find'!")
    return lineDindex, symbolIndex
# (E) lineD_find(ID,cell)


lnx,sbx = lineD_find('c',7)
print(lnx, sbx)


# (B) update_var_lineD(lineD,symbol,symValue)
# Function that updates the content of linesInput dictionary with solved values.
# After such update we need  to run the massUpdate function to update all other dependant values.
def update_var_lineD(lineD,symbol,symValue):
    lineTemp = linesInput[str(lineD)][-1]
    lineTemp = lineTemp[:symbol] + str(symValue) + lineTemp[symbol + 1:]
    print(lineTemp[:symbol])
    print(str(symValue))
    linesInput[str(lineD)][-1] = lineTemp
    print(lineTemp)
# (E) update_var_lineD(lineD,symbol,symValue)


solX = str(solution('c','7'))
print(len(solX))
print("Test for c7")
update_var_lineD(str(lnx),int(sbx),str(solX))
#update_var_lineD('2',7,'5')


# (B) massUpdate()
# Function that updates all the vars that we need to solve the puzzle.
# After each cycle their values should be updated with newer ones.
def massUpdate():
    var_lineD()
    var_list_lineD()
    var_cand_lineD()
    var_L()
    var_cand_L()
    var_colD()
    var_cand_colD()
    checkZero()
# (E) massUpdate()


#massUpdate()

#"""
# If len(result) == 1 then update the lines, but if not - run massUpdate() But how???
cyclesUsed = 0
for key in solve:
    for value in solve[key]:
        #print(key, value)
        result = solution(key,value)
        result = str(result)
        print(result)
        if len(result) == 1:
            lineX,symbolX = lineD_find(key,value)
            update_var_lineD(str(lineX),int(symbolX),result)
        else:
            cyclesUsed += 1
            massUpdate()
        print(cyclesUsed)
#"""
print(linesInput)


#cellID = ('a','b','c','d','e','f','g','h','i')
#cellIndex = ('0','1','2','3','4','5','6','7','8')
#linesInput['2'][-1] = '700023058'
#print("After changes: " + line2)
#print(linesInput['2'][-1])


# Start the automation process
#checkZero()
#solution()
#if len solution == 1
#updateLineInput
#recreate all cand_x vars


# (B)
# The start of solution algorithm
##while True:
#     do_something()
#     if condition():
#        break
#while True:
#	tries = cycleNumber
#    solution
#	tries -= 1
#	if tries == 0:
#		break
#		print("We failed to solve the puzzle!")
#print("Cycles used for solution " + cyclesUsed)
# (E)




# # FIrst take the inputs
sequence1 = input()
sequence2 = input()

# initialize a function
def lcso(sequence1, sequence2):
    length_of_s1 = len(sequence1)
    length_of_s2 = len(sequence2)

    minimum_lengtho_s11 = length_of_s1
    minimum_lengtho_s21 = length_of_s2

    #as we using the dynamic programming approach create a dp tableo
    d_table = []
    for i in range(length_of_s1+1):  # crete the rows
        row = []
        for j in range(length_of_s2+1):  # and col
            row.append(0)  
        d_table.append(row)


    #As the dp tale is done, let's fill it
    for i in range (1, length_of_s1+1):
        for j in range (1,length_of_s2+1):
            if sequence1[i - 1] == sequence2[j-1]:
                d_table[i][j]   = d_table[i-1][j-1]+1
            else:
                d_table[i][j] = max(d_table[i-1][j], d_table[i][j-1])

    
    for i in range (length_of_s1+1):
        for j in range (length_of_s2+1):
            if d_table[i][j] ==d_table[length_of_s1][length_of_s2]:
                if i +j < minimum_lengtho_s11+minimum_lengtho_s21:
                    minimum_lengtho_s11 = i
                    minimum_lengtho_s21=j

    return d_table[length_of_s1][length_of_s2], minimum_lengtho_s11+minimum_lengtho_s21

length, minimum_length = lcso(sequence1, sequence2)
print(length)
print(minimum_length)
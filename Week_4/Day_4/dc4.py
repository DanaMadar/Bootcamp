matrix = '7i3Tsih%xi #sM $a #t%^r'
def read():
    text = ''
    for j in range(0,3):
        for i in range(j,len(matrix),3):
            if matrix[i].isalpha():
                text += matrix[i] 
            else:
                k= i+3
                if k <= len(matrix)-1:
                    if matrix[k].isalpha() == False:
                        text += ' '
                else:
                   continue 

    return text
print(read())    
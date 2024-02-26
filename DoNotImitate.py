go = 1
list = []
count = 0
while go == 1:
    count = count + 1 
    try:
        add = int(input(f"roll {count}: "))
    except:
       count = count - 1
    if add == "end":
        go = 0
    else:
     list.append(add)

c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0
c7 = 0
c8 = 0
c9 = 0
c10 = 0
c11 = 0
c12 = 0
c13 = 0
c14 = 0
c15 = 0
c16 = 0
c17 = 0
c18 = 0
c19 = 0
c20 = 0

for i in range(list):
    if list[i] == 1:
        c1 = c1 + 1
    elif list[i] == 2:
       c2 = c2 +1
    elif list[i] == 3:
       c3 = c3 +1
    elif list[i] == 4:
       c4 = c4 +1
    elif list[i] == 5:
       c5 = c5 +1
    elif list[i] == 6:
       c6 = c6 +1
    elif list[i] == 7:
       c7 = c7 +1
    elif list[i] == 8:
       c8 = c8 +1
    elif list[i] == 9:
       c9 = c9 +1
    elif list[i] == 10:
       c10 = c10 +1
    elif list[i] == 11:
       c11 = c11 +1
    elif list[i] == 12:
       c12 = c12 +1
    elif list[i] == 13:
       c13 = c13 +1
    elif list[i] == 14:
       c14 = c14 +1
    elif list[i] == 15:
       c15 = c15 +1
    elif list[i] == 16:
       c16 = c16 +1
    elif list[i] == 17:
       c17 = c17 +1
    elif list[i] == 18:
       c18 = c18 +1
    elif list[i] == 19:
       c19 = c19 +1
    elif list[i] == 20:
       c20 = c20 +1

print(c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,c20)

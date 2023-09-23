# IMPORTING CSV
import csv

'''studentdetail=[[student0,00,False],[student1,11,True],[student2,22,False]
student3,33,False
student4,44,False
student5,55,False
,[student6,66,False],[student7,77,False],[student8,88,True],[student9,99,False]]'''


def details(stu_id):
    l = []
    # READING ALL DATA TO A NESTED LIST
    # EXAMPLE :[['student0', '00', 'False'], ['student1', '11', 'False'],...]
    with open('studentdetails.csv', 'r') as fo:
        reader = csv.reader(fo)
        for i in reader:
            if (i != []):
                l.append(i)
    # MODIFYING THE NESTED LIST, AND CHANGING FALSE TO TRUE
    for ls in l:
        if (ls[1] == stu_id):
            ls[2] = True
    # WRITING THE MODIFIED LIST INTO THE FILE
    with open('studentdetails.csv', 'w') as fo:
        w = csv.writer(fo)
        w.writerows(l)
        print(" UPDATED SUCCESSFULLY ")


def reset():
    with open('studentdetails.csv', 'r') as fo:
        csv_reader = csv.reader(fo)
        list_of_csv = list(csv_reader)
        M = list_of_csv
        l = []
        for j in M:
            if j != []:
                l.append(j)
        for i in l:
            if i[2] == str(True):
                i[2] = str(False)
    with open('studentdetails.csv', 'w') as fo2:
        N = csv.writer(fo2)
        N.writerows(M)

    with open("votes.csv", "w") as fo4:
        J = csv.writer(fo4)
        heading = ["CANDIDATES", "ID", "CLASS", "VOTES", "POST"]
        J.writerow(heading)
    print("------------THE DETAILS OF THE STUDENTS AND THE CANDIDATES HAS BEEN RESET------------")


# LISTS FOR STORING DETAILS OF CANDIDATES IN A NESTED LIST
presidents = []
artsclubsecs = []
mgznedi = []
sprtscap = []
vpresidents = []
vartsclubsecs = []
vmgznedi = []
vsprtscap = []


# VOTE ADDING FOR ALL THE CANDIDATES
def votechoice(m):
    q = []
    print("\n")
    for i in m:
        print("\n")
        print(i[1], i[0])
        q.append(i[1])
    print("\n")
    o = int(input("ENTER THE CANDIDATE'S ID YOU WISH TO VOTE FOR: "))
    if o in q:
        for i in m:
            if i[1] == o:
                i[3] += 1
        print("----YOUR VOTE HAS BEEN SAVED----")
    else:
        print(" INVALID CHOICE ! ")


# FUNCTION TO DISPLAY ANY CSV FILE
def display(file):
    import csv
    reader = csv.reader(open(file, 'r'))
    mock_data = []
    for row in reader:
        mock_data.append(row)

    header = mock_data.pop(0)

    def fixed_length(text, length):
        if len(text) > length:
            text = text[:length]
        elif len(text) < length:
            text = (text + " " * length)[:length]
        return text

    def draw_table(data):
        print('-' * 92)
        print('| ', end=" ")
        for column in header:
            print(fixed_length(column, 15), end=" | ")
        print()
        print("-" * 92)

        for row in data:
            print("| ", end=" ")
            for column in row:
                print(fixed_length(column, 15), end=" | ")
            print()
        print("-" * 92)

    draw_table(mock_data)


# TO FIND THE MAXIMUM NO.OF VOTES IN THE NESTED LIST AND RETURNS
# THE ENTIRE DETAILS OF THE CANDIDATE
def maxvotes(n):
    maxe = -1
    maxele = []
    l = len(n)
    for i in range(l):
        if n[i][3] > maxe:
            maxe = n[i][3]
            maxele = [n[i]]
        elif n[i][3] == maxe:
            if n[i][3] != None and n[i][3] != []:
                maxele = maxele.append([n[i][3]])
    return maxele


# TO MAKE SURE THE PERSON HAS VOTED
("""def voted(id):
    ########################################################################
    l = []
    # READING ALL DATA TO A NESTED LIST
    # EXAMPLE :[['student0', '00', 'False'], ['student1', '11', 'False'],...]
    with open('studentdetails.csv', 'r') as fo:
        reader = csv.reader(fo)
        for i in reader:
            if (i != []):
                l.append(i)
        # MODIFYING THE NESTED LIST, AND CHANGING FALSE TO TRUE
        for j in l:
            if j[1] == id:
                if j[2] == True:
                    print("\n")
                    print("THE STUDENT HAS ALREADY VOTED")
                    mainmenu()

                else:
                    for k in l:
                        if k[2] == False:
                            print("\n")
                            print("THE NAME OF THE STUDENT IS : ", k[0])
                            votingsession()

    # WRITING THE MODIFIED LIST INTO THE FILE
    with open('studentdetails.csv', 'w') as fo:
        w = csv.writer(fo)
        w.writerows(l)
    ########################################################################""")


# FUNCTION TO GET THE RESULTS IN THE TABULAR FORM
def results():
    print("\n")
    pin = int(input("ENTER THE SECURITY PIN: "))
    if pin == 9003:
        v1 = maxvotes(presidents)
        v2 = maxvotes(vpresidents)
        v3 = maxvotes(artsclubsecs)
        v4 = maxvotes(vartsclubsecs)
        v5 = maxvotes(mgznedi)
        v6 = maxvotes(vmgznedi)
        v7 = maxvotes(sprtscap)
        v8 = maxvotes(vsprtscap)
        a1 = []
        a2 = []
        a3 = []
        a4 = []
        a5 = []
        a6 = []
        a7 = []
        a8 = []

        for i in range(5):
            if v1 != None and v1 != []:
                a1.append(v1[0][i])
            else:
                break

        for i in range(5):
            if v2 != None and v2 != []:
                a2.append(v2[0][i])
            else:
                break

        for i in range(5):
            if v3 != None and v3 != []:
                a3.append(v3[0][i])
            else:
                break
        for i in range(5):
            if v4 != None and v4 != []:
                a4.append(v4[0][i])
            else:
                break
        for i in range(5):
            if v5 != None and v5 != []:
                a5.append(v5[0][i])
            else:
                break
        for i in range(5):
            if v6 != None and v6 != []:
                a6.append(v6[0][i])
            else:
                break
        for i in range(5):
            if v7 != None and v7 != []:
                a7.append(v7[0][i])
            else:
                break
        for i in range(5):
            if v8 != None and v8 != []:
                a8.append(v8[0][i])
            else:
                break
        vote_list = open('votes.csv', 'a', newline='')
        p = csv.writer(vote_list)
        if [a1] != [] and [a1] != None:
            p.writerows([a1])
        vote_list = open('votes.csv', 'a', newline='')
        p = csv.writer(vote_list)
        if [a2] != [] and [a2] != None:
            p.writerows([a2])
        vote_list = open('votes.csv', 'a', newline='')
        p = csv.writer(vote_list)
        if [a3] != [] and [a3] != None:
            p.writerows([a3])
        vote_list = open('votes.csv', 'a', newline='')
        p = csv.writer(vote_list)
        if [a4] != [] and [a4] != None:
            p.writerows([a4])
        vote_list = open('votes.csv', 'a', newline='')
        p = csv.writer(vote_list)
        if [a5] != [] and [a5] != None:
            p.writerows([a5])
        vote_list = open('votes.csv', 'a', newline='')
        p = csv.writer(vote_list)
        if [a6] != [] and [a6] != None:
            p.writerows([a6])
        vote_list = open('votes.csv', 'a', newline='')
        p = csv.writer(vote_list)
        if [a7] != [] and [a7] != None:
            p.writerows([a7])
        vote_list = open('votes.csv', 'a', newline='')
        p = csv.writer(vote_list)
        if [a8] != [] and [a8] != None:
            p.writerows([a8])
        vote_list = open('votes.csv', 'a', newline='')
        p = csv.writer(vote_list)
        display('votes.csv')
    else:
        print(" WRONG PIN ENTERED ! ")
        print(" TRY AGAIN.................")
        pass


# FUNCTION TO ENTER CANDIDATE DETAILS
def encad():
    print("\n")
    pin = int(input("ENTER THE SECURITY PIN: "))
    if pin == 9003:
        while (True):
            print("\n")
            print("*" * 56)
            print("---------------------- DATA ENTRY ----------------------")
            print("*" * 56)
            print("""
        1.TO ENTER CANDIDATES DETAILS FOR POST PRESIDENT
        2.TO ENTER CANDIDATES DETAILS POST VICE PRESIDENT
        3.TO ENTER CANDIDATES DETAILS FOR POST ARTS CLUB SECRETARY 
        4.TO ENTER CANDIDATES DETAILS FOR POST VICE ARTS CLUB SECRETARY
        5.TO ENTER CANDIDATES DETAILS FOR POST MAGAZINE EDITOR
        6.TO ENTER CANDIDATES DETAILS FOR POST VICE MAGAZINE EDITOR
        7.TO ENTER CANDIDATES DETAILS FOR POST SPORTS CAPTAIN
        8.TO ENTER CANDIDATES DETAILS FOR POST VICE SPORTS CAPTAIN
        9.TO RETURN TO MAIN PROGRAM """)
            print("\n")
            c = int(input("ENTER YOUR CHOICE[1-9]: "))
            print("\n")
            if c == 1:
                n = int(input("ENTER THE NO.OF CANDIDATES FOR POST PRESIDENT: "))
                print("\n")
                for i in range(n):
                    a = input("ENTER THE CANDIDATE NAME: ")
                    b = int(input("ENTER THE CANDIDATE SCHOOL ID: "))
                    c = int(input("ENTER THE CANDIDATE CLASS: "))
                    print("\n")
                    l = [a, b, c, 0, 'PRESIDENT']
                    presidents.append(l)
            elif c == 2:
                n = int(input("ENTER THE NO.OF CANDIDATES FOR POST VICE PRESIDENT: "))
                print("\n")
                for i in range(n):
                    a = input("ENTER THE CANDIDATE NAME: ")
                    b = int(input("ENTER THE CANDIDATE SCHOOL ID: "))
                    c = int(input("ENTER THE CANDIDATE CLASS: "))
                    print("\n")
                    l = [a, b, c, 0, 'VICE PRESIDENT']
                    vpresidents.append(l)
            elif c == 3:
                n = int(input("ENTER THE NO.OF CANDIDATES FOR POST ARTS CLUB SECRETARY: "))
                print("\n")
                for i in range(n):
                    a = input("ENTER THE CANDIDATE NAME: ")
                    b = int(input("ENTER THE CANDIDATE SCHOOL ID: "))
                    c = int(input("ENTER THE CANDIDATE CLASS: "))
                    print("\n")
                    l = [a, b, c, 0, 'ARTS CLUB SECRETARY']
                    artsclubsecs.append(l)
            elif c == 4:
                n = int(input("ENTER THE NO.OF CANDIDATES FOR POST VICE ARTS CLUB SECRETARY: "))
                print("\n")
                for i in range(n):
                    a = input("ENTER THE CANDIDATE NAME: ")
                    b = int(input("ENTER THE CANDIDATE SCHOOL ID: "))
                    c = int(input("ENTER THE CANDIDATE CLASS: "))
                    print("\n")
                    l = [a, b, c, 0, 'VICE ARTS CLUB SECRETARY']
                    vartsclubsecs.append(l)
            elif c == 5:
                n = int(input("ENTER THE NO.OF CANDIDATES FOR POST MAGAZINE EDITOR: "))
                print("\n")
                for i in range(n):
                    a = input("ENTER THE CANDIDATE NAME: ")
                    b = int(input("ENTER THE CANDIDATE SCHOOL ID: "))
                    c = int(input("ENTER THE CANDIDATE CLASS: "))
                    print("\n")
                    l = [a, b, c, 0, 'MAGAZINE EDITOR']
                    mgznedi.append(l)
            elif c == 6:
                n = int(input("ENTER THE NO.OF CANDIDATES FOR VICE POST MAGAZINE EDITOR: "))
                print("\n")
                for i in range(n):
                    a = input("ENTER THE CANDIDATE NAME: ")
                    b = int(input("ENTER THE CANDIDATE SCHOOL ID: "))
                    c = int(input("ENTER THE CANDIDATE CLASS: "))
                    print("\n")
                    l = [a, b, c, 0, 'VICE MAGAZINE EDITOR']
                    vmgznedi.append(l)
            elif c == 7:
                n = int(input("ENTER THE NO.OF CANDIDATES FOR POST SPORTS CAPTAIN: "))
                print("\n")
                for i in range(n):
                    a = input("ENTER THE CANDIDATE NAME: ")
                    b = int(input("ENTER THE CANDIDATE SCHOOL ID: "))
                    c = int(input("ENTER THE CANDIDATE CLASS: "))
                    print("\n")
                    l = [a, b, c, 0, 'SPORTS CAPTAIN']
                    sprtscap.append(l)
            elif c == 8:
                n = int(input("ENTER THE NO.OF CANDIDATES FOR POST VICE SPORTS CAPTAIN: "))
                print("\n")
                for i in range(n):
                    a = input("ENTER THE CANDIDATE NAME: ")
                    b = int(input("ENTER THE CANDIDATE SCHOOL ID: "))
                    c = int(input("ENTER THE CANDIDATE CLASS: "))
                    print("\n")
                    l = [a, b, c, 0, 'VICE SPORTS CAPTAIN']
                    vsprtscap.append(l)
            elif c == 9:
                print("GOING BACK TO THE MAIN-MENU...........")
                break
    else:
        print(" WRONG PIN ENTERED ! ")
        print(" TRY AGAIN.................")
        pass


# FUNCTION TO START LOGIN
def login():
    print("\n")
    d = input("DO YOU WANT TO CONTINUE TO LOGIN SESSION ? [Y|N]: ")
    if d in "yY":
        while (True):
            print("\n")
            print("*" * 41)
            print("---------------- LOG IN -----------------")  # loggin in starts
            print("*" * 41)
            print("\n")
            # TO CHECK ID AND TO VERIFY IT IN CSV FILE
            id = input("ENTER YOUR'E SCHOOL ID:  ")
            with open('studentdetails.csv', 'r') as fi:
                r = csv.reader(fi)
                l = []
                for i in r:
                    if (i != []):
                        l.append(i)
                for lst in l:
                    if (lst[1] == id):
                        ex = True
                        break
                    else:
                        ex = False
                if (ex == True):
                    print("\n")
                    var = lst[0]
                    print(" CORRECT ID ENTERED ! ")
                    fou = 0
                else:
                    print("\n")
                    print("ID NOT FOUND /n TRY AGAIN")
                    fou = 1

            # RECHECKING THE IDs IF ENTERED WRONG VALUES IN THE FIRST ATTEMPT
            if fou == 1:
                id = input(" ENTER YOUR'E SCHOOL ID:  ")
                with open('studentdetails.csv', 'r') as fi:
                    r = csv.reader(fi)
                    l = []
                    for i in r:
                        if (i != []):
                            l.append(i)
                    for lst in l:
                        if (lst[1] == id):
                            ex = True
                            break
                        else:
                            ex = False
                    if (ex):
                        var = lst[0]
                        print("CORRECT ID ENTERED ! ")
                        fou = 0
                    else:
                        print(" WRONG INPUTS SURGE | KINDLY RESTART PROGRAM ")
                        login()
                        fou = 0

            with open('studentdetails.csv', 'r') as fo:
                c = csv.reader(fo)
                for i in c:
                    if (i != []):
                        if (i[1] == id):
                            if (i[2] == str(True)):
                                cf = True

                            else:
                                cf = False
                            break
                        else:
                            cf = True

            if (cf):
                print(" YOU ALREADY HAVE VOTED ! ")
                print("\n")
                login()
            else:
                print(' THE NAME OF THE VOTER IS:', var)
                details(id)
                votingsession()
    else:
        print("\n")
        mainmenu()


# BEGINNING OF VOTING SESSION
def votingsession():
    while (True):
        print("""
        1.TO VOTE FOR THE PRESIDENT
        2.TO VOTE FOR THE VICE PRESIDENT
        3.TO VOTE FOR THE ARTS CLUB SECRETARY
        4.TO VOTE FOR THE VICE ARTS CLUB SECRETARY
        5.TO VOTE FOR THE MAGAZINE EDITOR 
        6.TO VOTE FOR THE VICE MAGAZINE EDITOR
        7.TO VOTE FOR THE SPORTS CAPTAIN
        8.TO VOTE FOR THE VICE SPORTS CAPTAIN
        9.TO GO BACK TO LOGIN SESSION""")
        print("\n")
        ch = int(input(" ENTER YOUR CHOICE[1-9]: "))

        if ch == 1:
            votechoice(presidents)
        elif ch == 2:
            votechoice(vpresidents)
        elif ch == 3:
            votechoice(artsclubsecs)
        elif ch == 4:
            votechoice(vartsclubsecs)
        elif ch == 5:
            votechoice(mgznedi)
        elif ch == 6:
            votechoice(vmgznedi)
        elif ch == 7:
            votechoice(sprtscap)
        elif ch == 8:
            votechoice(vsprtscap)
        elif ch == 9:
            print(" RETURNING TO LOGIN SESSION........")
            login()
        else:
            print(" INVALID CHOICE - TRY AGAIN ")


def allvotes():
    p=9003
    while(True):
        print("\n")
        pin=int(input('ENTER THE SECURITY PIN: '))
        if pin==p:
            print("\n")
            print("-" * 54)
            print('| VOTE |', "|       NAME       |", '|         POST         |')
            print("-" * 54)
            for q in presidents:
                print(q[3]," "*10, q[0]," "*11,q[4])
            for w in vpresidents:
                print(w[3]," "*10, w[0]," "*11, w[4])
            for e in artsclubsecs:
                print(e[3]," "*10, e[0]," "*11, e[4])
            for r in vartsclubsecs:
                print(r[3]," "*10, r[0]," "*11, r[4])
            for t in mgznedi:
                print(t[3]," "*10, t[0]," "*11, t[4])
            for y in vmgznedi:
                print(y[3]," "*10, y[0]," "*11, y[4])
            for u in sprtscap:
                print(u[3]," "*10, u[0]," "*11, u[4])
            for i in vsprtscap:
                print(i[3]," "*10, i[0]," "*11, i[4])
            break
        else:
            print(" WRONG PIN ENTERED ")
            break


def mainmenu():
    while (True):
        print("\n")
        print("*" * 55)
        print("----------- SENATE ELECTION VOTING SYSTEM ® -----------")
        print("*" * 55)
        print("""
        1.TO ENTER CANDIDATE DETAILS
        2.TO START THE VOTING SESSION
        3.TO PRINT RESULT
        4.TO PRINT THE VOTES OF ALL CANDIDATES 
        5.TO RESET THE PROGRAM 
        6.TO EXIT """)
        print("\n")
        n = int(input("ENTER YOUR CHOICE[1-6]: "))
        if n == 1:
            encad()
        elif n == 2:
            login()
            votingsession()

        elif n == 3:
            results()
        elif n == 4:
            allvotes()
        elif n == 5:
            print("CHANGING THE VALUES......... ")
            print("\n")
            reset()
        elif n == 6:
            print("\n")
            print("_" * 85)

            print("--------------------- ꧁༒☬🆃🅷🅰🅽🅺🆂 🅵🅾🆁 🆄🆂🅸🅽🅶 🆂🅴🆅🆂☬༒꧂ -------------------")
            print("---------------------------THE PROGRMAM HAS BEEEN TERMINATED-------------------------")
            reset()
            print("-" * 85)
            exit()
        else:
            print("---- INVALID CHOICE ----")
            pass


mainmenu()

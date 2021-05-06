def register(offered,wishlist):
    """
    Given two lists offered and wishlist of students, return the list that stores registration process.
    The ordering is IMPORTANT
    offered: The list that stores offered courses, their total and current capacities.
    wishlist: The list that stores each student's register wishes.
    offered = [['Ceng111', 10, 9], ['Ceng140', 11, 9], ['Ceng232', 10, 3], ['Ceng443', 10, 1],['Ceng351', 11, 3], ['Ceng790', 10,8], ['Ceng334',2,1]]
    wishlist = [['Student0','Ceng111','Ceng140','Ceng232'], ['Student1','Ceng111','Ceng140','Ceng232'],['Student2','Ceng140','Ceng232'],['Student3','Ceng232','Ceng351','Ceng111','Ceng443','Ceng334','Ceng790']]
    """
    totalcap = []
    usedcap = []
    courses = []
    queue = []
    result = []
    for course in offered:
        totalcap.append(course[1])
        usedcap.append(course[2])
        courses.append(course[0])
    again = True
    while again:
        again = False
        for student in wishlist:
            if len(student) == 1:
                continue
            else:
                again = True
                wanted = student[1]
                if usedcap[courses.index(wanted)] < totalcap[courses.index(wanted)]:
                    result.append([student[0]]+[student.pop(1)])
                    usedcap[courses.index(wanted)] += 1
                else:
                    student.pop(1)
                queue.append(student)

    return result
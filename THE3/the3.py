def find_root(ls):
    if not ls:
        return
    children = []
    parents = []
    for i in ls:
        if type(i[1]) == float:
            children.append(i)
        else:
            for j in i[1:]:
                children.append(j[1])
    for i in ls:
        if i[0] not in children:
            parents.append(i)
    if parents == []:
        return children
    return parents # [['wheel', [1, 'rim'], [1, 'spoke'], [1, 'hub']], ['frame', [1, 'rearframe'], [1, 'frontframe']]]

def order(part_list,bos): # if a given part_list is not in the desired order, this function puts the list in a correct order
    if part_list == []:
        return bos
    else:
        parents = find_root(part_list)
        for i in parents:
            if i in part_list:
                part_list.remove(i)
                bos.append(i)
                order(part_list,bos)
    return bos

def antialiasing(lst):  # a personal implementation of the deepcopy function
    bos = []
    for i in lst:
        nec = []
        for j in i:
            if type(j) == float:
                nec.append(j)
            else:
                nec.append(j[:])
        bos.append(nec)
    return bos

def tuple_to_list(lst):  # nothing important, it just replaces tuples with lists in part_list for visualization
    for i in lst:
        for j in i:
            if type(j) == tuple:
                lst[lst.index(i)][i.index(j)] = list(j)
    return lst #  [['bike', [2, 'wheel'], [1, 'frame']], ['wheel', [1, 'rim'], [1, 'spoke'], [1, 'hub']], ['rim', 60.0], ['spoke', 120.0], ['hub', [2, 'gear'], [1, 'axle']], ['gear', 25.0], ['axle', [5, 'bolt'], [7, 'nut']], ['bolt', 0.1], ['nut', 0.15], ['frame', [1, 'rearframe'], [1, 'frontframe']], ['rearframe', 175.0], ['frontframe', [1, 'fork'], [2, 'handle']], ['fork', 22.5], ['handle', 10.0]]

def maketree(lst):  # this function creates the desired tree structure
    b = antialiasing(lst)
    a = order(b,[])
    for i in a:
        for j in i:
            if type(j) == str or type(j) == float:
                continue
            for x in a:
                if j[1] in x:
                    j+=x[1:]
                    break
    return [1]+a[0]   #  tree structure for reference: [1, 'bike', [2, 'wheel', [1, 'rim', 60.0], [1, 'spoke', 120.0], [1, 'hub', [2, 'gear', 25.0], [1, 'axle', [5, 'bolt', 0.1], [7, 'nut', 0.15]]]], [1, 'frame', [1, 'rearframe', 175.0], [1, 'frontframe', [1, 'fork', 22.5], [2, 'handle', 10.0]]]]

def calculate_price(part_list):
    tree = maketree(tuple_to_list(part_list))
    return calculate_price_helper(tree)

def calculate_price_helper(x):
    total = 0
    if len(x) == 3 and type(x[-1]) == float:
        return x[0]*x[-1]
    for chl in x[2:]:
        total += x[0] * calculate_price_helper(chl)
    return total

def required_parts(part_list):
    tree = maketree(tuple_to_list(part_list))
    resultant = []
    return required_parts_rec(1,tree,resultant)

def required_parts_rec(mul,x,temp):
    if len(x) == 3 and type(x[-1]) == float:
        temp.append((mul*x[0],x[1]))
    else:
        for chl in x[2:]:
            required_parts_rec(mul*x[0],chl,temp) # by only calling the function, we do not use the returned value which in turn prevents nestedness
    return temp

def stock_check(part_list,stock_list):
    tree = maketree(tuple_to_list(part_list))
    res = []
    requ = required_parts_rec(1,tree,res)
    return stock_check_helper(stock_list,requ)

def stock_check_helper(stock_list,req_parts):
    stck= stock_list[:] #  [(2, "rim"), (2, "spoke"), (4, "gear"), (8, "bolt"), (12, "nut"), (1, "rearframe"), (1, "fork"), (1, "handle")]
    req = req_parts  # [(2, "rim"), (2, "spoke"), (4, "gear"), (10, "bolt"), (14, "nut"), (1, "rearframe"), (1, "fork"), (2, "handle")]
    stock_name = []  #  ["rim","spoke","gear","bolt","nut","rearframe","fork","handle"]
    stock_count = [] #  [2,2,4,8,12,1,1,1]
    req_name = []    #  ["rim","spoke","gear","bolt","nut","rearframe","fork","handle"]
    req_count = []   #  [2,2,4,10,14,1,1,2]
    result = []
    for i in stck:
        stock_name.append(i[1])
        stock_count.append(i[0])
    for i in req:
        req_name.append(i[1])
        req_count.append(i[0])
    for elm in req_name:
        if elm in stock_name:
            if stock_count[stock_name.index(elm)] >= req_count[req_name.index(elm)]:
                continue
            else:
                result.append((elm,req_count[req_name.index(elm)]-stock_count[stock_name.index(elm)]))  # the amount which we are short on
        else:
            result.append((elm,req_count[req_name.index(elm)]))
    return result
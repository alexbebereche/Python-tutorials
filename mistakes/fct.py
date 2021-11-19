# def add_names(names, agg_list=[]): # mutable type is only initialized once
def add_names(names, agg_list=None):
    if isinstance(agg_list, type(None)):
        agg_list = []
    for name in names:
        agg_list.append(name)

    return agg_list

print(add_names(["a", 1, 3]))
print(add_names(["a", 1, 3]))

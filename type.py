def homogenous_list_hetrogenous_list(data):
    ret_list = []
    for val in data:
        if type(val) != str:
            ret_list.append(val)
    return ret_list

print(homogenous_list_hetrogenous_list(["hello",45.0,7,8,9,"appu","pothu","gubbi"]))
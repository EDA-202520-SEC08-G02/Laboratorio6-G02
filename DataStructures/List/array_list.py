def new_list():
    newlist = {
        'elements': [],
        'size': 0,
    }
    return newlist

def get_element(my_list, index):

    return my_list["elements"][index]



def is_present(my_list, element, cmp_function):

    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1

def add_first(my_list,element):
    my_list["elements"].insert(0,element)
    my_list["size"]+=1
    return my_list

def add_last(my_list,element):
    my_list["elements"].append(element)
    my_list["size"]+=1
    return my_list

def size(my_list):
    return my_list["size"]

def first_element(my_list):
    if my_list["size"]==0:
        raise IndexError("list index out of range")
    return my_list["elements"][0]


def is_empty(my_list):
    final = False
    if my_list["size"]==0:
        final = True
    return final

def last_element(my_list):
    if my_list["size"]==0:
        raise IndexError("list index out of range")
    resultado = my_list["elements"][-1]
    return resultado

def delete_element(my_list,pos):
    if 0 > pos or pos >= my_list["size"]:
        raise IndexError("list index out of range")
    my_list["elements"].pop(pos)
    my_list["size"]-=1
    return my_list

def remove_first(my_list):
    if my_list["size"]==0:
        raise IndexError("list index out of range")
    eliminado = my_list["elements"][0]
    my_list["elements"].pop(0)
    my_list["size"]-=1
    return eliminado

def remove_last(my_list):
    if my_list["size"]==0:
        raise IndexError("list index out of range")
    eliminado = my_list["elements"][-1]
    my_list["elements"].pop()
    my_list["size"]-=1
    return eliminado

def insert_element(my_list,element,pos):
    if 0 > pos or pos > my_list["size"]:
        raise IndexError("list index out of range")
    my_list["elements"].insert(pos,element)
    my_list["size"]+=1
    return my_list

def change_info(my_list,pos,new_info):
    if 0 > pos or pos >= my_list["size"]:
        raise IndexError("list index out of range")
    my_list["elements"][pos]= new_info
    return my_list

def exchange(my_list,pos_1,pos_2):
    if pos_1 < 0 or pos_1 >= my_list["size"] or pos_2 < 0 or pos_2 >= my_list["size"]:
        raise IndexError("list index out of range")
    primera_pos = my_list["elements"][pos_1]
    segunda_pos = my_list["elements"][pos_2]
    my_list["elements"][pos_1] = segunda_pos
    my_list["elements"][pos_2] = primera_pos
    return my_list

def sub_list(my_list,pos_i,num_elements):
    if 0 > pos_i or pos_i >= my_list["size"]:
        raise IndexError("list index out of range")
    final_sublista = pos_i + num_elements
    elementos_nuevos = my_list["elements"][pos_i:final_sublista]
    nueva_lista = {"elements":elementos_nuevos, "size":len(elementos_nuevos)}
    return nueva_lista

def default_sort_criteria(element_1, element_2):
    return element_1 < element_2

def selection_sort(lst, sort_criteria):

    l = size(lst)

    for i in range(l):

        curr_max = i

        for j in range(i+1, l):

            if not sort_criteria(get_element(lst, curr_max), get_element(lst,j)):

               curr_max = j

        exchange(lst, i, curr_max)
    return lst

def insertion_sort(my_list, sort_crit):
    l = size(my_list)
    for i in range(1, l):
        curr_element = get_element(my_list, i)
        swaping_cursor = i

        while swaping_cursor > 0 and sort_crit(curr_element, get_element(my_list, swaping_cursor - 1)):
            # intercambio
            exchange(my_list, swaping_cursor, swaping_cursor - 1)
            swaping_cursor -= 1

    return my_list

def shell_sort(lst, sort_criteria):
    l = size(lst)
    h = 1
    while h < (l//3): 
        h = 3*h + 1 
    while (h >= 1):
        for i in range (h, l): 
            j = i
            while (j>=h) and sort_criteria(get_element(lst, j), get_element(lst, j-h)):
                exchange (lst, j, j-h)
                j -= h
        h //= 3 
    return lst


def merge_sort(lst, sort_criteria):
    n = size(lst)
    aux_lst = new_list()
    for i in range(n):
        add_last(aux_lst, get_element(lst, i))
    merge_sort_recursive(lst, aux_lst, sort_criteria, 0, n-1)
    return lst

def merge_sort_recursive(lst, aux_lst, sort_criteria, lo, hi):
    if hi <= lo:
        return
    mid = lo + (hi - lo) // 2
    merge_sort_recursive(lst, aux_lst, sort_criteria, lo, mid)
    merge_sort_recursive(lst, aux_lst, sort_criteria, mid+1, hi)
    merge(lst, aux_lst, sort_criteria, lo, mid, hi)

def merge(lst, aux_lst, sort_criteria, lo, mid, hi):
    for k in range(lo, hi+1):
        change_info(aux_lst, k, get_element(lst, k))
    i = lo      
    j = mid + 1 
    for k in range(lo, hi+1):
        if i > mid:  
            change_info(lst, k, get_element(aux_lst, j))
            j += 1
        elif j > hi:  
            change_info(lst, k, get_element(aux_lst, i))
            i += 1
        elif sort_criteria(get_element(aux_lst, j), get_element(aux_lst, i)):
            change_info(lst, k, get_element(aux_lst, j))
            j += 1
        else:
            change_info(lst, k, get_element(aux_lst, i))
            i += 1


    
def quick_sort(lst, sort_criteria):
    quick_sort_recursive(lst, 0, size(lst)-1, sort_criteria)
    return lst
    
def quick_sort_recursive(lst, lo, hi, sort_criteria):
    if (lo >= hi ):
        return
    pivot =partition(lst, lo, hi, sort_criteria)
    quick_sort_recursive(lst, lo, pivot-1, sort_criteria)
    quick_sort_recursive(lst, pivot+1, hi, sort_criteria)

def partition(lst, lo, hi, sort_criteria):
    follower = lo 
    leader = lo 
    while leader < hi:
        if sort_criteria(get_element(lst, leader), get_element(lst, hi)):
            exchange(lst, follower, leader)
            follower += 1
        leader +=1
    exchange(lst, follower, hi) 
    return follower 
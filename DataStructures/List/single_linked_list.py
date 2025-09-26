from . import list_node as ln

def new_list():
    newlist = {
        'first': None,
        'last': None,
        'size':0,
    }
    return newlist



def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"]



def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else: 
            temp = temp["next"]
            count += 1

    if not is_in_array:
        count = -1
    return count

def add_first(my_list, element):
    
    node = ln.new_single_node(element=element)
    
    
    node["next"] = my_list["first"]
    my_list["first"] = node
    
    if is_empty(my_list):
        my_list["last"] = node
    
    my_list["size"] += 1
    return my_list

def add_last(my_list, element):
    
    node = ln.new_single_node(element=element)
    
    if is_empty(my_list):
        
        my_list["first"] = node
        my_list["last"] = node
        
    else:
        
        my_list["last"]["next"] = node
        my_list["last"] = node
        
    my_list["size"] += 1
    return my_list

def size(my_list):
    
    return my_list["size"]

def first_element(my_list):
    
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    
    return ln.get_element(my_list["first"])

def is_empty(my_list):
    
    return size(my_list) == 0

def last_element(my_list):
    
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    
    return my_list["last"]["info"]

def delete_element(my_list, pos):
    
    if pos < 0 or pos >= size(my_list) or type(pos) != int:
        raise Exception('IndexError: list index out of range')
    
    if pos == 0:
        remove_first(my_list)
        return my_list
    
    if pos == size(my_list)-1:
        remove_last(my_list)
        return my_list
    
    # In case is any random position
    
    prev = None
    curr = my_list["first"]
    
    # Traverse to pos
    i = 0
    while i<pos:
        prev = curr
        curr = curr["next"]
        i += 1
     
        
    prev["next"] = curr["next"]    
    
    my_list["size"] -= 1
    return my_list

def remove_first(my_list):
    
    if my_list["first"] == None:
        next_n = None
    else:
        next_n = my_list["first"]["next"]
    
    info = ln.get_element(my_list["first"])
    
    my_list["first"] = next_n
    
    my_list["size"] -= 1
    
    if is_empty(my_list):
        my_list["last"] = None
    
    return info

def remove_last(my_list):
    
    pos = size(my_list)-1 -1
    
    curr = my_list["first"]
    
    i = 0
    while i<pos:
        curr = curr["next"]
        i += 1
        
    curr["next"] = None
    
    info = my_list["last"]["info"]
    
    my_list["last"] = curr
    
    my_list["size"] -= 1
    return info
        
def insert_element(my_list, element, pos):
    
    prev = None
    curr = my_list["first"]
    
    # Traverse to pos
    i = 0
    while i<pos:
        prev = curr
        curr = curr["next"]
        i += 1
        
    n_node = ln.new_single_node(element)
    
    n_node = curr
    
    if prev == None:
        
        my_list["first"]
        
    else: 
        
        prev["next"] = n_node
    
    my_list["size"] += 1
    return my_list

def change_info(my_list, pos, new_info):
     
    curr = my_list["first"]
    
    # Traverse to pos
    i = 0
    while i<pos:
        curr = curr["next"]
        i += 1
        
    curr["info"] = new_info
    
    return my_list

def exchange(my_list, pos_1, pos_2):
    
    l = size(my_list)
    
    if pos_1 < 0 or pos_1 >= l or type(pos_1) != int or \
        pos_2 < 0 or pos_2 >= l or type(pos_2) != int:
    
        raise Exception('IndexError: list index out of range') 
    
    i=0
    
    prev_1 = None
    slct_1 = my_list["first"]
    
    prev_2 = None
    slct_2 = my_list["first"]
    
    while i<pos_1 or i<pos_2:
        
        if i < pos_1:
            prev_1 = slct_1
            slct_1 = slct_1["next"]
            
        if i < pos_2:
            prev_2 = slct_2
            slct_2 = slct_2["next"]
        
        i += 1
        
    if prev_1  == None:
        my_list["first"] = slct_2
    else:    
        prev_1["next"] = slct_2
        
    if prev_2  == None:
        my_list["first"] = slct_1
    else:    
        prev_2["next"] = slct_1
        
    slct_1_next = slct_1["next"]    
    slct_1["next"] = slct_2["next"]
    slct_2["next"] = slct_1_next
    
    if slct_1["next"] == None:
        my_list["last"] = slct_1
        
    if slct_2["next"] == None:
        my_list["last"] = slct_2
        
    return my_list

def sub_list(my_list, pos, num_elements):
    
    n_list = new_list()
    
    curr = my_list["first"]
    
    # Traverse to pos
    i = 0
    while i<pos:
        curr = curr["next"]
        i += 1
        
    n_list["first"] = curr
    
    i = 1
    while i<num_elements:
        curr = curr["next"]
        i += 1
        
    curr["next"] = None    
    n_list["last"] = curr
    
    n_list["size"] = num_elements
    
    return n_list

def default_sort_criteria(element_1, element_2):
    return element_1 < element_2  


def selection_sort(lst, sort_criteria):
    if size(lst) <= 1:
        return lst
    current = lst["first"]
    while current is not None:
        max_node = current
        search_node = current["next"]
        while search_node is not None:
            if sort_criteria(search_node["info"], max_node["info"]):
                max_node = search_node
            search_node = search_node["next"]
        if max_node != current:
            temp_info = current["info"]
            current["info"] = max_node["info"]
            max_node["info"] = temp_info
        current = current["next"]
    
    return lst

def insertion_sort(my_list, sort_crit):
    if size(my_list) <= 1:
        return my_list
    current = my_list["first"]["next"]
    
    while current is not None:
        next_node = current["next"]  
        current_value = current["info"]
        prev = None
        sorted_current = my_list["first"]
        while sorted_current != current and sort_crit(sorted_current["info"], current_value):
            prev = sorted_current
            sorted_current = sorted_current["next"]
        if sorted_current != current:
            if prev is None:
                prev_node = my_list["first"]
                while prev_node["next"] != current:
                    prev_node = prev_node["next"]
                prev_node["next"] = current["next"]
                current["next"] = my_list["first"]
                my_list["first"] = current
            else:
                prev_node = my_list["first"]
                while prev_node["next"] != current:
                    prev_node = prev_node["next"]
                prev_node["next"] = current["next"]
                current["next"] = prev["next"]
                prev["next"] = current
        
        current = next_node
    
    return my_list

def shell_sort(lst, sort_criteria):
    n = size(lst)
    if n <= 1:
        return lst
    gap = 1
    while gap < n // 3:
        gap = 3 * gap + 1
    while gap >= 1:
        for start in range(gap):
            i = start + gap
            while i < n:
                current_info = get_element(lst, i)
                j = i
                while j >= gap:
                    prev_info = get_element(lst, j - gap)
                    if sort_criteria(current_info, prev_info):
                        current_node_info = get_element(lst, j)
                        change_info(lst, j, prev_info)  
                        change_info(lst, j - gap, current_node_info)  
                        j -= gap
                    else:
                        break     
                i += gap
        gap //= 3
    return lst



def merge_sort(lst, sort_criteria):
    if size(lst) <= 1:
        return lst
    mid = size(lst) // 2
    left = new_list()
    right = new_list()
    
    curr = lst["first"]
    for i in range(mid):
        add_last(left, curr["info"])
        curr = curr["next"]
    for i in range(mid, size(lst)):
        add_last(right, curr["info"])
        curr = curr["next"]
    merge_sort(left, sort_criteria)
    merge_sort(right, sort_criteria)
    return merge_lists(lst, left, right, sort_criteria)

def merge_lists(lst, left, right, sort_criteria):
    lst["first"] = None
    lst["last"] = None
    lst["size"] = 0
    
    left_curr = left["first"]
    right_curr = right["first"]

    while left_curr is not None and right_curr is not None:
        if sort_criteria(left_curr["info"], right_curr["info"]):
            add_last(lst, left_curr["info"])
            left_curr = left_curr["next"]
        else:
            add_last(lst, right_curr["info"])
            right_curr = right_curr["next"]
    while left_curr is not None:
        add_last(lst, left_curr["info"])
        left_curr = left_curr["next"]
    while right_curr is not None:
        add_last(lst, right_curr["info"])
        right_curr = right_curr["next"]
    return lst


def quick_sort(lst, sort_criteria):
    if size(lst) <= 1:
        return lst
    pivot = first_element(lst)
    less = new_list()
    equal = new_list()
    greater = new_list()
    curr = lst["first"]
    while curr is not None:
        if sort_criteria(curr["info"], pivot):
            add_last(less, curr["info"])
        elif sort_criteria(pivot, curr["info"]):
            add_last(greater, curr["info"])
        else:
            add_last(equal, curr["info"])
        curr = curr["next"]
        
    quick_sort(less, sort_criteria)
    quick_sort(greater, sort_criteria)
    lst["first"] = None
    lst["last"] = None
    lst["size"] = 0

    if not is_empty(less):
        curr = less["first"]
        while curr is not None:
            add_last(lst, curr["info"])
            curr = curr["next"]
    if not is_empty(equal):
        curr = equal["first"]
        while curr is not None:
            add_last(lst, curr["info"])
            curr = curr["next"]
    if not is_empty(greater):
        curr = greater["first"]
        while curr is not None:
            add_last(lst, curr["info"])
            curr = curr["next"]
    return lst


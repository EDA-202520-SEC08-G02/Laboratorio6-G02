import random

from DataStructures.List import array_list as lt
from . import map_entry as mpe
from . import map_functions as mpf

def new_map(num_elements,load_factor,prime=109345121):
    new_hashmap = {}
    new_hashmap['prime'] = prime
    new_hashmap['capacity'] = mpf.next_prime(int(num_elements/load_factor))
    new_hashmap['scale'] = random.randint(1,prime-1)
    new_hashmap['shift'] = random.randint(0,prime-1)
    new_hashmap['table'] = lt.new_list()
    for _ in range(new_hashmap['capacity']):
        lt.add_last(new_hashmap['table'], mpe.new_map_entry(None,None))
    new_hashmap['current_factor'] = 0
    new_hashmap['limit_factor'] = load_factor
    new_hashmap['size'] = 0
    return new_hashmap

def default_compare(key, entry):
    entry_key = mpe.get_key(entry)
    if key is None and entry_key is None:
        return 0
    elif key is None:
        return -1
    elif entry is None:
        return 1
    if key == entry_key:
        return 0
    if key > entry_key:
        return 1
    else:
        return -1

def is_available(table, pos):
    
    entry = lt.get_element(table, pos)
    entry_key = mpe.get_key(entry)
    return entry_key is None or entry_key == "__EMPTY__"



def find_slot(my_map, key, hash_value):
    capacity = my_map["capacity"]
    i = hash_value
    first_available = -1
    done = 0
    
    while done < capacity:
        if i >= capacity:
            i = i % capacity
        elem = lt.get_element(my_map["table"], i)
        elem_key = mpe.get_key(elem)
        if elem_key == key:
            return (True, i)
        if is_available(my_map["table"], i):
            if first_available == -1:
                first_available = i 
            if elem_key is None:
                return (False, first_available)
        i = (i + 1) % capacity
        done += 1
    if first_available != -1:
        return (False, first_available)
    raise Exception("pues esta llena")
    
    
"""def find_slot(my_map, key, hash_value):
"
    capacity = my_map["capacity"]
    i = hash_value % capacity  # Asegurar que empiece en rango
    first_available = -1

    #Buscar de manera más eficiente
    for attempt in range(capacity):
        elem = lt.get_element(my_map["table"], i)
        elem_key = mpe.get_key(elem)

    # 1: Encontramos la key
        if elem_key == key:
            return (True, i)

    #Caso 2: Espacio disponible
        if elem_key is None or elem_key == "EMPTY":
            if first_available == -1:
                first_available = i
            # Si es None (nunca usado), podemos terminar la búsqueda
            if elem_key is None:
                return (False, first_available)

        i = (i + 1) % capacity

    return (False, first_available)"""
    
def rehash(my_map):
    prime = my_map['prime']
    load_factor = my_map['limit_factor']
    new_num_elements = 2*my_map['capacity']*load_factor # Doesn't calculate next prime since since new_map already does

    new_hashmap = new_map(new_num_elements,load_factor,prime)

    for i in range(lt.size(my_map["table"])):
        elem = lt.get_element(my_map["table"], i)
        key = mpe.get_key(elem)
        val = mpe.get_value(elem)
        if key is not None and key != "__EMPTY__":
            put(new_hashmap, key, val)

    my_map["table"] = new_hashmap["table"]
    my_map["capacity"] = new_hashmap["capacity"]

    my_map["scale"] = new_hashmap["scale"]
    my_map["shift"] = new_hashmap["shift"]
    my_map["size"] = new_hashmap["size"]

    return my_map



def place(my_map,key,val):
    if (my_map["size"]+1)/my_map["capacity"] >= my_map["limit_factor"]:
        my_map = rehash(my_map)

    key_hash = mpf.hash_value(my_map,key)
    found,indice = find_slot(my_map,key,key_hash)
    
    if not found:
        my_map['size'] += 1
        my_map['current_factor'] = my_map['size'] / my_map['capacity']
    lt.change_info(my_map["table"], indice, val)

    return my_map

def put(my_map,key,value):
    entry = mpe.new_map_entry(key, value)
    my_map = place(my_map, key, entry)
    return my_map

def contains(my_map, key):

    hash_value = mpf.hash_value(my_map, key)
    found,_ = find_slot(my_map, key, hash_value)
    return found

def remove(my_map, key):
    hash_value = mpf.hash_value(my_map, key)
    found, i = find_slot(my_map, key, hash_value)
    if found:
        empty_entry = mpe.new_map_entry("__EMPTY__", None)
        lt.change_info(my_map["table"], i, empty_entry)
        my_map["size"] -= 1
    
    return my_map 

def get(my_map, key):
    hash_value = mpf.hash_value(my_map, key)
    found, i = find_slot(my_map, key, hash_value)
    if found:
        entry = lt.get_element(my_map["table"], i)
        return mpe.get_value(entry)
    else:
        return None


def size(my_map):
    return my_map["size"]

def is_empty(mY_map):
    if mY_map['size'] == 0:
        return True
    else:
        return False

def key_set(my_map):
    keys = lt.new_list()
    table = my_map['table']
    for i in range(0,lt.size(table)):
        entry = lt.get_element(table,i)
        key = mpe.get_key(entry)
        if key != None and key != "__EMPTY__":
            lt.add_last(keys,key)
    return keys

def value_set(my_map):
    values = lt.new_list()
    table = my_map['table']
    for i in range(0,lt.size(table)):
        entry = lt.get_element(table,i)
        key = mpe.get_key(entry)
        value = get(my_map,key)
        if value != None and value != "__EMPTY__":
            lt.add_last(values,value)
    return values
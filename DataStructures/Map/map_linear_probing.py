import random

from List import array_list as lt
from . import map_entry as mpe
from . import map_functions as mpf

def new_map(num_elements,load_factor,prime=109345121):
    new_hashmap = {}
    new_hashmap['prime'] = prime
    new_hashmap['capacity'] = mpf.next_prime(num_elements/load_factor)
    new_hashmap['scale'] = random.randint(1,prime-1)
    new_hashmap['shift'] = random.randint(0,prime-1)
    new_hashmap['table'] = lt.new_list()
    for _ in range(num_elements):
        lt.add_last(new_hashmap['table'], mpe.new_map_entry(None,None))
    new_hashmap['current_factor'] = 0
    new_hashmap['limit_factor'] = load_factor
    new_hashmap['size'] = 0
    return new_hashmap

def default_compare(key, entry):

    if key == mpe.get_key(entry):
        return 0
    if key > mpe.get_key(entry):
        return 1
    return -1

def is_available(table, pos):
    
    entry = lt.get_element(table, pos)
    return mpe.get_key(entry) is None or mpe.get_key(entry) == "__EMPTY__"

def find_slot(my_map,key,hash_value):
    i = hash_value

    elem = lt.get_element(my_map["table"], i)
    while default_compare(key, elem) == 0 and default_compare(None, elem) and i != hash_value-1:
        i = (i+1) % my_map["capacity"]
        elem = lt.get_element(my_map["table"], i)
        i_key = mpe.get_key(elem)
    
    if i_key == key:
        return (True, i)
    elif i_key == None:
        return (False, i)
    else:
        raise Exception("pues esta llena")
    
def rehash(my_map):
    prime = my_map['prime']
    load_factor = my_map['load_factor']
    new_num_elements = 2*my_map['capacity']*load_factor # Doesn't calculate next prime since since new_map already does

    new_hashmap = new_map(new_num_elements,load_factor,prime)

    for i in range(lt.size(my_map["table"])):
        elem = lt.get_element(my_map["table"], i)
        key = mpe.get_key(elem)
        val = mpe.get_value(elem)
        put(new_hashmap, key, val)

    my_map["table"] = new_hashmap["table"]
    my_map["capacity"] = new_hashmap["capacity"]

    return my_map

def place(my_map,key,val):
    if my_map["size"]/my_map["capacity"] >= my_map["limit_factor"]:
        rehash(my_map)

    key_hash = mpf.hash_value(my_map,key)
    _,indice = find_slot(my_map,key,key_hash)
    lt.change_info(my_map["table"], indice, val)

    my_map["size"] += 1

def put(my_map,key,value):
    place(my_map, key, mpe.new_map_entry(key, value))

    return my_map

def contains(my_map, key):

    hash_value = mpf.hash_value(my_map, key)

    return find_slot(my_map, key, hash_value)[0]

def remove(my_map, key):

    place(my_map, key, "__EMPTY__")

    return  my_map

def get(my_map, key):
    hash_value = mpf.hash_value(my_map, key)
    found, i = find_slot(my_map, key, hash_value)

    return lt.get_element(my_map["table"], i)


def size(my_map):
    return my_map["size"]


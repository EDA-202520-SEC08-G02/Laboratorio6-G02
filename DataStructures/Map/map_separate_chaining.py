#llenar esto

import random

from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sl

from . import map_entry as mpe
from . import map_functions as mpf

def new_map(num_elements,load_factor,prime=109345121):
    new_hashmap = {}
    new_hashmap['prime'] = prime
    new_hashmap['capacity'] = mpf.next_prime(int(num_elements/load_factor))
    new_hashmap['scale'] = random.randint(1,prime-1)
    new_hashmap['shift'] = random.randint(0,prime-1)
    new_hashmap['table'] = al.new_list()
    for _ in range(new_hashmap['capacity']):
        al.add_last(new_hashmap['table'], sl.new_list())
    new_hashmap['current_factor'] = 0
    new_hashmap['limit_factor'] = load_factor
    new_hashmap['size'] = 0
    return new_hashmap

def default_compare(key, entry):
    if key == mpe.get_key(entry):
        return 0
    else:
        return -1
 
def rehash(my_map):
    prime = my_map['prime']
    load_factor = my_map['limit_factor']
    new_num_elements = 2*my_map['capacity']*load_factor # Doesn't calculate next prime since since new_map already does

    new_hashmap = new_map(new_num_elements,load_factor,prime)

    for i in range(al.size(my_map["table"])):
        bucket = al.get_element(my_map["table"], i)
        if not sl.is_empty(bucket):
            current = bucket['first']
            while current is not None:
                key = mpe.get_key(current['info'])
                val = mpe.get_value(current['info'])
                if key is not None and key != "__EMPTY__":
                    put(new_hashmap, key, val)
                current = current['next']

    my_map["table"] = new_hashmap["table"]
    my_map["capacity"] = new_hashmap["capacity"]

    my_map["scale"] = new_hashmap["scale"]
    my_map["shift"] = new_hashmap["shift"]
    my_map["size"] = new_hashmap["size"]

    return my_map

def place(my_map,key,value):
    key_hash = mpf.hash_value(my_map,key)
    bucket_index = key_hash % my_map["capacity"]
    bucket = al.get_element(my_map["table"], bucket_index)
    entry = mpe.new_map_entry(key, value)
    current = bucket['first']
    position = 0
    key_exists = False
    
    while current is not None and key_exists is False:
        if default_compare(key, current['info']) == 0:
            sl.change_info(bucket, position, entry)
            key_exists = True
        else:
            current = current['next']
            position += 1
    
    if key_exists is False:
        sl.add_last(bucket, entry)
        my_map["size"] += 1
        my_map["current_factor"] = my_map["size"] / my_map["capacity"]
        if my_map["current_factor"] > my_map["limit_factor"]:
            my_map = rehash(my_map)
    
    return my_map

def put(my_map,key,value):
    my_map = place(my_map, key, value)
    return my_map

def contains(my_map, key):
    hash_value = mpf.hash_value(my_map, key)
    bucket_index = hash_value % my_map["capacity"]
    bucket = al.get_element(my_map["table"], bucket_index)
    if sl.is_empty(bucket):
        return False
    current = bucket['first']
    while current is not None:
        if default_compare(key, current['info']) == 0:
            return True
        current = current['next']
    return False

def remove(my_map, key):
    hash_value = mpf.hash_value(my_map, key)
    bucket_index = hash_value % my_map["capacity"]
    bucket = al.get_element(my_map["table"], bucket_index)
    current = bucket['first']
    i = 0
    found = False
    if sl.is_empty(bucket):
        return my_map
    while current is not None and found is False:
        if default_compare(key, current['info']) == 0:
            found = True
        else:
            current = current['next']
            i += 1
    if found:
        empty_entry = mpe.new_map_entry("__EMPTY__", None)
        sl.change_info(bucket, i, empty_entry)
        my_map["size"] -= 1
        my_map["current_factor"] = my_map["size"] / my_map["capacity"]

    return my_map

def get(my_map, key):
    hash_value = mpf.hash_value(my_map, key)
    bucket_index = hash_value % my_map["capacity"]
    bucket = al.get_element(my_map["table"], bucket_index)
    current = bucket['first']
    found = False
    if sl.is_empty(bucket): 
        return None
    while current is not None and found is False:
        if default_compare(key, current['info']) == 0:
            found = True
            return mpe.get_value(current['info'])
        current = current['next']
    return None


def size(my_map):
    return my_map["size"]

def is_empty(my_map):
    if my_map['size'] == 0:
        return True
    else:
        return False

def key_set(my_map):
    keys = al.new_list()
    table = my_map['table']
    for i in range(0,al.size(table)):
        bucket = al.get_element(table,i)
        if not sl.is_empty(bucket):
            current = bucket['first']
            while current is not None:
                key = mpe.get_key(current['info'])
                if key != None and key != "__EMPTY__":
                    al.add_last(keys,key)
                current = current['next']
    return keys

def value_set(my_map):
    values = al.new_list()
    table = my_map['table']
    for i in range(0,al.size(table)):
        bucket = al.get_element(table,i)
        if not sl.is_empty(bucket):
            current = bucket['first']
            while current is not None:
                value = mpe.get_value(current['info'])
                if value != None and value != "__EMPTY__":
                    al.add_last(values,value)
                current = current['next']
    return values
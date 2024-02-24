def is_type(obj: object):
    try:
        type(obj)
        return True
    except Exception:
        return False

def is_set(obj: object):
    try:
        set(obj)
        return True
    except Exception:
        return False

def is_tuple(obj: object):
    try:
        tuple(obj)
        return True
    except Exception:
        return False

def is_list(obj: object):
    try:
        list(obj)
        return True
    except Exception:
        return False

def is_dict(obj: object):
    try:
        dict(obj)
        return True
    except Exception:
        return False

def is_bool(obj: object):
    try:
        bool(obj)
        return True
    except Exception:
        return False

def is_str(obj: object):
    try:
        str(obj)
        return True
    except Exception:
        return False

def is_int(obj: object):
    try:
        int(obj)
        return True
    except Exception:
        return False

def is_float(obj: object):
    try:
        float(obj)
        return True
    except Exception:
        return False
    
def get_true_type(type_: type, obj: object):
    if type_ == int and is_int(obj=obj):
        return int
    elif type_ == float and is_float(obj=obj):
        return float
    elif type_ == dict and is_dict(obj=obj):
        return dict
    elif type_ == list and is_list(obj=obj):
        return list
    elif type_ == set and is_set(obj=obj):
        return set
    elif type_ == tuple and is_tuple(obj=obj):
        return tuple
    elif type_ == bool and is_bool(obj=obj):
        return bool
    elif type_ == str and is_str(obj=obj):
        return str
    
    return None
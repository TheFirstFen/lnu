import requests

URL = 'http://localhost:3000/kvs'

def get(key):
    r = requests.get(f'{URL}/{key}')
    if r.status_code == 200:
        return r.text, True
    else:
        return None, False

def put(key, val):
    r = requests.put(f'{URL}/{key}', data=val)
    return r.status_code == 201

def delete(key):
    r = requests.delete(f'{URL}/{key}')
    return r.status_code == 200




# Set key "first" to "initial"
assert put('first', 'initial'), 'put first failed'

# Check that it is set
assert get('first') == ('initial', True), 'get first failed'

# Setting a few more keys
assert put('second', 'another'), 'put second failed'
assert put('third', 'more'), 'put third failed'
assert put('fourth', 'done'), 'put fourth failed'

# Trying to get a bad key
assert get('fifth') == (None, False), 'get fifth should fail'

# Deleting a key
assert delete('third'), 'delete failed'

# Trying to get deleted key
assert get('third') == (None, False), 'get third should fail'


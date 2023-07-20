import hashlib

def generateHash(input_string):
    hash_object = hashlib.sha256()
    hash_object.update(input_string.encode('utf-8'))
    hash_value = hash_object.hexdigest()
    return hash_value


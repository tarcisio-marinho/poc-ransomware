
import decrypt
import pickle
import os

def main(path):

    path_n_keys = pickle.load(open('teste/keys.key', 'r')) 
    for found_file, key in path_n_keys:
        
        with open(found_file, 'rb') as f:
            file_content = f.read()
        
        decrypted = decrypt.decrypt(file_content, key)

        new_file_name = found_file.replace('.GNNCRY', '')
        with open(new_file_name, 'wb') as f:
            f.write(decrypted)

        os.remove(found_file)

if __name__ == "__main__":
    main('teste/')
    
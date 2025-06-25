import os
import shutil

def verify_directory_path(directory):
    # returns true if the directory exists, false otherwise
    return os.path.exists(directory)

def list_directory_files(directory):
    # returns a list of all the files in a directory
    return os.listdir(directory)

def found_file_at_path(path_to_file):
    # returns true is the path_to_file is an existing file.
    return os.path.isfile(path_to_file)

def found_dir_at_path(path_to_directory):
    # returns true if the path leads to an existing directory
    return os.path.isdir(path_to_directory)

def create_new_directory(path_ending_with_name):
    # creates a new directory, using a path and ending with the /directory_name
    return os.mkdir(path_ending_with_name)

def copy_file(old, new):
    return shutil.copy(old, new)

def delete_directory(path):
    return shutil.rmtree(path)


def file_or_directory(path):
    files = list_directory_files(path)
    for file in files:
        full_path = os.path.join(path, file)
        if found_file_at_path(full_path) == True:
            print(f"{file} is a 'file' type")
        if found_dir_at_path(full_path) == True:
            print(f"{file} is a 'directory' type")

def copy_files_recursively(source, dest):
    files = list_directory_files(source)
    for file in files:
        source_path = os.path.join(source, file)
        destination_path = os.path.join(dest, file)
        
        if found_file_at_path(source_path) == True:
            print(f"{file} is a 'file' type")
            os.makedirs(os.path.dirname(destination_path), exist_ok=True)
            copy_file(source_path, destination_path)

        elif found_dir_at_path(source_path):
            if not verify_directory_path(destination_path):
                create_new_directory(destination_path)
            copy_files_recursively(source_path, destination_path)



def main():
    
    # file directory locations.
    root_dir = "/home/joshburne/workspace/boot.dev/static_site_generator"
    src_dir = f"{root_dir}/src"
    public_dir = f"{root_dir}/public"
    static_dir = f"{root_dir}/static"
    
    # test directories while writing the code
    test_destination_dir = f"{root_dir}/test_desitnation_dir"
    source_dir = f"{root_dir}/sourcedir"

    if verify_directory_path(public_dir):
        delete_directory(public_dir)
    else:
        create_new_directory(public_dir)
    copy_files_recursively(static_dir, public_dir)
    



 
main()


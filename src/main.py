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

def create_new_directory(path_ending_with_name):
    # creates a new directory, using a path and ending with the /directory_name
    return os.mkdir(path_ending_with_name)

def copy_file(old, new):
    return shutil.copy(old, new)

def delete_directory(path):
    return shutil.rmtree(path)



def main():
    # file directory locations.
    root_dir = "/home/joshburne/workspace/boot.dev/static_site_generator"
    src_dir = f"{root_dir}/src"
    public_dir = f"{root_dir}/public"
    static_dir = f"{root_dir}/static"
    test_dir = f"{root_dir}/testdir"
    source_dir = f"{root_dir}/sourcedir"

    create_new_directory(source_dir)

    delete_directory(test_dir)

    





main()


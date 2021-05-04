import os, shutil, sys

def extract_files_from_dir(root_dir, sub_dirs):
    for sub_dir in sub_dirs:
        sub_dir_path = root_dir + sub_dir.path
        move_to_root_folder(root_dir, sub_dir_path)

# Move all files from subdirectories to root directories
def move_to_root_folder(root_path, curr_path):
    # print("Path: ", curr_path)
    try:
        if not os.path.isdir(curr_path): #dir not exists!
            return 
        for filename in os.listdir(curr_path):
            if os.path.isfile(os.path.join(curr_path, filename)):
                shutil.move(os.path.join(curr_path, filename), os.path.join(root_path, filename))
            elif os.path.isdir(os.path.join(curr_path, filename)):
                move_to_root_folder(root_path, os.path.join(curr_path, filename))
            else:
                sys.exit("Should never reach here!")
        
    except (FileExistsError, FileNotFoundError, OSError):
        print("\n>>> Error - File/Dir not exits!")

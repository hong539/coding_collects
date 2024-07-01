import os
import glob

def main():
    current_dir = os.getcwd()
    print(current_dir)
    # glob.glob('**/*.py', recursive=True)
    # glob.glob('**/*add.py', recursive=True)

    find_dic = {
                "add.py":"",
                "print_list04.py":"",
                "str_to_dic01.py":"",
                "ci_example01.py":"",
                "list01.py":"",
            }

    path_list = []

    for key in find_dic:
        # print(key)
        pattern = "**/" + key    
        result = glob.glob(pathname=pattern, recursive=True)
        print(result)
        path_list.append(result)
        # print(type(result))
        # path_list = glob.glob(f"**/{key}.py", recursive=True)
        # path_list.append(result)

    print(path_list)    

if __name__ == "__main__":
    main()
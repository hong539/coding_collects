import os
import shutil
import glob

def create_dict_from_env_variable():
    # Get the environment variable TARGET's value
    target = os.getenv('TARGET')
    
    # If TARGET does not exist, return an empty dictionary
    if target is None:
        return {}
    
    # Split the TARGET value by "\n" and convert to a list
    target_list = target.split('\n')
    
    # Create a dictionary with list values as keys and default value as ""
    result_dict = {key: "" for key in target_list}
    
    return result_dict

def move_jar_files(target_dict, search_path, destination_path="/tmp"):
    # Ensure the destination directory exists
    os.makedirs(destination_path, exist_ok=True)
    
    for key in target_dict:
        # Search for files matching "key.jar" in the specified search path
        search_pattern = os.path.join(search_path, f"{key}.jar")
        jar_files = glob.glob(search_pattern)
        
        # Move each found jar file to the destination path
        for jar_file in jar_files:
            shutil.move(jar_file, destination_path)
            print(f"Moved {jar_file} to {destination_path}")

if __name__ == "__main__":
    # Create the dictionary from the TARGET environment variable
    target_dict = create_dict_from_env_variable()
    
    # Specify the directory where to search for .jar files
    search_directory = "/path/to/search/directory"
    
    # Move the .jar files based on the dictionary keys
    move_jar_files(target_dict, search_directory)
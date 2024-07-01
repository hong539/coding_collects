import os
import shutil
import glob
import json

def create_dict_from_env_variable():
    # Get the environment variable TARGET's value
    target = os.getenv('TARGET')
    
    # If TARGET does not exist, return an empty dictionary
    if target is None:
        return {}
    
    # Split the TARGET value by "\n" and convert to a list
    target_list = target.split('\n')
    
    # Create a dictionary with list values as keys and default value as ""
    # tips: https://www.geeksforgeeks.org/python-dictionary-comprehension/
    result_dict = {key: "" for key in target_list}
    
    return result_dict

def move_jar_files(target_dict, search_path, destination_path="/tmp"):
    # Ensure the destination directory exists
    os.makedirs(destination_path, exist_ok=True)
        
    for key in target_dict:
        # Search for files matching "key.jar" in the specified search path
        # search_pattern = os.path.join(search_path, f"{key}.jar")
        search_pattern = "**/" + key + ".jar"
        jar_files = glob.glob(search_pattern)
        
        # Initialize an empty list to store the moved file paths
        moved_files = []
        
        # Move each found jar file to the destination path
        for jar_file in jar_files:
            destination_file = shutil.move(jar_file, destination_path)
            print(f"Moved {jar_file} to {destination_path}")
            moved_files.append(destination_file)
        
        # Update the dictionary value with the list of moved file paths
        target_dict[key] = moved_files
    
    return target_dict

def save_dict_to_json(data_dict, output_path):
    with open(output_path, 'w') as json_file:
        json.dump(data_dict, json_file, indent=4)
    print(f"JSON file saved to {output_path}")

if __name__ == "__main__":
    # Create the dictionary from the TARGET environment variable
    target_dict = create_dict_from_env_variable()
    
    # Specify the directory where to search for .jar files
    search_directory = "/path/to/search/directory"
    
    # Move the .jar files based on the dictionary keys and update the dictionary
    updated_dict = move_jar_files(target_dict, search_directory)
    
    # Specify the output path for the JSON file
    output_json_path = "/path/to/output/directory/result.json"
    
    # Save the updated dictionary to a JSON file
    save_dict_to_json(updated_dict, output_json_path)
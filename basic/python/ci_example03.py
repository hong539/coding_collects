import os
import json
import subprocess

def get_target_list():
    # Get the environment variable TARGET's value
    target = os.getenv('TARGET')
    
    # If TARGET does not exist, return an empty list
    if target is None:
        return []
    
    # Split the TARGET value by "\n" and convert to a list
    target_list = target.split('\n')
    
    return target_list

def load_json_to_dict(json_path):
    # Load the JSON file and convert its content to a dictionary
    with open(json_path, 'r') as json_file:
        data_dict = json.load(json_file)
    
    return data_dict

def run_docker_push(target_list, data_dict):
    for key in target_list:
        if key in data_dict:
            # Get the value from the dictionary for the given key
            value = data_dict[key]
            # Construct the docker push command
            cmd = f"docker push {value}"
            print(f"Running command: {cmd}")
            # Execute the docker push command
            subprocess.run(cmd, shell=True, check=True)

if __name__ == "__main__":
    # Get the target list from the environment variable
    target_list = get_target_list()
    
    # Specify the path to the JSON file
    json_path = "/path/to/your/json_file.json"
    
    # Load the JSON file to a dictionary
    data_dict = load_json_to_dict(json_path)
    
    # Run the docker push commands based on the target list and the dictionary
    run_docker_push(target_list, data_dict)
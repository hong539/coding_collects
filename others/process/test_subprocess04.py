import subprocess

try:
    subprocess.call(['bash', '/path/to/script.sh'])
except subprocess.CalledProcessError as e:
    print(f"Error executing script: {e}")
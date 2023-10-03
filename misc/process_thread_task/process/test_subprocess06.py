import os
import subprocess

os.chmod('/path/to/script.sh', 0o755)
subprocess.call(['bash', '/path/to/script.sh'])
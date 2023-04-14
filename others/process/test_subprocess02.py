import subprocess

# 指定要執行的腳本
script_path = "/path/to/script.sh"

# 傳遞參數給腳本
args = ["arg1", "arg2", "arg3"]

# 執行腳本
subprocess.run(["bash", script_path] + args)
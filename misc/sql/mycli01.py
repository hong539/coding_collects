import subprocess

def run_mycli_command(command):
    try:
        # Run mycli command
        result = subprocess.run(
            ['mycli', '--defaults-group-suffix=_your_mysql_config_group_', '--execute', command],
            capture_output=True,
            text=True,
            encoding='utf-8'
        )
        # Check for errors
        if result.returncode != 0:
            print(f"Error: {result.stderr}")
            return None
        # Return output
        return result.stdout
    except Exception as e:
        print(f"Error: {e}")
        return None

# Example usage
query = "SELECT * FROM your_table;"
output = run_mycli_command(query)
if output:
    print(output)
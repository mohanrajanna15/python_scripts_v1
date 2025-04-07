# main.py

import helper
import os
import subprocess

if __name__ == "__main__":
    name = "Mohan"
    message = helper.greet(name)
    print(os.environ.get("PATH"))
    result = subprocess.run("whoami", shell=True, capture_output=True, text=True)
    print(result.stdout)
    print(message)

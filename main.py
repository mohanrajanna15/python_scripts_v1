# main.py

import helper
import os

if __name__ == "__main__":
    name = "Alice"
    message = helper.greet(name)
    print(os.environ.get("PATH"))
    print(message)

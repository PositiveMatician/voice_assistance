import importlib
import sys

import os
from dotenv import load_dotenv
load_dotenv()
DEBUG:bool = os.getenv("DEBUG") == "True"


def import_all_from_current_directory() -> dict:
    """
    Imports all Python files from the current directory.
    Each module is expected to have a function with the same name as the file.
    Returns a list of those functions.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))

    if current_dir not in sys.path:
        sys.path.insert(0, current_dir)

    collected_functions = dict()

    for filename in os.listdir(current_dir):
        if filename.endswith(".py") and filename != os.path.basename(__file__):
            module_name = filename[:-3]  # Strip .py extension
            function_name = module_name   # Function name matches module name

            try:
                module = importlib.import_module(module_name)
                func = getattr(module, function_name, None)

                if callable(func):
                    collected_functions[function_name] = func
                    if DEBUG: print(f"Found '{function_name}' in: {module_name}")
                else:
                    if DEBUG: print(f"No callable '{function_name}' in: {module_name}")

            except Exception as e:
                if DEBUG: print(f"Failed to import {module_name}: {e}")

    return collected_functions

if __name__ == "__main__":
    functions = import_all_from_current_directory()
    if DEBUG: print(f"Collected functions: {[func.__name__ for func in functions.values()]}")
import os

def load_instructions_file(file_path:str, default :str = "No instructions provided.") -> str:
    """
    Load instructions from a text file.
    :param file_path: Path to the instructions file.
    :return: Content of the file as a string. If the file does not exist or is empty, returns a default message.

    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read().strip() #read and return the entire file contents
    except FileNotFoundError:
        #if the file doesn't exist, return the default message
        print(f"[WARNING] File not found: {file_path}. Returning default instructions.")
        return default
    except Exception as e:
        #print(f"[ERROR] Error loading instructions: {e}")
        return f"[ERROR] Error loading instructions: {e}"

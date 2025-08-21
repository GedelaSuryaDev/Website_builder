from datetime import datetime
from pathlib import Path

def write_to_file(file_path: str, content: str) -> dict:
    """
    Write the provided content to a specific file path.
    :Args:
        file_path (str): The relative path where the file should be saved (e.g., "src/App.jsx").
        content (str): The content to be written to the file.
    :return: A dictionary with the status of the write operation.
    """
    try:
        # Ensure the output directory exists
        output_dir = Path("output")
        full_path = output_dir/Path(file_path)
        #full_path =f"{output_dir}/{file_path}"
        full_path.parent.mkdir(parents=True, exist_ok=True)

        # Write the content to the specified file
        with open(full_path, 'w', encoding='utf-8') as file:
            file.write(content)

        return {"status": "success", "file_path": str(full_path)}
    except Exception as e:
        return {"status": "error", "message": str(e)}
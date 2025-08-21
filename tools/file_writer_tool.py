from datetime import datetime
from pathlib import Path
#import path from pathlib for convienient and safe file/directory handling
def write_to_file(content: str)->dict:
    """
    Write  the HTML/CSS/JS file to timestamped HTML file. 
    :Args: 
        content (str): Full HTML content as a string to be saved to the file.
    :return: A dictionary with the status of the write operation.
    """
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        # Create a filename with the current timestamp
        # This ensures that each file is unique and avoids overwriting previous files
        file_path = f"output/{timestamp}_generated_page.html"

        # Define the file path where the file will be saved
        # make sure the output directory exists. if doesn't, create it
        #file_path = Path("output").mkdir(exist_ok=True)
        #write the HTML contnt to the constructed file path.
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        return {"status": "success", "file_path": str(file_path)}
    except Exception as e:
        return {"status": "error", "message": str(e)}
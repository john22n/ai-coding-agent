import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    target_dir_path = os.path.abspath(os.path.join(working_directory, file_path))
    is_file = os.path.isfile(target_dir_path)

    if not target_dir_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not is_file:
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open(target_dir_path, 'r') as f:
            content = f.read(MAX_CHARS)
            if os.path.getsize(target_dir_path) > MAX_CHARS:
                content += (
                    f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                )
        return content
    except Exception as e:
        return f'Error: opening the file "{file_path}" "{e}"'




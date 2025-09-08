import os
from google.genai import types

MAX_CHARS = 10000

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



schema_get_files_content = types.FunctionDeclaration(
    name="get_file_content",
    description="use this tool to get the contents of a file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
        required=["file_path"],
    ),
)

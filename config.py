from google.genai import types
from functions.get_files_info import schema_get_files_info 
from functions.get_file_content import schema_get_files_content
from functions.write_file import schema_write_file 
from functions.run_python import schema_run_python_file


system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

available_tools = types.Tool(
        function_declarations=[schema_get_files_content, schema_write_file, schema_get_files_info, schema_run_python_file]
)

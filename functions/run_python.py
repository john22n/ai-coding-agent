import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    abs_working = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory.'

    if not os.path.exists(file_path):
        return f'Error: File "{file_path}" not found.'
    
    if not ".py" in file_path:
        return f'Error: "{file_path}" is not a Python file.'

    try:
        cmds = ["python", abs_file_path]
        if args:
            cmds.extend(args)
        result = subprocess.run(
            cmds,
                capture_output=True,
                text=True,
                timeout=30,
                cwd=abs_working
        )
        output = []
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")

        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")

        return "\n".join(output) if output else "No output produced."
    except Exception as e:
        return f'{e}'

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="use this tool to run python scripts, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

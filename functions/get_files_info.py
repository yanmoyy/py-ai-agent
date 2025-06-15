import os

from google.genai import types


class FileInfo:
    def __init__(self, name, size, id_dir=False):
        self.name = name
        self.size = size
        self.id_dir = id_dir

    def __str__(self):
        return f"{self.name}: file_size={self.size} bytes, is_dir={self.id_dir}"


def get_files_info(working_directory, directory=None):
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = abs_working_dir
    if directory:
        target_dir = os.path.abspath(
            os.path.join(working_directory, directory),
        )

    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'

    try:
        file_info = []
        for filename in os.listdir(target_dir):
            file_path = os.path.join(target_dir, filename)
            if os.path.isdir(file_path):
                file_info.append(FileInfo(filename, os.path.getsize(file_path), True))
            else:
                file_info.append(FileInfo(filename, os.path.getsize(file_path)))

        str_file_info = "\n".join(["- " + str(info) for info in file_info])
        return str_file_info
    except Exception as e:
        return f"Error: listing files: {e}"


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
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

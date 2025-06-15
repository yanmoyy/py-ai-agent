# Python AI Agent

- This is a simple AI agent CLI written in Python.
- From boot.dev

## Goal of this project

1. To learn multi-directory Python project structure.
2. Understand how the AI tools actually work under the hood.
3. Practice Python and Functional programming.
4. Not Building LLM from scratch, but building an Agent from scratch.

## Features

- there are several functions available to the agent:
  - get_files_info
  - get_file_content
  - run_python_file
  - write_file

1. get_files_info
   - lists all files and directories in a given directory
2. get_file_content
   - reads the content of a file
3. run_python_file
   - runs a Python file
4. write_file
   - writes content to a file

## Requirements

.env file is required to run the agent.

```bash
GEMINI_API_KEY=your-api-key
```

## Usage

```bash
python main.py "your prompt here"

# Example:
python main.py "How do I build a calculator app?"
```

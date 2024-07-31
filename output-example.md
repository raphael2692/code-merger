## Folder Structure
```
    code_merge.egg-info/
    merge/
        __init__.py
        __pycache__/
        merge.py
    setup.py
```

## C:\\dev\\merge-util\\setup.py
```python
from setuptools import setup, find_packages

setup(
    name='code_merge',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'merge = merge.merge:main',
        ],
    },
)
```

## C:\\dev\\merge-util\\merge\\merge.py
```python
import argparse
from pathlib import Path
import tkinter as tk

DEFAULT_EXTENSIONS = ["ts", "py", "css", "scss", "html", "js", "jsx", "tsx"]
DEFAULT_OUTPUT_FILE = "merged.md"

def escape_markdown_characters(text):
    escaped_text = text.replace("\\", "\\\\").replace("_", "\\_").replace("#", "\\#").replace("`", "\\`")
    return escaped_text

def create_folder_structure_illustration(root_path, extensions):
    tree = ""
    for path in sorted(root_path.rglob('*')):
        if path.is_dir():
            depth = len(path.relative_to(root_path).parts)
            indent = '    ' * depth
            tree += f"{indent}{path.name}/\n"
        elif path.suffix[1:] in extensions:
            depth = len(path.relative_to(root_path).parts) - 1
            indent = '    ' * (depth + 1)
            tree += f"{indent}{path.name}\n"
    return tree

def merge_files(extensions, root_path):
    content = ""
    for ext in extensions:
        for file_path in root_path.rglob(f"*.{ext}"):
            try:
                file_path_str = str(file_path)
                escaped_file_path = escape_markdown_characters(file_path_str)
                content += f"\n## {escaped_file_path}\n"

                if ext == "py":
                    content += "```python\n"
                elif ext == "html":
                    content += "```html\n"
                elif ext == "css":
                    content += "```css\n"
                elif ext == "js":
                    content += "```javascript\n"
                elif ext == "jsx":
                    content += "```jsx\n"
                elif ext == "tsx":
                    content += "```tsx\n"
                elif ext == "ts":
                    content += "```typescript\n"
                elif ext == "scss":
                    content += "```scss\n"

                with file_path.open("r", encoding="utf-8") as f:
                    content += f.read()

                content += "\n```\n"
            except Exception as e:
                print(f"Error reading file {file_path}: {e}")
    return content

def save_to_file(content, output_path):
    try:
        with output_path.open("w", encoding="utf-8") as file:
            file.write(content)
    except Exception as e:
        print(f"Error writing to output file {output_path}: {e}")

def copy_to_clipboard(content):
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    root.clipboard_clear()
    root.clipboard_append(content)
    root.update()  # Now it stays on the clipboard after the window is closed
    root.destroy()

def main():
    parser = argparse.ArgumentParser(description="Merge files with specified extensions.")
    parser.add_argument("-e", "--extensions", nargs="*", help="List of file extensions to merge.")
    parser.add_argument("-f", "--filename", help="Name of the output file (default: merged.md).")
    args = parser.parse_args()

    extensions = args.extensions or DEFAULT_EXTENSIONS
    root_path = Path.cwd()
    folder_structure = create_folder_structure_illustration(root_path, extensions)
    content = merge_files(extensions, root_path)

    full_content = f"## Folder Structure\n```\n{folder_structure}```\n{content}"
    
    if args.filename:
        output_path = Path(args.filename)
        save_to_file(full_content, output_path)
        print(f"Merged content saved to: {output_path}")
    else:
        copy_to_clipboard(full_content)
        print(folder_structure)
        print("Folder structure and merged content copied to clipboard.")

if __name__ == "__main__":
    main()
```

## C:\\dev\\merge-util\\merge\\\_\_init\_\_.py
```python

```

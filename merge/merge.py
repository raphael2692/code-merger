import argparse
from pathlib import Path
import tkinter as tk

# Updated to include more markdown-supported languages
DEFAULT_EXTENSIONS = [
    "ts", "py", "css", "scss", "html", "js", "jsx", "tsx", "yaml", "yml", 
    "json", "md", "c", "cpp", "java", "rb", "go", "rs", "sh", "pl", "php", 
    "swift", "kotlin", "r", "m", "h"
]
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
                
                language_map = {
                    "py": "python",
                    "html": "html",
                    "css": "css",
                    "js": "javascript",
                    "jsx": "jsx",
                    "tsx": "tsx",
                    "ts": "typescript",
                    "scss": "scss",
                    "yaml": "yaml",
                    "yml": "yaml",
                    "json": "json",
                    "md": "markdown",
                    "c": "c",
                    "cpp": "cpp",
                    "java": "java",
                    "rb": "ruby",
                    "go": "go",
                    "rs": "rust",
                    "sh": "shell",
                    "pl": "perl",
                    "php": "php",
                    "swift": "swift",
                    "kotlin": "kotlin",
                    "r": "r",
                    "m": "objectivec",
                    "h": "c"
                }

                language = language_map.get(ext, "")
                if language:
                    content += f"```{language}\n"
                else:
                    content += "```\n"  # fallback to a default code block if extension is not in the map

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

    full_content = f"## Project Structure\n```\n{folder_structure}```\n{content}"
    
    print("Merging:")
    if args.filename:
        output_path = Path(args.filename)
        save_to_file(full_content, output_path)
        print(f"Merged and saved to: {output_path}")
    else:
        copy_to_clipboard(full_content)
        print(folder_structure)
        print("Merged and copied to clipboard!")

if __name__ == "__main__":
    main()
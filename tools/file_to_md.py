import argparse
from tqdm import tqdm
from pathlib import Path
from markitdown import MarkItDown


def convert_directory_to_md(input_dir: Path, delete_source: bool = False):
    """
    Convert files to Markdown beside each original, skipping existing outputs.
    :param input_dir: str
        The Path object pointing to the directory to process.
    :param delete_source: bool = False
        Whether to delete the original source files. Defaults to False.
    """

    md = MarkItDown(enable_plugins=False)

    # get list of files to convert
    files_to_process = [f for f in input_dir.rglob('*') if f.is_file()]

    if not files_to_process:
        print(f"No files found in {input_dir}!")
        return

    for file_path in tqdm(files_to_process, desc="Converting Files"):
        # skip hidden files and existing markdown files
        if file_path.name.startswith('.') or file_path.suffix.lower() == '.md':
            print(f"Skipping conversion of {file_path.name}")
            continue

        # convert filepath to md
        output_path = file_path.with_suffix(".md")
        if output_path.exists():
            tqdm.write(f"Skipping existing Markdown: {output_path.name}")
            continue
        try:
            # convert
            result = md.convert(str(file_path))
            # save to .md
            with output_path.open("x", encoding="utf-8") as output_file:
                output_file.write(result.text_content)
            # optional remove original file
            if delete_source:
                file_path.unlink()
            tqdm.write(f"Converted: {file_path.name}")
        except Exception as e:
            tqdm.write(f"FAILED: Could not convert '{file_path.name}'. Reason: {e}")


def main(args):
    # set Paths
    input_path = Path(args.input_dir).resolve()
    print("-" * 40)
    print(f"Input Directory: {input_path}")
    print("-" * 40)

    # execute
    try:
        convert_directory_to_md(input_path, args.delete_source)
        print("\nConversion process complete.")
    except FileNotFoundError:
        print(f"\nError: Input directory not found at {input_path}")
    except Exception as e:
        print(f"\nAn unexpected error occurred during execution: {e}")


if __name__ == "__main__":
    """Command-line arguments."""
    parser = argparse.ArgumentParser(description="Convert files to Markdown beside the originals; skip existing Markdown outputs.")
    parser.add_argument(
        "--input_dir",
        type=str,
        help="The path to the directory containing files to convert."
    )
    parser.add_argument(
        "--delete_source",
        action="store_true",
        help="Whether to delete the original source files."
    )
    args = parser.parse_args()

    main(args)

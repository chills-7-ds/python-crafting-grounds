import argparse
import shutil

def backup_folder(source, destination, compress=False):
    """
    Copies a folder from source to destination using shutil only.
    Optionally compresses the copied folder into a .zip file.
    """
    try:
        print(f"🔄 Copying from '{source}' to '{destination}'...")
        # Copies the directory recursively; merges if destination exists
        shutil.copytree(source, destination, dirs_exist_ok=True)
        print("✅ Folder copied successfully.")

        # Optional compression
        if compress:
            archive_name = shutil.make_archive(destination, "zip", destination)
            print(f"📦 Compressed archive created: {archive_name}")

    except Exception as e:
        print(f"❌ Error: {e}")

def main():
    parser = argparse.ArgumentParser(
        description="PyBackup Lite - Simple Folder Backup Tool (shutil-only)"
    )

    # Two required positional arguments
    parser.add_argument("source", help="Path to the source folder to back up")
    parser.add_argument("destination", help="Path to the destination folder or archive name (without .zip)")

    # Optional flag to compress after copying
    parser.add_argument(
        "--compress", 
        action="store_true", 
        help="Compress the copied folder into a ZIP archive"
    )

    args = parser.parse_args()
    backup_folder(args.source, args.destination, args.compress)

if __name__ == "__main__":
    main()

import os

def explore_directory(path):
    if not os.path.exists(path):
        print("❌ Path does not exist.")
        return

    items = os.listdir(path)
    files = []
    folders = []

    for item in items:
        full_path = os.path.join(path, item)
        if os.path.isfile(full_path):
            files.append((item, os.path.getsize(full_path)))
        elif os.path.isdir(full_path):
            folders.append(item)

    print(f"\n📁 Exploring: {path}")
    print("\n📂 Folders:")
    for folder in folders:
        print(f"   - {folder}")
    
    print("\n📄 Files:")
    for file, size in files:
        print(f"   - {file} ({size // 1024} KB)")

    print(f"\n✅ Total folders: {len(folders)}")
    print(f"✅ Total files: {len(files)}")

if __name__ == "__main__":
    folder = input("Enter folder path (leave empty for current directory): ").strip()
    if not folder:
        folder = os.getcwd()

    explore_directory(folder)
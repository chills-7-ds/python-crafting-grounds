## **PyBackup Lite**

`PyBackup Lite` is a simple yet functional **command-line folder backup tool** built purely using Python’s **`shutil`** standard library.
It demonstrates high-level file operations — copying and compressing directories — without relying on any external dependencies.
A practical example of how Python alone can automate everyday backup workflows.
---

## **Goal**

To **understand and implement real-world file operations** using the `shutil` module.
Specifically, this project aims to:

* Demonstrate how to copy and archive folders via CLI.
* Practice command-line argument handling using `argparse`.
* Build confidence in Python’s standard libraries for system tasks.

---

## **Tech Stack**

**Language:** Python 3.8+
**Libraries Used:**

* `shutil` — for copying, archiving, and managing files/folders.
* `argparse` — for parsing command-line arguments.

(No database or third-party packages used.)

---

## **Features**

* 📂 Copy entire folders recursively from source to destination.
* 🗜️ Optional compression into `.zip` archives using `--compress`.
* 💥 Error-handling for invalid paths or missing directories.
* 🧱 Simple, portable, and dependency-free — works cross-platform.

---

## **How to Run**

### **1. Clone or Download**

Save the script as:

```
pybackup_lite.py
```

### **2. Run in Terminal (VS Code or CMD)**

Basic copy:

```bash
python pybackup_lite.py "C:\path\to\source_folder" "D:\path\to\backup_folder"
```

Copy and compress:

```bash
python pybackup_lite.py "C:\path\to\source_folder" "D:\path\to\backup_folder" --compress
```

### **Example Output**

```
🔄 Copying from 'C:\path\to\source_folder' to 'D:\path\to\backup_folder'...
✅ Folder copied successfully.
📦 Compressed archive created: D:\path\to\backup_folder.zip
```

---

## **Possible Extensions**

* 🧩 Add support for single-file backups (`shutil.copy`).
* 🔁 Add restore functionality using `shutil.unpack_archive`.
* 🕒 Include timestamps or versioned backups.
* 🧹 Optional cleanup for old backups.
* 📜 Log backup history to a file for audit or tracking.

---

## **Notion Site**

[📘 Read More on Notion → **shutil-bts**](https://dramatic-psychology-0d8.notion.site/shutil-bts-29303656c6c380d688fae3343ed44fd4?source=copy_link)

---

**See you in the next one! 🚀**
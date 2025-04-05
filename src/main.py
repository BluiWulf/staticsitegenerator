import os
import shutil

def main():
    copy_static()

def copy_static(base_path = ""):
    contents = []
    main_src = os.path.join("static", base_path)
    main_dest = os.path.join("public", base_path)

    if os.path.exists(main_dest):
        shutil.rmtree(main_dest)
    os.mkdir(main_dest)

    contents.extend(os.listdir(main_src))
    for item in contents:
        src = os.path.join(main_src, item)
        dest = os.path.join(main_dest, item)
        print(f" * {src} -> {dest}")
        if os.path.isfile(src):
            shutil.copy(src, dest)
            continue
        if not os.path.exists(dest):
            copy_static(item)

if __name__ == "__main__":
    main()
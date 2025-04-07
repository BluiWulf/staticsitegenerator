from generatepage import generate_pages_recursive, copy_static

import os
import pathlib

def main():
    copy_static()

    dest_path = "public"
    template_path = "template.html"
    from_path = "content"

    generate_pages_recursive(from_path, template_path, dest_path)

if __name__ == "__main__":
    main()
from generatepage import generate_pages_recursive, copy_static

import sys
import os

def main():
    if len(sys.argv) > 1:
        if not sys.argv[1] is None:
            base_path = sys.argv[1]
    else:
        base_path = "/"
    dest_path = "docs"
    template_path = "template.html"
    from_path = "content"

    copy_static(dest_path)
    generate_pages_recursive(base_path, from_path, template_path, dest_path)

if __name__ == "__main__":
    main()
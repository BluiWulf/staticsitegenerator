import os
import shutil

from block_parser import *
from converter import markdown_to_html_node

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

def extract_title(markdown):
    headers = extract_markdown_headers(markdown)

    if len(headers) == 0:
        raise Exception("A title (h1 header) is required")
    for header in headers:
        if header[0] == "#":
            return header[1]
    raise Exception("A title (h1 header) is required")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating html page from {from_path} to {dest_path} using {template_path}")

    input_md = open(from_path, 'r')
    markdown = input_md.read()
    input_md.close()

    template_file = open(template_path, 'r')
    template = template_file.read()
    template_file.close()

    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    new_page = template.replace("{{ Title }}", title).replace("{{ Content }}", html)

    if not os.path.exists(os.path.join(os.path.dirname(dest_path))):
        os.makedirs(os.path.join(os.path.dirname(dest_path)), exist_ok = True)
    output_html = open(dest_path, 'w')
    output_html.write(new_page)
    output_html.close()

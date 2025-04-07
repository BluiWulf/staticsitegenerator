from generatepage import generate_page, copy_static

def main():
    copy_static()

    dest_path = "public/index.html"
    template_path = "template.html"
    from_path = "content/index.md"

    generate_page(from_path, template_path, dest_path)

if __name__ == "__main__":
    main()
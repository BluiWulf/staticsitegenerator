
def markdown_to_blocks(markdown):
    sections = []
    blocks = []

    sections = markdown.split("\n\n")
    for section in sections:
        if section != "":
            blocks.append(section.strip())

    return blocks
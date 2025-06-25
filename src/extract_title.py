def extract_title(markdown):
    if markdown.startswith("# "):
        split_markdown = markdown.split("\n", 1)
        return split_markdown[0].strip("#").strip()
    else:
        raise Exception ("no heading found")





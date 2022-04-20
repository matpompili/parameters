import re

def _lint_yaml_file(file_path: str) -> None:
    """Lint a yaml file, such that it passes yamllint.

    Args:
        file_path: the path to the file to lint.
    """

    # Fix spaces between comments
    # https://regex101.com/r/prKl93/2
    with open(file_path, "r", encoding="UTF-8") as handle:
        content = handle.read()
        regex = r"^(\s*\w+[^\n\r#]+?)(?:[ \t]*)#(?:\s*)([^\n\r]*)$"
        subst = "\\g<1>  # \\g<2>"
        content_new = re.sub(regex, subst, content, 0, re.MULTILINE)
    with open(file_path, "w", encoding="UTF-8") as handle:
        handle.write(content_new)

    # Fix spaces at the end of the line and a final new line
    with open(file_path, "r", encoding="UTF-8") as handle:
        content = handle.read()
        regex = r"^(.*?)(?:\s*)$"
        subst = "\\g<1>"
        content_new = re.sub(regex, subst, content, 0, re.MULTILINE)
    with open(file_path, "w", encoding="UTF-8") as handle:
        handle.write(content_new + "\n")
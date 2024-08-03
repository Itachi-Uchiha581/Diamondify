def extract_code_without_backticks(text):
    split_text = text.split("\n")
    if "" in split_text[1]:
        split_text.pop(1)
    if split_text[0] == "" or "" in split_text[0]:
        split_text.pop(0)
    if "" in split_text[-1]:
        split_text.pop(-1)
    if "" in split_text[-2]:
        split_text.pop(-2)

    return split_text

def write_file(file_name, file_content):
    text_file = open(file_name+ ".txt", mode="w", encoding="utf-8")
    text_file.write(file_content)
    text_file.close()

def append_file(file_name, append_content):
    text_file = open(file_name + ".txt", mode="a", encoding="utf-8")
    text_file.write(append_content)
    text_file.close()

def read_file(file_name):
    with open(file_name + ".txt", mode="r", encoding="utf-8") as text:
        string = text.read()

    return string

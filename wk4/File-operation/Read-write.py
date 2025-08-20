def modify_content(content):
    # Example: reverse each line
    return '\n'.join(line[::-1] for line in content.splitlines())

def read_and_write():
    with open("input.txt", "r") as infile:
        content = infile.read()

    modified = modify_content(content)

    with open("output.txt", "w") as outfile:
        outfile.write(modified)

    print("✅ File processed and saved as 'output.txt'.")

read_and_write()
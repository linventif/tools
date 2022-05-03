file_html = open('index.html', "r")
file_ino = open("code-convert.ino", "w")

lines = file_html.readlines()
file_html.close()

for line in lines:
    line = line.replace("\"", "'")

    line = f"page += \"{line}\";"
    #line = f"client.println(\"{line}\");"
    line = line.replace("\n", "")

    line = f"{line} \n"
    file_ino.write(line)

file_ino.close()
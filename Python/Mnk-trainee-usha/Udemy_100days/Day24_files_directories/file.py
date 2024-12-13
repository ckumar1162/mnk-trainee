# #to read a content of a file
# with open("my_file.txt") as f:
#     content=f.read()
#     print(content)

with open ("my_file.txt","a") as f:
    file=f.write("\nMnk Gcs")
    print(file)
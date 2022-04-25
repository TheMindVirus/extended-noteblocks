import os

path = os.path.join(os.getcwd(), "assets/minecraft/textures")
suffix = "_e"

for root, dirs, files in os.walk(path):
    for filename in files:
        filepath = os.path.join(root, filename)
        name, extension = os.path.splitext(filename)
        if extension == ".png":
            newname = name + suffix + extension
            newpath = os.path.join(root, newname)
            print(newpath)
            file = open(filepath, "rb")
            data = file.read()
            file.close()
            file = open(newpath, "wb")
            file.write(data)
            file.close()
print("Done!")

import os


def testConversion(file):

    filePath = file.split("/")
    filePath = filePath[len(filePath)-1]

    # Replacing spaces with dashes for less web browsing
    filePath = filePath.replace(" ", "_")

    # Only get the filename from the absolute directory
    filePathArray = filePath.rsplit("/")
    fileName = filePathArray[len(filePathArray) - 1]
    fileName = fileName.replace(".mp3", "")
    print(f"\n{fileName}\n")

    if (not (os.path.exists(f"splitted/{fileName}"))):
        os.mkdir(f"../splitted/{fileName}")

    returnFiles = []
    returnFiles.append(f"splitted/{fileName}/instrumental.mp3")
    returnFiles.append(f"splitted/{fileName}/vocals.mp3")

    return returnFiles


if __name__ == "__main__":
    name = testConversion("../Betty G Nhatty Man.mp3")
    print(name)
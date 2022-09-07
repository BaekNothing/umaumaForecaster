import os 
import pytest
from PIL import Image

def CheckDirExist(dir : str) -> bool :
    return os.path.isdir(dir)

def CheckFileExist(file : str) -> bool :
    return os.path.isfile(file)

def SaveFile(filePath : str, content : str) -> bool :
    try:
        with open(filePath, "w") as file:
            file.write(content)
        return True
    except:
        return False

def ReadFile(filePath : str) -> str :
    try:
        with open(filePath, "r") as file:
            return file.read()
    except:
        return ""

def SaveCapturedImage(filePath : str, image : Image) -> bool :
    try:
        image.save(filePath)
        return True
    except:
        return False

def GetFilesInDir(dir : str) -> list :
    try:
        return os.listdir(dir)
    except:
        return []
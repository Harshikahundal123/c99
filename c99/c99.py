import os 
import shutil
#os.mkdir("test")
path = "c:/Users/Harpal Singh/Downloads/python/Classes/c99/test/"
isExist = os.path.exists(path)
print(isExist)
root_ext=os.path.splitext(path)
print("rootpart",root_ext[0])
print("extpart",root_ext[-1],"\n")
os.listdir()
print("Before copying files:")
print(os.listdir(path))
source= "c:/Users/Harpal Singh/Downloads/python/Classes/c99/test/file.txt"
destination="c:/Users/Harpal Singh/Downloads/python/Classes/c99/test/file1.txt"
dest = shutil.copy(source,destination)
print("After copying files")
print (os.listdir(path))
path1 = "c:/Users/Harpal Singh/Downloads/python/Classes/c99/test/videos"
print("Before Moving File")
print(os.listdir(path1))
source1 = "c:/Users/Harpal Singh/Downloads/python/Classes/c99/test/videos/mp4"
destination1 = "c:/Users/Harpal Singh/Downloads/python/Classes/c99/test/videos/png"
dest1 = shutil.move(source1, destination1)
print("After moving file")
print(os.listdir(path1))

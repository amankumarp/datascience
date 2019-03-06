import shutil
import os
# print(os.getcwd())#it function return the current working directory
# print(os.mkdir("test"))# function create the new directory in the current working directory
# print(os.path.exists('test'))# it function return the true if directory exist in current working directory
# ex1
# if os.path.exists("test"):
#     print("folder already exist")
# else:
#     os.mkdir("test")
# os.chdir(path)# it fuction take specific path for change the current working directory
# print(os.listdir())#it return the a list of file and folder in the current working directory
# for item in os.listdir():
#     print(os.getcwd()+'\\'+item)
# for item in os.listdir():
#     path=os.path.join(os.getcwd(),item)
#     print(path)
# for item in os.listdir('c:\\'):
#     path=os.path.join('C:\\',item)
#     print(path)
# filename=os.walk('a:\\')
# for cur,fold,file in filename:
#     print(cur)
#     print(fold)
#     print(file)
# os.rmdir(dirname) # function delete the empty folder
# os.makedirs('new\\movies')# it function create ones more directiry in that time
# shutil.rmtree("test")#it function takes directory name for delete with items

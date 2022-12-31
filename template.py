import os

# required directories
dirs =[
    "Data_given", # get the data from the cloud or resouce or import dataset
    os.path.join("data","raw"), # data is directory and raw is folder, save preprocess data
    os.path.join("data","processed"),# data is directory and processed is folder,split&save train test data
    "notebooks", # notebook is directory
    "saved_models", # saved_model is directory
    "src" # src is directory and make a separate file for every step performed 
]

# add required directories to the project

for dir in dirs:
    os.makedirs(dir,exist_ok=True)
#exist_ok=True-->if the dir is not created will create and if it is created will simply ignore
#exist_ok=False-->if the dir is not created will create and and if it is created will throw error'''
    with open(os.path.join(dir,".gitkeep"), 'w') as f:
    #it will create all the .gitkeep file inside all dirs
        pass
    
    


# required files
files =[
    "dvc.yaml", 
    "params.yaml",
    os.path.join("src","__init__.py")
]

# add required files to the project
for file in files:
    with open(file, 'w') as f:
        pass
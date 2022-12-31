# mlops-practice/Steps of MLOPS

Creating a Setup:
1. Create suitable venv
conda create -n venv3.7 python=3.7 -y

2. Create requirements.txt
Add all the required libraries and install them using command
pip install -r requirements.txt

3. Create template.py
In template.py create required directories and required files of the project

4. Dataset loaded at data_given directory manually

5. git init

6. dvc init

7. dvc add data_given\winequality.csv (To track the data)

   To push changes in repository 
   git add . && git commit -m "<message>"
   git push (from) origin (to) main

# Main operation steps:

1. Params.yaml file
Define all the parameters to run this project

2. create get_data.py in src dir

3. create load_data.py in src dir

4. dvc.yaml file
   define stage -01(load_dataset) and run using command dvc repro
   all the changes will be updated in dvc.lock file for stage-01

5. define stage -01(spit_data) and run using command dvc repro
   all the changes wiil be updated in dvc.lock file for stage-02
   
6. define stage -03(train_evaluate) and run using command dvc repro
   all the changes wiil be updated in dvc.lock file for stage-03
   change parameters in params.yaml and test accuracy again
   to see the chnages and effects in previous and current parameters 
   run comman dvc metrics diff
   to see all metrices 
   run command dvc metrics show


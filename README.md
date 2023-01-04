# mlops-practice/Steps of MLOPS

Creating a Setup:
1. Create suitable venv
conda create -n venv3.7 python=3.7 -y

2. Create requirements.txt
Add all the required libraries and install them using command
pip install -r requirements.txt

3. Create template.py
In template.py create required directories and files for the project

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
   1. define stage -01(load_dataset) and run using command dvc repro
      all the changes will be updated in dvc.lock file for stage-01

   2. define stage -01(spit_data) and run using command dvc repro
      all the changes wiil be updated in dvc.lock file for stage-02
   
   3. define stage -03(train_evaluate) and run using command dvc repro
      all the changes wiil be updated in dvc.lock file for stage-03
      change parameters in params.yaml and test accuracy again
      to see the chnages and effects in previous and current parameters 
      run command dvc metrics diff
      to see all metrices 
      run command dvc metrics show
5. create tox.ini
   1. it is used to automate testing in python.
   2. it will create virtual enviornment for the project and install dependencies. 
      adv of tox is list of venv's can be given
   3. it has command to run pytest (used to run and test 
      files inside tests directories)
   4. it also has requirements.txt as dependency to create venv
   5. test  to confirm whether code is running on multiple venv's
      run command for tox is 'tox'.
   6. rebuilding : run command is tox -r if we update requirements.txt 
   7. run command for pytest is pytest -v(v for verborse)
6. tests folder is created to put all the tests in one place
   1. inside test folder create conftest.py
   2. inside test folder create test_config.py
   3. inside test folder create __init__.py
   pytest is used for run and test, tests(conftest,test_config) saved inside tests folder
   after saving tests inside tests folder run pytest using command pytest -v or by using tox can also be tested

6. create setup.py file for creating our own packages
   1. at setup.py by default we have to give some details regarding project such as 
      folder, version, description, author, License and many other.
   2. using command pip install -e . to install libraries mention in local directories 
      (by now there are  only two directories which has libraries install src and test) 
      will collect and installed
   3. If needed only 
      command : python setup.py sdist bdist wheel(If needed only, It will add all the packages dist directory and .tar.gz file inside and if needed can share with friends to install all the libraries)

jupter notebook:
pip install jupyterlab
run command jupyter-lab notebooks/

7. create app.py file

8. Create webapp folder

9. Create Procfile for deploying app using Heroku

10. Create artifacts folder

11. mlflow server command
mlflow server \
   --backend-store-uri sqlite:///mlflow.db \
   --default-artifact-root ./artifacts \
   --host 0.0.0.0 -p 1234

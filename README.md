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
DVC Pipeline
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
Till Now: using dvc, created dvc pipeline for this project there were 3 stages(stored in src directory)

Testing:
5. create tox.ini
   1. it is used to automate testing in python.
   2. it will create virtual enviornment for the project and install dependencies,
      adv of tox is list of venv's can be given to test suitable python version.
   3. inside tox.ini, command is given to run pytest (To run and test 
      files inside tests directories)
   4. inside tox.ini, requirements.txt as dependency is given helps in creating venv
   5. To test using tox, run command: 'tox'
   6. if we update requirements.txt then rebuilding is required, it can be done using: tox -r command
   7. command to pytest:  pytest -v(v for verborse)
6. tests folder is created to put all the tests parameters in one place
   1. inside test folder, create conftest.py
   2. inside test folder, create test_config.py
   3. inside test folder, create __init__.py
   by using pytest files inside tests folder can be tested.
7. setup.py file
   1. in setup.py, by default we have to give some details regarding project such as 
      folder, version, description, author, License and many other.
   2. using command pip install -e . to install libraries mention in local directories 
      (by now there are  only two directories which has libraries install src and test) 
      will collect and installed
   3. If needed only 
      command : python setup.py sdist bdist wheel(If needed only, It will add all the packages dist directory and .tar.gz file inside and if needed can share with friends to install all the libraries)
8. Create directory by name prediction_service and create another directory inside prediction_service
   by name model and create files inside prediction_service, prediction.py and __init__.py 
      1. inside prediction_service\prediction.py define all the methods required for app.py
         (for code to look modular and clean)
      2. because schema_in.json is required in prediction_service copy from notebooks\schema_in.json
         to prediction_service\schema_in.json
      
Create app
9. Create app.py file for all the flask functions

10. Create webapp directory 
   1. Create static folder
      1. Create css and script files
         1. inside css create main.css file
         2. inside script file create index.js file
   2. Create template folder for all the html files
      1. base.html
      2. index.html
      3. 404.html

9. Create .github directory for github actions
   1. inside directory create folder workflows
   2. inside .github add ci-cd.yaml file


9. Create Procfile for deploying app using Heroku

Till now using dvc, created dvc pipeline for this project there were 3 stages(stored in src directory)
GitHub Actions, testing and linting process is done, added which helps to deploy app through Heroku
testing is done at main branch --> tests directory, app.py and prediction services
Here we are performing continues Integration--> continues Testing-->continues Deployment.

In future, for model versioning mlflow library is used

10. Create artifacts folder

11. mlflow server command
mlflow server \
   --backend-store-uri sqlite:///mlflow.db \
   --default-artifact-root ./artifacts \
   --host 0.0.0.0 -p 1234


jupter notebook:
pip install jupyterlab
run command jupyter-lab notebooks/
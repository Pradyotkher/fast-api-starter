# Create a  virtual Environment first after making the directory of your project.

# Command to creatre a virtual environment in python 
python -m venv {env_name}

.\{env_name}\Scripts\activate Activates the Virtual environment
pip install "fastapi[standard]"

# Add the requirements.txt file to your  project
pip freeze > requirements.txt

pip install -m requirements.txt


# For post request and put requests , we nneed to pass a body and to achieve that : 
# from pydantic import BaseModel

class class_Name(BaseModel):
    *all class entities*

# To connect the fastAPI application to MYSQL, we can host the MYSql server on docker and start it as a docker container 
# once the docker container is up and running , we can add the credentials of the username and password in the python app 
# and connect it 

# In python , the models.py is the Databse Schemas , sqlalchemy which represents all the tables in our DB
# Where as , schemas.py contains all the Classes which will be used as a model , which is Request , Response , Schema Tables
# If we want to send a custom request or Response , then we will define that class in Schemas.py
# the schemas.py will also contain the schema tables.


# Checking null checks in python can be done in 2 ways : 
#   if item is None
#   if not item
# both contribute to if(item == null)
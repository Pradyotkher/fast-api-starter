# Create a  virtual Environment first after making the directory of your project.

# Command to creatre a virtual environment in python 
python -m venv {env_name}

.\{env_name}\Scripts\activate Activates the Virtual environment
pip install "fastapi[standard]"

# Add the requirements.txt file to your  project
pip freeze > requirements.txt

pip install -m requirements.txt
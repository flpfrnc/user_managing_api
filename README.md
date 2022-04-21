## user_managing_api
### Project of an API to manage an user CRUD, including testing practices
<hr>

```bash
# Properly clone the repository
$ git clone https://github.com/flpfrnc/user_managing_api.git

# Install the virtual environment
$ pip install virtualenv

# Access the project folder
$ cd user_managing_api

# Instantiate the virtual environment
$ virtualenv env

# Activate the environment
$ . env/bin/activate

# Instal all dependencies
$ pip install -r requirements.txt

# Start the server
$ python3 manage.py runserver
```

##### To be added: 
- Swagger docs.

##### Current endpoints: 
- check api status: http://127.0.0.1:8000/ or http://127.0.0.1:8000/api/
- list all users: http://127.0.0.1:8000/api/users/
- list each users: http://127.0.0.1:8000/api/users/<int:id>
- list all profiles: http://127.0.0.1:8000/api/profiles/
- list each profile: http://127.0.0.1:8000/api/profiles/<int:id>

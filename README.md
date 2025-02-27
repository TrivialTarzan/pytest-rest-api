<h1 align="center">REST API Testing with Python & PyTest</h1>

This repository is a collection of experiments with various free-to-use websites created to help people practice and have fun with API testing automation. 
The primary goal is to not let good old Pytest get rusty and to play around with different types of public APIs and automate the testing process using **Pytest** and **Python**
For the first time I have implemented GitHub Actions into my project to automate code quality checks.

- **PyTest** for writing and executing automated test scripts
- **Requests** for sending HTTP requests
- **PyYAML** for storing configuration data needed for testing, such as endpoints and payload information, to keep everything organized

- **Ruff** is installed during GitHub Actions workflow and used to check the code quality and static analysis

### Webistes used (so far)
- **Mocky** https://designer.mocky.io/
- **Contact List Web App** https://thinking-tester-contact-list.herokuapp.com/ with the API docs here -> https://documenter.getpostman.com/view/4012288/TzK2bEa8

### Config files
I have two YAML files that store important data for testing. One of them, protected.yaml, is excluded from the repository because it contains sensitive info.

If you want the tests to pass, you must first create a protected.yaml file in the config folder.
Here’s what you need to include:

```yaml
my_user:
    token: "your_token"
    first_name: "your_name"
    last_name: "your_surname"
    email: "your_email"
    password: "your_password"
    _id: "your ID"
```

## Setup (Windows)

##### If you don't have a venv, create one
```sh
python -m venv venv
```

##### Now activate it
```sh
venv\Scripts\activate
```

##### And install dependencies 
```sh
pip install -r requirements.txt
```


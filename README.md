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


## 🐳 Running the Project with Docker

This project is packaged with Docker to make it easy to run the tests, even if you don't have Python installed locally.

### Prerequisites

Make sure you have:

- **Docker Desktop** installed: [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)
- **Windows Subsystem for Linux (WSL 2)** installed and up-to-date (for Windows users).

To install or update WSL:

```bash
wsl --install
wsl --update
```

Building the Docker Image

Clone the repository and navigate to the project directory:

```bash
git clone <repository_url>
cd pytest-rest-api
```

Build the Docker image:

```bash
docker build -t pytest-rest-api .
```

Running the Tests Inside the Container

Once the image is built, you can run the tests with:

```bash
docker run --rm pytest-rest-api
```

This will:

- Start a container based on the image.
- Run all the Pytest tests inside the container.
- Print the test results to the terminal.
- Automatically remove the container after it finishes.

Optional - Running Tests with Logs Stored on Host

If you want to keep the test logs on your local machine (for easier access), you can mount a volume:

```bash
docker run --rm -v ${PWD}/test_log.log:/app/test_log.log pytest-rest-api
```

### Troubleshooting

If you encounter issues with Docker Desktop, especially on Windows, you may need to:

- Ensure Docker Desktop is running.
- Ensure WSL 2 is installed and up-to-date.
- Check if the correct WSL backend is enabled in Docker Desktop settings.
- Restart Docker Desktop if needed.

You can also try resetting Docker’s WSL environment with:

```bash
wsl --unregister docker-desktop
wsl --unregister docker-desktop-data
```

Then restart Docker Desktop to let it recreate these environments.

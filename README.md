This repo contains the solution in context to the exercise shared.

## Dependencies

The solution uses the following libraries:

- requests
- pytest

## Installation

Naviagte to root folder and find the `requirements.txt` file. It contains the freezed dependencies for the solution. Run the following command to install the dependencies:

```
pip3 install -r requirements.txt
```

Alternatively, if you are using `virtualenv` then create a virtual environment using the following command:

```
python3 -m venv <env_name>
```

Then activate the environment using the following command:

```
source <env_name>/bin/activate
```

After that, run the following command to restore the dependencies in the selected environment:

```
pip3 install - requirements.txt
```

Once the prupose is achieved, exit the environment using `deactivate` command.

## Running the program

The program can be executed from the command line using the following:

```
python3 app.py
```

The tests can be run using the following:

```
python3 ./src/__tests__/ -v
```

NOTE: `-v` in the above command is optional. If you want you can skip it.

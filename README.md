todoist-cli
===

This is simple command line tool for Todoist.

# Feature

- add a task

# Usage

## Preparing

0. get token

    Access to [Todoist App Management Console](https://developer.todoist.com/appconsole.html) and create a new Todoist App. A test token will be generate with new app, so use it.
  
1. create `config.ini` file

    ```
    $ cp config.ini.sample config.ini
    ```
    
    and replace `your_todoist_token` in `config.ini` to your Todoist App access token. (test token)

2. install Python modules

    This tool work on Python `3.x`.

    ```
    $ python3 -m venv .venv && source ./.venv/bin/activate
    ```
    
    Install modules.
    
    ```
    $ pip install -r requirements.txt
    ```

## Use CLI

### add a task

```
$ python src/add-task.py -h
usage: add-task.py [-h] [-p PROJECT_ID] task_name

positional arguments:
  task_name             task name for new task

optional arguments:
  -h, --help            show this help message and exit
  -p PROJECT_ID, --project_id PROJECT_ID
                        project ID for new task added
```

- `task_name` is required for task name
- `-p` or `--project_id` is optional parameter for project ID
import os

project_slug = '{{ cookiecutter.project_slug }}'
MSG_COLOR = '\033[1;32m'
RESET_ALL = '\033[0m'

print(f"{MSG_COLOR}\n\nCREATING the project {project_slug} at {os.getcwd()}{RESET_ALL}")

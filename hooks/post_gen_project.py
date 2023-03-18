import subprocess


BLUE_COLOR = '\x1b[34m'
GREEN_COLOR = '\033[1;32m'
RESET_ALL = '\x1b[0m'


def run_command(command: str, idx=1) -> None:
    print(f"{BLUE_COLOR}{idx}. Running command: {command}{RESET_ALL}")
    subprocess.run(command, shell=True, check=True)


def main() -> None:
    comands = [
        "git init",
        "git add .",
        "git commit -m 'Initial commit'",
        "conda env create -f environment.yml",
    ]
    for idx, command in enumerate(comands, start=1):
        run_command(command, idx)

    msg = f"""{GREEN_COLOR}
    Your project is ready to go!
    To activate the environment run:
    $ cd {{ cookiecutter.project_slug }}
    $ conda activate {{ cookiecutter.project_slug }}-env \n\n
    {RESET_ALL}
    """
    print(msg)


if __name__ == "__main__":
    main()

# Cheat-sheet of various tech

git:
- switching branch on remote server:
  1. `git fetch`
  2. `git branch -v -a`
  3. `git switch BRANCH_NAME` without remote and origin
- `git checkout BRANCH_NAME` to switch branch on local
- install package from git
  - `git submodule -b BRANCH_NAME add https://github.com/username/repo.git path/to/submodule` this is how to add submodule and use specific branch
  - `git submodule update --init --recursive` to Initialize and fetch the contents of the submodule
- `git show HEAD` to show current HEAD status

vcpkg:
- `vcpkg new --application` to initialize
- `vcpkg add port PACKAGE_NAME` to add package

golang:
- `go build -o mydll.dll -buildmode=c-shared main.go` to build main.go file as shared library

elixir:
- `iex.bat --werl -S mix phx.server` starting phoenix server with erlang prompt
- `mix ecto.rollback --step 2` to rollback using ecto 
- `mix ecto.migrate --step 2` to migrate using ecto
- `mix run priv/repo/seeds.exs` to run seeder
- restarting genserver:
  1. `pid = Process.whereis(ATOM)`
  2. `res = Process.exit(pid, :shutdown)`

python:
- initializing python project
  1. use Anaconda to generate Python env
  2. `python -m venv venv` to create virtual env
  3. `source venv/bin/activate` or WIN `venv/Scripts/activate` to activate venv
  4. `pip install poetry` install poetry to handle dependencies
- `pip freeze > requirements.txt` to export dependencies list, better use poetry, or manually make your own requirements.txt
- `pip install -r /path/to/requirements.txt` to install dependencies

django:
- `python manage.py migrate APP_NAME TARGET` can be used to migrate (/ rollback with using previous TARGET version)
- `python manage.py makemigrations` run after make model in models.py to generate migrations

conda:
- `conda list -e > requirements.txt` to create requirements.txt from conda

node:
- `npm install git+https://github.com/USERNAME/REPO_NAME.git#HASH` install from git

SSH:
- public key: a key text that is needed to be put on remote server
- private key: a key text that is on local machine, and ONLY you should have it, to authenticate to server.
- use `ed25519` encryption as it's the latest tech

bash:
- `less /etc/passwd` to list user
- `groups` to list group
- `chmod -R 777 <file or directory>`
  - R is recursive
  - Read (4), Write (2), and Execute (1) permissions to the owner.
  - Read (4), Write (2), and Execute (1) permissions to the group.
  - Read (4), Write (2), and Execute (1) permissions to everyone else.
- `id USERNAME` check user

Unity:
- always use Power of Two textures

C#:
- `virtual` a method that can be overridden
- `abstract` a method that SHOULD be overridden

docker:
- `docker exec -it <container_name_or_id> /bin/bash` to go inside the container

apache:
- `var/log/apache/` directory for apache log: `access.log`, `error.log`
- django error will show on that file

github:
- `.github/workflows/FILE_NAME.yml` this is the location of workflow if you want to use github workflow

gcloud:
- Google Cloud Run use docker container, that means it supports older runtime such as Python 2.7
- Cloud Run default port is 8080
- Service account need permission: Cloud Run Admin, Artifact Registry Writer, Viewer, 

bitnami:
- Give SSH access to another person, such as a customer:
  - generate new SSH key pair, use puttygen (Windows) or ssh-keygen (Linux / macOS)
  - login as bitnami user
  - `sudo useradd -s /bin/bash -o -u `id -u` -g `id -g` USERNAME` this is alias for bitnami account
  - configure SSH access:
    ```
    sudo mkdir ~USERNAME/
    sudo cp -rp ~bitnami/.ssh ~USERNAME/
    sudo cp -rp ~bitnami/.bashrc ~USERNAME/
    sudo cp -rp ~bitnami/.profile ~USERNAME/
    ```
  - `cat USERNAME.pub >> /home/USERNAME/.ssh/authorized_keys` add public key to authorized_keys
  - `sudo usermod -aG bitnami-admins USERNAME` allow execute command as root
  - `sudo userdel USERNAME -f` to delete user


# Cheat-sheet of various tech

git:
- switching branch on remote server:
  1. `git fetch`
  2. `git branch -v -a`
  3. `git switch BRANCH_NAME` without remote and origin
- `git checkout BRANCH_NAME` to switch branch on local
- install package from git
  - `git submodule add -b BRANCH_NAME https://github.com/username/repo.git path/to/submodule` this is how to add submodule and use specific branch
  - `git submodule update --init --recursive` to Initialize and fetch the contents of the submodule
- `git show HEAD` to show current HEAD status

vcpkg:
- `vcpkg new --application` to initialize
- `vcpkg add port PACKAGE_NAME` to add package

golang:
- `go mod init github.com/USERNAME/MODULE_NAME` to initialize golang project
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
- `npm list -g --depth=0` list installed global packages

SSH:
- public key: a key text that is needed to be put on remote server
- private key: a key text that is on local machine, and ONLY you should have it, to authenticate to server.
- use `ed25519` encryption as it's the latest tech
- `ssh-keygen -t ed25519 -f FILE_NAME -C "your_email@example.com"` command to generate ssh pair key

bash:
- `top` to see CPU and RAM usage
- `mpstat` to see brief CPU usage
- `free -h` to see RAM usage
- `df -h` to see free disk space
- `ss -tuln` to see used port
- `lsof -i -P -n`
  - -i: Show network files.
  - -P: Display ports numerically (avoids service name resolution).
  - -n: Display IP addresses numerically (avoids DNS lookups).
- `nc -zv 127.0.0.1 PORT_NUMBER` check specific port number
- `fuser -n tcp PORT_NUMBER` check process using specific port
- `less /etc/passwd` to list user
- `groups` to list group
- `chmod -R 777 <file or directory>`
  - R is recursive
  - Read (4), Write (2), and Execute (1) permissions to the owner.
  - Read (4), Write (2), and Execute (1) permissions to the group.
  - Read (4), Write (2), and Execute (1) permissions to everyone else.
- `id USERNAME` check user
- `ls -la -R` list all files and directories, with detailed info (permission etc), include hidden files, recursive
- `tree -a -L 2 -h` show directory contents, with hidden files, 2 level deep, with file sizes
- copy
  - `cp source_file target_directory/` basic
  - `cp source_file target_directory/new_filename` rename
  - `cp file1 file2 file3 target_directory/` multiple file
  - `cp -r source_directory target_directory/` recursive
  - `cp -a source_file target_directory/` preserve attribute
  - `cp prefix_*.txt target_directory/` using wildcard
- move
  - basic, rename, multiple same as copy
  - `mv source_directory new_directory_name` move or rename directory
- remote copy
  - `scp username@source_host:/path/to/source_file target_directory/` copy source from remote host to local
  - `scp source_file username@target_host:/path/to/target_directory/` copy local file to remote

cmd:
- `dir /a /s` list all files and directories, include hidden files, recursive
- `tree /f` show all files

Unity:
- always use Power of Two textures

C#:
- `virtual` a method that can be overridden
- `abstract` a method that SHOULD be overridden

docker:
- `docker images` list docker images
- `docker system prune` 
- `docker stats --no-stream --format "table {{.Name}}\t{{.MemUsage}}"` check docker RAM usage
- `docker stats --no-stream --format "table {{.Name}}\t{{.CPUPerc}}"` check docker CPU usage
- `docker exec -it <container_name_or_id> /bin/bash` to go inside the container

apache:
- `var/log/apache/` directory for apache log: `access.log`, `error.log`
- django error will show on that file
- default user of apache in ubuntu is `www-data` and other usually `nobody` or `apache`, this is important to note because if you use Docker container with Dockerfile using mkdir, the default user of that directory will be `root`, that's why you need to either change the permission on the directory, or change the user

nginx:
- `/etc/nginx/sites-available` path to nginx site configuration
- `/var/run/php/phpX.X-fpm.sock` path to php-fpm socket, put into nginx config
- `sudo nginx -t` test config file
- `sudo tail -f /var/log/nginx/error.log` check error log of nginx
- `sudo ln -s /etc/nginx/sites-available/example.com /etc/nginx/sites-enabled/` link sites enabled to sites available so nginx will recognize it
- nginx must be able to see the directory to be able to serve it, so move it to `/var/www/html` and chmod and chown
- `sudo chown -R www-data:www-data DIRECTORY_NAME` change owner of directory
- `sudo chmod -R 755 DIRECTORY_NAME` change permission of directory

github:
- `.github/workflows/FILE_NAME.yml` this is the location of workflow if you want to use github workflow
- to clone github projects using ssh, first you need to create SSH pair, and put the public key to github. Then put your private key in .ssh/id_ed25519, it will automatically be picked by github to use as private key to authenticate SSH

gcloud:
- Google Cloud Run use docker container, that means it supports older runtime such as Python 2.7
- Cloud Run default port is 8080, it's automatically setup in cloud run, so we should remove the environment variables for PORT
- Service account need permission: Cloud Run Admin, Artifact Registry Writer, Viewer, Storage Admin, Service Account User

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
- Start or Stop Service
  - `sudo /opt/bitnami/ctlscript.sh status` get service status
  - `sudo /opt/bitnami/ctlscript.sh start` start all service
  - `sudo /opt/bitnami/ctlscript.sh restart service name` restart service
  - `sudo /opt/bitnami/ctlscript.sh stop` stop all service
  - `sudo /opt/bitnami/ctlscript.sh restart` restart all service

chrome:
- `chrome://inspect/#devices` link to open device inspector in browser

flask:
- `flask --app main run --debug` command to run flask app

PHP:
- `php -m` check enabled extensions

laravel:
- `php artisan make:migration create_users_table` to generate migration
- `php artisan migrate:rollback --step=1` to rollback with step
- `php artisan config:cache` deployment, cache the config
- `php artisan route:cache` deployment, cache the route
- `php artisan view:cache` deployment, cache the view

redis:
- `EXPIRE key seconds` to set expiration of keys
- `GET SET TYPE TTL DEL` simple operations
- `redis-cli -h ADDRESS -p PORT`

SQL:
- example LEFT JOIN query
```
SELECT column_name(s)
FROM table1
LEFT JOIN table2
ON table1.column_name = table2.column_name;
WHERE table1.id = table2.id
ORDER BY table.field ASC/DESC
LIMIT limit
```

Windows:
- `alt-space Move` restore windows off screen

Ubuntu / WSL:
- `wsl --list --verbose` check installed, status, and version of wsl in windows
- `sudo apt update` to update the local packages list
- `sudo apt upgrade` to upgrade the local packages (major version only)
- `sudo apt autoremove` removes unused orphaned packages. use `--dry-run` to check first
- `sudo apt clean` removes old cached files. use `--dry-run` to check first
- `cat /etc/os-release` check what distro of linux
- `cd /mnt/c` access drive c
- `apt-cache policy PACKAGE_NAME` to check whether package exist or not in package manager
- `sudo systemctl status SERVICE_NAME` to check status of the service
- `sudo systemctl start SERVICE_NAME` to start service
- `sudo systemctl enable SERVICE_NAME` to start automatically on boot
- `ps aux | grep SERVICE_NAME`

Ansible:
- `ansible -i inventory.ini YOUR_SERVER_GROUPS -m ping` ping to troubleshoot connection
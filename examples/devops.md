## Add user to a group

- `sudo groupadd groupname` make a group
- `sudo usermod -a -G groupname username` -a = append, -G groupname
- `sudo chown -R username:groupname /opt/dirname`

## Make shared optional software directory

- `sudo mkdir -p /opt/dirname`
- `sudo chown username:groupname /opt/dirname`
- `sudo chmod 775 /opt/dirname`

## Make Redis has public access

- `sudo nano /etc/redis/redis.conf`
- change `bind 127.0.0.1 ::1` to `bind 0.0.0.0`
- change `protected-mode yes` to no
- open firewall for port 6379
- `sudo systemctl restart redis`

## Make Bitnami Mariadb has public access

- `sudo nano /opt/bitnami/mariadb/conf/my.cnf`
- change `bind-address = 127.0.0.1` to `bind-address = 0.0.0.0`

## Deploy to Google Cloud Run using Github Action

- create a new service account to be used by Github Action, also the key
- attach permissions: `Artifact Registry Writer`, `Cloud Run Admin`, `Service Account User`, `Storage Admin`, `Viewer`
- create a new Repository in Artifact Registry
- fill secrets and vars in Github action

## Create Google Application Load Balancer

- prepare Origin Certificate to use from Cloudflare, don't forgot to store the origin cert PK in local
- create Https Frontend, Ephemeral IP, attach cert
- create NEG, attach to cloud run, disable CDN
- set A record from Cloudflare to ALB
- set Cloudflare SSL to Full
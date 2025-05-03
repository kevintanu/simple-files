## Add user to a group

- `sudo groupadd groupname` make a group
- `sudo usermod -a -G groupname username` -a = append, -G groupname
- `sudo chown -R username:groupname /opt/dirname`

## Make shared optional software directory

- `sudo mkdir -p /opt/dirname`
- `sudo chown username:groupname /opt/dirname`
- `sudo chmod 775 /opt/dirname`

## Make Redis has public access

- go to `/etc/redis/redis.conf` as a root
- change `bind 127.0.0.1 ::1` to `bind 0.0.0.0`
- change `protected-mode yes` to no
- open firewall for port 6379
- `sudo systemctl restart redis`

## Deploy to Google Cloud Run using Github Action

- create a new service account to be used by Github Action, also the key
- attach permissions: `Artifact Registry Writer`, `Cloud Run Admin`, `Service Account User`, `Storage Admin`, `Viewer`
- create a new Repository in Artifact Registry
- fill secrets and vars in Github action
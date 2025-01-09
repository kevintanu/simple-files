# Simple Notes

- PHP, Python, Ruby, Java are all blocking, scripting programming language
- By default, nodejs and golang are non-blocking
- prefer golang / elixir for webserver
- use `Redis Sorted Set` for game leaderboard, it's fast
- always think of Operating System
- try to fit your app on HTML5, which is included in all superapps

# Webserver
- Health check
- Add server git commit check
- Always make admin token bypass to test
- Make a cron to periodically update static data from server / auto patcher
- Make a checksum or CSRF to prevent hitting api not from your app
- make CI CD
- Static data system
- make a job scheduler system, which only run ON user input
- insert logging system
- insert monitoring system such as grafana (probably also handle logging)
- add rate limit / request lock, try using Redis SETNX
- add impersonate system
- Add API versioning
- Add timer check on API call
- Add SQL query monitoring
- Add API doc & README
- Register & Login
- Add Dashboard
  - Add reset data
  - Maintenance mode
- Return standard: add status and data/message

# SSL
- put your domain on Cloudflare to get free SSL certificate (gain lock icon on browser), and free DDOS protection
- use Let's encrypt set your server reverse proxy. This will make sure user doesn't see that we are using Let's encrypt cert, also create secure connection between cloudflare and your server
- try to get Full Strict. means you get prevention on MITM attack, can't be eavesdropped. You need to manage let's encrypt or get Certificate from Cloudflare by yourself (technically Cloudflare itself can decrypt it).

# Game
- Health check
- Add server git commit check
- Maintenance mode
- Make a checksum or CSRF to prevent hitting api not from your app
- make CI CD
- Static data system
- Send error log
- Analytics
- Daily Login Bonus
- Gacha
- Disable Multiple Login
- Register & Login

# Recommended Tools:
- Imgui - desktop apps
- Flutter - mobile apps

# Abbreviations:
- CIDR: Classless Inter-Domain Routing
- CRTP: Curiously Recurring Template Pattern

# Crypto:
- btc -> altCoin, boomerCoin -> memeCoin/shitCoin -> btc
- fdv: Fully Diluted Value, total worth or market cap of a cryptocurrency if the entire supply of tokens were in circulation.
- market cap: total worth of crypto, not including vested token
- always look at market cap, not coin value

# Website:
- if using google ads, try using google tag manager for tracking, google analytics conversion is buggy as hell

# Python:
- install pyenv for version management, Anaconda only for Jupyter, to avoid error on pyinstaller
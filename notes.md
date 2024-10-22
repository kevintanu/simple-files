# Simple Notes

- PHP, Python, Ruby, Java are all blocking, scripting programming language
- By default, nodejs and golang are non-blocking
- prefer golang / elixir for webserver
- use `Redis Sorted Set` for game leaderboard, it's fast
- always think of Operating System
- try to fit your app on HTML5, which is included in all superapps

# Webserver
- Always make a health check
- Always make a server git commit check
- Always make admin token bypass to test
- Make Maintenance mode
- Make a cron to periodically update static data from server / auto patcher
- Make a checksum or CSRF to prevent hitting api not from your app
- make CI CD
- make static data system
- make a job scheduler system, which only run ON user input
- insert logging system
- insert monitoring system such as grafana (probably also handle logging)

# Recommended Tools:
- Imgui - desktop apps
- Flutter - mobile apps

# Abbreviations:
- CIDR: Classless Inter-Domain Routing
- CRTP: Curiously Recurring Template Pattern
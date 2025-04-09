# Go Tooling

- 1 package = multiple source files in 1 directory
- 1 module = multiple packages, contains go.mod
- `go mod init github.com/username/projectname` create a module
- Project structure:
```
projectname/
│── cmd/
│   ├── main.go         # Entry point
│   ├── seeder.go       # Seeder script
│── internal/
│   ├── database/       # Database connection
│   ├── handlers/       # HTTP handlers
│   ├── models/         # Structs (not ORM)
│   ├── repository/     # Query builder logic
│   ├── routes/         # Router
│── migrations/         # SQL migration files
│── config/             # Configuration files
│── .env                # Environment variables
│── go.mod              # Go module file
│── go.sum              # Go dependencies
```
- `go install example/user/hello` or `go install .` to install the exe to `$HOME/go/bin/hello`, based on `GOPATH` or `GOBIN`. globally
- `go build` save the compiled package in local cache
- `go mod tidy` adds missing module requirements for imported packages and removes requirements on modules that aren't used anymore, similiar to `npm install`
- check `GOPATH` for downloaded `pkg/mod`
- `go clean -modcache` remove all downloaded modules
- `go test` run file ending with _test.go, `func TestReverseRunes(t *testing.T) {`
- `go help mod tidy` show help on action

## SQLC

- `https://docs.sqlc.dev/en/stable/tutorials/getting-started-postgresql.html`
- create `sqlc.yaml`
- create `schema.sql` and `query.sql`
- run `sqlc generate`

## Migrate

- `migrate create -ext sql -dir db/migrations -seq create_users_table` create migration`
- `migrate -database "postgres://postgres:postgres@host:5432/dbname?sslmode=disable&search_path=public" -path ./db/migrations up` up migration
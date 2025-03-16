# Ecto

## Start

- `mix new friends --sup` ensure app has supervision tree
```
defp deps do
  [
    {:ecto_sql, "~> 3.0"},
    {:postgrex, ">= 0.0.0"}
  ]
end
```
- `mix ecto.gen.repo -r Friends.Repo`
- ensure Ecto started in App Supervision Tree
- `config :friends, ecto_repos: [Friends.Repo]`
- `mix ecto.create` to create db
- `mix ecto.gen.migration create_people`
- `mix ecto.migrate`
```
defmodule Friends.Person do
  use Ecto.Schema

  schema "people" do
    field :first_name, :string
    field :last_name, :string
    field :age, :integer
  end
end
```
- `Friends.Repo.insert(person)` insert data
- `mix ecto.drop` to drop db
- `Friends.Person |> Ecto.Query.first |> Friends.Repo.one` fetch first
- `Friends.Person |> Friends.Repo.all` fetch all
- `Friends.Person |> Friends.Repo.get(1)` fetch based on id
- `Friends.Person |> Friends.Repo.get_by(first_name: "Ryan")` fetch one based on attr
- `Friends.Person |> Ecto.Query.where(last_name: "Smith") |> Friends.Repo.all` filter
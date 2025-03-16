# Elixir Learn

## Language

### Intro
- `elixir --version` or `elixir -v`
- `iex` or powershell `iex.bat --werl`
- `IO.puts("hello")` print

### Basic Types
- int, float, bool, atom/symbol, str, list, tuple
- `div`, `rem`, `round`, `trunc`
- `is_integer`, `is_float`, `is_number`, `is_atom`, `is_boolean`, `byte_size`
- `1.0e-10`
- `true or raise("This error will never be raised")` short circuit
- `nil`, `false` falsy
- `"hello #{value}!"` string interpolation

### list and tuples
- `length`, `hd`, `tl`
- `[1, 2, 3] ++ [4, 5, 6]` and `[1, true, 2, false, 3, true] -- [true, false]` concat and substract
- `tuple_size`, `put_elem(tuple, 1, "world")`
- list is vary, tuple is not

### pattern match
- `x = 1`, `1 = x` match op
- `{:ok, result} = {:ok, 13}` match on specific value
- `[head | tail] = [1, 2, 3]` match list
- `[0 | list]` can also for prepend
- `x = 1`, `^x = 2` pin op, don't rebound
- `[head | _] = [1, 2, 3]` don't care for value

### case cond if
```
case {1, 2, 3} do
  {4, 5, 6} ->
    "This clause won't match"
  {1, x, 3} ->
    "This clause will match and bind x to 2 in this clause"
  _ ->
    "This clause would match any value"
```
- `{1, x, 3} when x > 0 ->` guard
```
cond do
  2 + 2 == 5 ->
    "This will not be true"
  2 * 2 == 3 ->
    "Nor this"
  1 + 1 == 2 ->
    "But this will"
  true ->
    "This is always true (equivalent to else)"
end
```

### anon fn
- `h Kernel.trunc/1` means trunc takes 1 arg
- `add = fn a, b -> a + b end`
- `add.(1, 2)` invoke anon fn
- `is_function`
- `double = fn a -> add.(a, a) end` closure
- pattern match:
```
f = fn
  x, y when x > 0 -> x + y
  x, y -> x * y
end
```
- `is_arity_2 = &is_function(&1, 2)` capture op, `&1` means the first arg

### binary, string, charlist
- `?a` code point of a
- `"hełło" <> <<0>>` check bytes of str
- `"hello" <> " world"` concat str, or binary, will result in copy because immutability
- `~c"hello"` charlist
- `inspect` check var

### keyword list and map
- `String.split("1  2  3  4", " ", [parts: 3, trim: true])` keyword list example
- `String.split("1  2  3  4", " ", parts: 3, trim: true)` can skip bracket if at the last argument
- `[{:parts, 3}, {:trim, true}] == [parts: 3, trim: true]` keyword list = list with 2 item tuple
- `map = %{:a => 1, 2 => :b}` map = key value pair
- `Map.get(%{:a => 1, 2 => :b}, :a)`
- `Map.put(%{:a => 1, 2 => :b}, :c, 3)`
- `Map.to_list(%{:a => 1, 2 => :b})`
- `map = %{name: "John", age: 23}` can be key:value syntax
- `map.name` can access using map.key syntax
- `%{map | name: "Mary"}` can update key like this
- `users = put_in(users[:john].age, 31)`

### Module, Function
- `defmodule Math do ... end`
- `elixirc math.ex` compile
- `elixir math.exs` run script
- `defp` private func
- `def zero?(x) when is_integer(x) do` guard on fn declaration, also when recursion
- `def join(a, b, sep \\ " ") do` default arg

### Enumerable and Stream
- `Enum.map([1, 2, 3], fn x -> x * 2 end)`
- `Enum.map(%{1 => 2, 3 => 4}, fn {k, v} -> k * v end)`
- `1..3` range
- `|>` pipe op
- `1..100_000 |> Stream.map(&(&1 * 3)) |> Stream.filter(odd?) |> Enum.sum()` stream is lazy
- `"path/to/file" |> File.stream!() |> Enum.take(10)` fetch first 10 lines of the file

### Process
- `pid = spawn(fn -> send(parent, {:hello, self()}) end)`
- `Process.alive?(pid)`
- `self()` get PID current process
- `send(self(), {:hello, "world"})`
```
receive do
  {:hello, msg} -> msg
  {:world, _msg} -> "won't match"
after
  1_000 -> "nothing after 1s" // timeout
end
```
- `flush` print all msg in mailbox
- `spawn_link(fn -> raise "oops" end)` linked process
- `Task.start(fn -> raise "oops" end)` or `Task.start_link` process abstraction, got better error report
- `Process.register(pid, :kv)` register pid, give name
- `{:ok, pid} = Agent.start_link(fn -> %{} end)` abstraction of state

### alias, require, import, use

- Alias the module so it can be called as Bar instead of Foo.Bar

`alias Foo.Bar, as: Bar`, same as alias `Foo.Bar` `alias MyApp.{Foo, Bar, Baz}`
- Require the module in order to use its macros

`require Integer` , `Integer.is_odd(3)`
- Import functions from Foo so they can be called without the `Foo.` prefix. Prefer alias over import

`import List, only: [duplicate: 2]`
- Inject function to current module, Invokes the custom code defined in Foo as an extension point

`use Foo`

### Module attribute

- `@moduledoc`, `@doc` provide doc for module and function, will be shown on `h`
- `@service URI.parse("https://example.com")` define attribute in compile time. support any elixir type such as map, increase compile time
- `@hours_in_a_day 24` but better use fn: `defp hours_in_a_day(), do: 24`

### Struct

- `defmodule User do` `defstruct name: "John", age: 27` map that have compile-time check and default value

### Protocol
```
defprotocol Utility do
  @spec type(t) :: String.t()
  def type(value)
end

defimpl Utility, for: BitString do
  def type(_value), do: "string"
end

defimpl Utility, for: Integer do
  def type(_value), do: "integer"
end
```

### Comprehension
- `for n <- 0..5, rem(n, 3) == 0, do: n * n`

### try, catch, and rescue
- `raise ArgumentError, message: "invalid argument foo"`
- `try do ... rescue ... end`
- `try do ... catch ... end` rearely used

### Erlang Lib

```
table = :ets.new(:ets_test, [])
# Store as tuples with {name, population}
:ets.insert(table, {"China", 1_374_000_000})
:ets.insert(table, {"India", 1_284_000_000})
:ets.insert(table, {"USA", 322_000_000})
:ets.i(table)
```

### Debugging

- `IO.inspect` and `dbg`, use `iex.bat --werl --dbg pry -S mix`
- for `iex`, `:observer.start()` Start an Observer App
- for `iex -S mix`:
```
Mix.ensure_application!(:wx)
Mix.ensure_application!(:runtime_tools)
Mix.ensure_application!(:observer)
```

## MIX & OTP

### Intro
- mix a build tool
- `mix new kv --module KV` make project, with path kv, and module name KV
- `mix compile`, `recompile()`, `mix test`, `mix format`, `mix help`
- `iex -S mix` to start iex and load project modules

### Client Server
- `Process.monitor(pid)`
- `Agent.stop(pid)`
- `handle_call/3, handle_cast/2 and handle_info/2` Genserver callbacks

### Supervisor
```
defmodule KV.Supervisor do
  use Supervisor

  def start_link(opts) do
    Supervisor.start_link(__MODULE__, :ok, opts)
  end

  @impl true
  def init(:ok) do
    children = [
      KV.Registry
    ]

    Supervisor.init(children, strategy: :one_for_one)
  end
end
```
Start in App
```
  def application do
    [
      extra_applications: [:logger],
      mod: {KV, []}
    ]
  end
```
```
defmodule KV do
  use Application

  @impl true
  def start(_type, _args) do
    # Although we don't use the supervisor name below directly,
    # it can be useful when debugging or introspecting the system.
    KV.Supervisor.start_link(name: KV.Supervisor)
  end
end
```

### Dynamic Supervisor
```
  def init(:ok) do
    children = [
      {KV.Registry, name: KV.Registry},
      {DynamicSupervisor, name: KV.BucketSupervisor, strategy: :one_for_one}
    ]

    Supervisor.init(children, strategy: :one_for_one)
  end
```

### Dependencies
```
def deps do
  [{:plug, "~> 1.0"}]
  [{:plug, git: "https://github.com/elixir-lang/plug.git"}]
end
```
- `mix deps.get` and `mix deps.update`
# Elixir

## Install

- `mix archive.install hex phx_new` install phoenix
- `mix phx.new hello` `--no-ecto` `--no-html` `--no-assets` `--no-live`
- `iex.bat --werl --dbg pry -S mix phx.server`

## Directory Structures

- `assets` frontend, js, css. auto bundled by esbuild
- `config` config for all env
- `lib/hello` (model) and `lib/hello_web` (view and controller)
- `priv` db scripts, translation files, images. `priv/static` for generated assets
- `test` tests files, mirrors lib

## Request life-cycle

- New View
```
defmodule HelloWeb.HelloHTML do
  use HelloWeb, :html
  embed_templates "hello_html/*" # embed all .heex templates found in hello_html
end
```

- endpoint -> router -> controller -> view


## Plug

- conn `%Plug.Conn{}`
- can be function plug or module plug (init/1 & call/2)
- controller is also a plug
- `plug HelloWeb.Plugs.Locale, "en" when action in [:index]`
- good read on composition `https://hexdocs.pm/phoenix/plug.html#plugs-as-composition`

## Routing

- `mix phx.routes`
- `get "/", PageController, :home`
- `resources "/posts", PostController, only: [:index, :show]` also can use `except`. can be nested
- `~p"/unknown/123"` Verified routes, to catch bug on compile time
- `scope "/admin", HelloWeb.Admin do` scoped routes
- `pipeline :browser do` `pipe_through :browser` `pipe_through [:browser, :auth]` pipelines is a series of plug

## Controllers

- can use `text/2`, `json/2` and `render/2` to render content
- `assign(:messenger, messenger)` assign to pass value to template
- `render(conn, :show, messenger: messenger, receiver: "Dweezil")` or directly to render
- `put_resp_content_type("text/plain")` `send_resp(conn, 201, "")` send response directly
- `put_status(202)`
- `redirect(conn, to: ~p"/redirect_test")`
- `redirect(conn, external: "https://elixir-lang.org/")`
- `render(conn, :home, layout: false)`
- `put_flash(:error, "Let's pretend we have an error.")` `<.flash_group flash={@flash} />` use flash + redirect to redirect with extra information

## Components and HEEx

- Function components
```
  attr :messenger, :string, required: true

  def greet(assigns) do
    ~H"""
    <h2>Hello World, from {@messenger}!</h2>
    """
  end
```
- `<div title="My div" class={@class}>` auto handle false to remove attr
- `<div title="My div" {@many_attributes}>` dynamic number of attr in keyword list or map
- `{@inner_content}`
- `put_root_layout(html: false)` & `put_layout(html: :admin)` switch layouts and disable layout

## Ecto
- `mix phx.gen.schema User users name:string email:string `
```
def changeset(user, attrs) do
  user
  |> cast(attrs, [:name, :email, :bio, :number_of_pets])
  |> validate_required([:name, :email, :bio, :number_of_pets])
  |> validate_length(:bio, min: 2)
  |> validate_length(:bio, max: 140)
  |> validate_format(:email, ~r/@/)

...

  |> validate_required([:price_when_carted, :quantity])
  |> validate_number(:quantity, greater_than_or_equal_to: 0, less_than: 100)
end
```

## Contexts

- `mix phx.gen.html` also `json`, `live` and `context`
- if stuck, use plural form, e.g. `Products` context
- `mix phx.gen.html Catalog Product products title:string \`
- Catalog module serve as plubic API
- Catalog.Product , Ecto schema for casting and validating
- `add :price, :decimal, precision: 15, scale: 6, null: false`
- Atomic update
```
  def inc_page_views(%Product{} = product) do
    {1, [%Product{views: views}]} =
      from(p in Product, where: p.id == ^product.id, select: [:views])
      |> Repo.update_all(inc: [views: 1])

    put_in(product.views, views)
  end
```
- `mix ecto.gen.migration create_product_categories` reference:
```
  def change do
    create table(:product_categories, primary_key: false) do
      add :product_id, references(:products, on_delete: :delete_all)
      add :category_id, references(:categories, on_delete: :delete_all)
    end

    create index(:product_categories, [:product_id])
    create unique_index(:product_categories, [:category_id, :product_id])
  end
```
- `mix run priv/repo/seeds.exs`
- `belongs_to :cart, Hello.ShoppingCart.Cart` `many_to_many :categories, Category, join_through: "product_categories", on_replace: :delete` in schema, add relation
- more on relation read: `https://hexdocs.pm/phoenix/contexts.html#in-context-relationships`
- `on_conflict and conflict_target`
- `def currency_to_str(%Decimal{} = val), do: "$#{Decimal.round(val, 2)}"` function in html
- form
```
<div :if={@cart.items !== []}>
  <.simple_form :let={f} for={@changeset} action={~p"/cart"}>
    <.inputs_for :let={%{data: item} = item_form} field={f[:items]}>
      <.input field={item_form[:quantity]} type="number" label={item.product.title} />
      {currency_to_str(ShoppingCart.total_item_price(item))}
    </.inputs_for>
    <:actions>
      <.button>Update cart</.button>
    </:actions>
  </.simple_form>
  <b>Total</b>: {currency_to_str(ShoppingCart.total_cart_price(@cart))}
</div>
```
- `Ecto.Changeset.cast_assoc/3` to cast the nested item data into CartItem changesets
```
 def update_cart(%Cart{} = cart, attrs) do
    changeset =
      cart
      |> Cart.changeset(attrs)
      |> Ecto.Changeset.cast_assoc(:items, with: &CartItem.changeset/2)

    Ecto.Multi.new()
    |> Ecto.Multi.update(:cart, changeset)
    |> Ecto.Multi.delete_all(:discarded_items, fn %{cart: cart} ->
      from(i in CartItem, where: i.cart_id == ^cart.id and i.quantity == 0)
    end)
    |> Repo.transaction()
    |> case do
      {:ok, %{cart: cart}} -> {:ok, cart}
      {:error, :cart, changeset, _changes_so_far} -> {:error, changeset}
    end
  end
```

## JSON and API
- `https://hexdocs.pm/elixir/Kernel.SpecialForms.html#with/1` use with to simplify case, combining match
```
defmodule HelloWeb.MyController do
  use Phoenix.Controller

  def show(conn, %{"id" => id}, current_user) do
    with {:ok, post} <- fetch_post(id),
         :ok <- authorize_user(current_user, :view, post) do
      render(conn, :show, post: post)
    else
      {:error, :not_found} ->
        conn
        |> put_status(:not_found)
        |> put_view(html: HelloWeb.ErrorHTML, json: HelloWeb.ErrorJSON)
        |> render(:"404")

      {:error, :unauthorized} ->
        conn
        |> put_status(403)
        |> put_view(html: HelloWeb.ErrorHTML, json: HelloWeb.ErrorJSON)
        |> render(:"403")
    end
  end
end
```
- `https://hexdocs.pm/phoenix/json_and_apis.html#action-fallback` use fallback to implement similiar logic `action_fallback HelloWeb.MyFallbackController` `lib/hello_web/controllers/fallback_controller.ex`

## Test

- `MIX_ENV=test mix ecto.reset`
- `$env:MIX_ENV="test"` `mix ecto.reset` in Windows PS
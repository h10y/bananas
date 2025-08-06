# Bananas Shiny App 

Shiny app for classifying ripening bananas based on their color.

Data set from <https://github.com/psolymos/bananas>.

![](example-bananas.png)

| Flavour           | Link  | Image  |
|-------------------|---|---|
| Python Shiny      | [`py-shiny`](./py-shiny/)  | [`ghcr.io/h10y/bananas/py-shiny`](https://github.com/h10y/bananas/pkgs/container/bananas%2Fpy-shiny)  |
| R Shiny           | [`r-shiny`](./r-shiny/)  | [`ghcr.io/h10y/bananas/r-shiny`](https://github.com/h10y/bananas/pkgs/container/bananas%2Fr-shiny)  |

Shinylive does not work - see the [`shinylive.md`](./shinylive.md) file for details.

# Deploy to shinyapps.io

R version:

```R
rsconnect::setAccountInfo(
    name = "h10y",
    token = "A1B2...Y8Z9",
    secret = "abc123...xyz789")

rsconnect::deployApp(
    appDir = "./r-shiny/app", 
    account = "h10y",
    appName = "bananas-r")
```

Python:

```bash
rsconnect add \
    --account h10y \
    --name h10y \
    --token A1B2...Y8Z9 \
    --secret abc123...xyz789

rsconnect deploy shiny ./py-shiny/app \
    --name h10y \
    --title bananas-py
```

Render HTML from markdown:

```bash
pandoc -s -f markdown -t html5 -o "docs/index.html" "index.md"
```

See deployed Shiny results at <https://h10y.github.io/bananas/>.

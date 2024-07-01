# Bananas Shiny App 

## For R

1. Install libraries with `R -q -e "install.packages('deps');deps::install()"` in the r folder
2. Run the app with `R -q -e "shiny::runApp(port=8080)"`

## For Python

1. Install libraries with `pip install -r requirements.txt` in the python folder
2. Run the app with `shiny run --reload --port 8080`

# Shinylive - DOES NOT WORK

Create Python shinylive version following <https://github.com/posit-dev/py-shinylive>:

```bash
cd shiny-apps/bananas
shinylive export python py-shinylive
python3 -m http.server --directory py-shinylive 8008
# ValueError: Can't find a pure Python 3 wheel for 'pandas==1.5.3'.
# See: https://pyodide.org/en/stable/usage/faq.html#micropip-can-t-find-a-pure-python-wheel
```

Create R shinylive version following <https://posit-dev.github.io/r-shinylive/>:

```bash
cd shiny-apps/bananas
R -q -e 'shinylive::export("r", "r-shinylive")'
R -q -e 'httpuv::runStaticServer("r-shinylive", port=8008)'
# Traceback (most recent call last):
#   File "<exec>", line 202, in _start_app
#   File "/lib/python3.10/importlib/__init__.py", line 126, in import_module
#     return _bootstrap._gcd_import(name[level:], package, level)
#   File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
#   File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
#   File "<frozen importlib._bootstrap>", line 1004, in _find_and_load_unlocked
# ModuleNotFoundError: No module named 'app_mslnoz8ax567q6haiit6.app'
```

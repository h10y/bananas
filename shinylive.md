# Shinylive - DOES NOT WORK

Create Python Shinylive version following <https://github.com/posit-dev/py-shinylive>:

```bash
shinylive export py-shiny/app py-shinylive

python3 -m http.server --directory py-shinylive 8080

# Traceback (most recent call last):
#   File "<exec>", line 369, in _start_app
#   File "<exec>", line 302, in _install_requirements_from_dir
#   File "/lib/python3.11/site-packages/micropip/_commands/install.py", line 142, in install
#     await transaction.gather_requirements(requirements)
#   File "/lib/python3.11/site-packages/micropip/transaction.py", line 204, in gather_requirements
#     await asyncio.gather(*requirement_promises)
#   File "/lib/python3.11/site-packages/micropip/transaction.py", line 211, in add_requirement
#     return await self.add_requirement_inner(Requirement(req))
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/lib/python3.11/site-packages/micropip/transaction.py", line 300, in add_requirement_inner
#     await self._add_requirement_from_package_index(req)
#   File "/lib/python3.11/site-packages/micropip/transaction.py", line 339, in _add_requirement_from_package_index
#     wheel = find_wheel(metadata, req)
#             ^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/lib/python3.11/site-packages/micropip/transaction.py", line 431, in find_wheel
#     raise ValueError(
# ValueError: Can't find a pure Python 3 wheel for 'scikit-learn==1.3.0'.
# See: https://pyodide.org/en/stable/usage/faq.html#why-can-t-micropip-find-a-pure-python-wheel-for-a-package
# You can use `await micropip.install(..., keep_going=True)` to get a list of all packages with missing wheels.
```

Create R Shinylive version following <https://github.com/posit-dev/r-shinylive/>:

```bash
R -q -e "shinylive::export('r-shiny/app', 'r-shinylive')"

R -q -e "httpuv::runStaticServer('r-shinylive', port=8080)"

# Robj construction for this JS object is not yet supported
```

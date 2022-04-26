#!/bin/bash -i

jupyter-book config sphinx .
sphinx-build  . _build/html -D html_baseurl=${JUPYTERHUB_SERVICE_PREFIX}/proxy/absolute/8000

jupyter-book build .

echo "Use the link below to view"

cd _build/html
python -m http.server
## VARIABLES 
AUDIO=$(wildcard audio/*.wav)
FIGURS=$(wildcard figurs/*.png)
DATA=$(wildcard data/*.csv)
BUILD=$(wildcard _build/*)
## ENVIRONMENT SETUP

.PHONY : env
env :
    bash -i envsetup.sh

.PHONY : env_update
env_update :
    mamba env update --file environment.yml --prune



# Build the JupyterBook locally
.PHONY : html
html :
    chmod a+x booksetup.sh
    bash -ic booksetup.sh



# Build JupyterBook with GitHub Pages
.PHONY : html-hub
html-hub :
    pip install ghp-import
    ghp-import -n -p -f _build/html


## CLEAN 

.PHONY : clean
clean:
    rm -f $(AUDIO)
    rm -f $(DATA)
    rm -f $(FIGURS)
    rm -f $(_build)


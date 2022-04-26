## VARIABLES 
AUDIO=$(wildcard audio/*.wav)
FIGURS=$(wildcard figurs/*.png)
DATA=$(wildcard data/*.csv)


html:
    jupyter-book build .

## CLEAN 

.PHONY : clean
clean:
    rm -f $(AUDIO)
    rm -f $(DATA)
    rm -f $(FIGURS)
    rm -f $(_build)


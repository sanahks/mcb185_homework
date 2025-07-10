gunzip -c ~/Code/MCB185/data/dictionary.gz | grep -E ".{4,}" | grep -E -i "r+" | grep -i "[oncaiz]*" | grep -v "[^roncaiz]"

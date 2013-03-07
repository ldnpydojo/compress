
# abc=5 foo=3 bar=2

compress_input = "foo bar xxx abc abc bar foo abc abc abc"
compress_output = "abc|foo|bar" \
                  "$1 $2 xxx $0 $0 $0 $2 $1 $0 $0 $0"





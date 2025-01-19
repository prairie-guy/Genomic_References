#!/usr/bin/env sh

# Used to edit the original fasta sequence to remove all regions except for regions 1..22, X, Y, MT

if [ $# -eq 0 ]; then
    echo "Usage: $0 <input_fasta_file>"
    exit 1
fi

awk '
BEGIN { ORS = ""; }
/^>/ {
    if (seq != "") {
        print header "\n" seq "\n";
    }
    header = $0;
    seq = "";
    if (header ~ /^>(1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|X|Y|MT) /) {
        print_flag = 1;
    } else {
        print_flag = 0;
    }
    next;
}
{
    if (print_flag) {
        seq = seq $0 "\n";
    }
}
END {
    if (print_flag && seq != "") {
        print header "\n" seq;
    }
}' "$1"

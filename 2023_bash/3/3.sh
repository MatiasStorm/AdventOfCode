# file="3-example.txt"
file="3.txt"

symbols="[*+#\\/\$%=@&-]"

parts=$(cat $file | grep --byte-offset --only-matching -E "[0-9]+" | tr '\n' ' ')
symbol_bytes=$( cat $file | grep --byte-offset --only-matching -E "$symbols"  | cut -d':' -f1 | sort )

line_lenght=$(( $(wc -L $file | cut -d' ' -f1) + 1)) # add 1 because newline is not counted by wc

parts_to_sum=""
for p in $parts
do
  part=(${p//:/ })

  part_offset=${part[0]}
  part_num=${part[1]}
  part_lenght=${#part_num}
  part_row=$(($part_offset / $line_lenght))

  beforeline=$( seq $(($part_offset - $line_lenght - 1)) $(($part_offset - $line_lenght + $part_lenght )))
  afterline=$( seq $(($part_offset + $line_lenght - 1)) $(($part_offset + $line_lenght + $part_lenght )))

  reg="$(($part_offset - 1))
$(($part_offset + $part_lenght ))
$beforeline
$afterline"

  if [[  $( comm -1 -2 <(echo "$reg" | sort) <(echo "$symbol_bytes") ) ]]; then ## str contains substr
    parts_to_sum="$parts_to_sum $part_num"
  fi
done
echo -n "Part 1: "
echo $parts_to_sum | tr ' ' '\n'  | paste -s -d+ | bc

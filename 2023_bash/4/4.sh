# file="4-example.txt"
file="4.txt"

data=$(sed -n "s/Card\s*[0-9]*:\s*//p" "$file")

s=0
while read line
do
  wn=$(echo "${line}" | xargs | tr ' ' '\n' | sort | uniq -d | wc -l)
  s=$(($s + (2 ** $wn) / 2 ))
done < <(echo -e "$data" )
echo $s

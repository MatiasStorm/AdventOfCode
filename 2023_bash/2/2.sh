# file="2_example.txt"
file="2.txt"

# part 1
red=$(cat $file | grep -E "1[3-9]{1}\sred|[2-9]{1}[0-9]{1}\sred")
green=$(cat $file | grep -E "1[4-9]{1}\sgreen|[2-9]{1}[0-9]{1}\sgreen")
blue=$(cat $file | grep -E "1[5-9]{1}\sblue|[2-9]{1}[0-9]{1}\sblue")

impossible_games=$( sort -u  <( echo "$red" ) <( echo "$green" ) <( echo "$blue") )
possible_games=$(comm -13 <(echo "$impossible_games") <(cat $file | sort))

echo -n "Part 1: "
echo "$possible_games" \
  | grep -E "Game\s[0-9]+" -o \
  | cut -d " " -f2 \
  | paste -s -d+ \
  | bc


s=0
while read line
do
  r=$( echo "$line" | grep -E "[0-9]+\sred" -o | cut -d " " -f1 | sort -n | tail -1)
  g=$( echo "$line" | grep -E "[0-9]+\sgreen" -o | cut -d " " -f1 | sort -n | tail -1 )
  b=$( echo "$line" | grep -E "[0-9]+\sblue" -o | cut -d " " -f1 | sort -n | tail -1 )
  s=$(($s + r * g * b))
done <$file

echo "Part 2: $s"


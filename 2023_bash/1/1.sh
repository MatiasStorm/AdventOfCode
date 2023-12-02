data=$( cat 1.txt );
numbers="one|two|three|four|five|six|seven|eight|nine"
declare -A number_str_map=( ["one"]="1" ["two"]="2" ["three"]="3" ["four"]="4" ["five"]="5" ["six"]="6" ["seven"]="7" ["eight"]="8" ["nine"]="9")
numbers_rev=$(echo $numbers | rev)
s_1=0
s_2=0
for line in $data
do
  line_rev=$(echo $line | rev)
  # part 1
  n=$(echo $line | grep -E "[1-9]{1}" -o | head -1)
  s_1=$(( $s_1 + $n * 10 ))
  n=$(echo $line_rev | grep -E "[1-9]{1}" -o | head -1)
  s_1=$(( $s_1 + $n ))
  
  # part 2
  n=$(echo $line | grep -E "([1-9]|$numbers)" -o | head -1)
  if [[ ${#n} > 1 ]]
  then
    n=${number_str_map[$n]}
  fi
  s_2=$(( $s_2 + $n * 10 ))

  n=$(echo $line_rev | grep -E "([1-9]|$numbers_rev)" -o | head -1 | rev)
  if [[ ${#n} > 1 ]]
  then
    n=${number_str_map[$n]}
  fi
  s_2=$(( $s_2 + $n ))
done
echo "Part 1: $s_1"
echo "Part 2: $s_2"

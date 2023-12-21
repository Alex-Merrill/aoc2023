#!/bin/zsh

# old_string="\.\/input.txt"
# new_string="input.txt"
old_string="\"input.txt\""
new_string="f\"{os.path.dirname(__file__)}\/input.txt\""
# old_string="second"
# new_string="nth"

cd "/home/alex/Code/aoc2023/"
for folder in *; do
  if [ -d $folder ]; then
    # echo "day $folder"
    # python3 $folder/code.py
    rm $folder/code.py.old
    # for file in $folder/*; do
    #   if [ -f "$file" ] && [ "$(basename "$file")" = "code.py" ]; then
    #     echo "$file"
    #     sed -i.old "s/$old_string/$new_string/g" "$file"
    #     # sed -i.old '1s;^;import os\n;' "$file"
    #   fi
    # done
  fi

done

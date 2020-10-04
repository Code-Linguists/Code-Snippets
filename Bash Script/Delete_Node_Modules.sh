
# To delete folders one by one and printing the folder being deleted

find . -name 'node_modules' -type d -prune -print -exec rm -rf '{}' \;

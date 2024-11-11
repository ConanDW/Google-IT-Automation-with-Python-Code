files=$(grep " jane " ~/data/list.txt | cut -d " " -f 3)
for file in $files; do 
        if test -e ~/$file; then echo $file >> oldFiles.txt; else echo "file not found"; fi
done

#REMEBER TO GO BACK AND SAVE OLD LABS
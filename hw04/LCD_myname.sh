# Here's how to use imagemagick to display text
# Make a blank image
SIZE=320x240
TMP_FILE=boris_ref_image.png;

convert $TMP_FILE -resize $TMP_FILE
convert $TMP_FILE -rotate 0 $TMP_FILE
convert $TMP_FILE -gravity center -fill purple -pointsize 60 -annotate 0 'Eliza Romeu'  $TMP_FILE

sudo fbi -noverbose -T 1 -a $TMP_FILE

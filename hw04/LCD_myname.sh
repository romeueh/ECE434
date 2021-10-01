# Here's how to use imagemagick to display text
# Make a blank image
SIZE=320x240
TMP_FILE=/tmp/frame.png

convert boris_ref_iamge.png -resize $TMP_FILE
convert $TMP_FILE -rotate 90 $TMP_FILE
convert $TMP_FILE -gravity NorthWest -annotate 0 'Eliza Romeu'  $TMP_FILE

sudo fbi -noverbose -T 1 -a $TMP_FILE

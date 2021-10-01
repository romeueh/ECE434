# Here's how to use imagemagick to display text
# Make a blank image
SIZE=320x240
TMP_FILE=boris_ref_iamge.png

convert TMP_FILE -resize $SIZE TMP_FILE
convert TMP_FILE -rotate 0 TMP_FILE
convert TMP_FILE -gravity NorthWest -annotate 0 'Eliza Romeu'  TMP_FILE

sudo fbi -noverbose -T 1 -a $TMP_FILE

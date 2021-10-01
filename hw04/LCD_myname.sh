# Here's how to use imagemagick to display text
# Make a blank image
SIZE=320x240
TMP_FILE=boris_ref_iamge.png

# From: http://www.imagemagick.org/Usage/text/
convert -font Times-Roman -pointsize 24 \
     -size $SIZE \
     label:'ImageMagick Usage' \
     -draw "text 0,200 'Eliza Romeu'" \
     $TMP_FILE

convert $TMP_FILE -rotate 0 $TMP_FILE
sudo fbi -noverbose -T 1 $TMP_FILE

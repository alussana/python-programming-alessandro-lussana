wget http://hgdownload.soe.ucsc.edu/goldenPath/eboVir3/bigZips/KM034562v1.fa.gz;
PATTERN=$1;
echo "Number of sites were $PATTERN pattern was found in the sequence:";
zcat KM034562v1.fa.gz | tr -d "\n" | grep -o $PATTERN | wc -l


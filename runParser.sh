rm *.dat
python parser.py ebay_data/items-*.json
sort -u *.dat
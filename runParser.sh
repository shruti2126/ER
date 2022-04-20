rm Items.dat
rm Category.dat
rm Bid.dat
rm Seller.dat
python parser.py ebay_data/items-*.json
sort Items.dat > Items.dat
sort Category.dat > Category.dat
sort Bid.dat > Bid.dat
sort Seller.dat > Seller.dat
uniq Items.dat > Items.dat
uniq Category.dat Category.dat
uniq Bid.dat > Bid.dat
uniq Seller.dat > Seller.dat
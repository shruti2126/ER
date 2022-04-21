rm -rf *.dat
python parser.py ebay_data/items-*.json
sort -u Items.dat > newItems.dat
sort -u Category.dat > newCategory.dat
sort -u Bid.dat > newBid.dat
sort -u Seller.dat > newSeller.dat
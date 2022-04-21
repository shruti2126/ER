-- Find the number of categories that include at least one item a bid of more that $100

select count (distinct c.CategoryName)
from Category c, Bid b
where c.ItemID=b.ItemID and b.Amount>100;

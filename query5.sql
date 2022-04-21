-- Find the number of sellers whose rating is higher than 1000
Select COUNT(UserID) from Seller
where rating > 1000;
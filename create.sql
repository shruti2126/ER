drop table if exists Items;
create table Items(
    ItemID int,
    Name varchar(255),
    Currently double,
    First_Bid  double,
    SellerID varchar(255),
    Number_Of_Bids int,
    Buy_Price double, 
    Started double, 
    Ends double, 
    Description varchar(255), 
    PRIMARY KEY (ItemID),
    FOREIGN KEY (SellerID) REFERENCES Seller(UserID)
);

drop table if exists Bid;
create table Bid (
    ItemID int, 
    Amount double, 
    Bid_Time TIMESTAMP,
    UserID varchar(255), 
    Rating int, 
    Location varchar(255), 
    Country varchar(255),
    Primary Key (ItemID, UserID),
    FOREIGN KEY (ItemID) REFERENCES Items(ItemID)
);

drop table if exists Seller;
create table Seller (
    UserID int, 
    Rating int, 
    PRIMARY KEY (UserID)
);

drop table if exists Category;
create table Category (
    ItemID int, 
    CategoryName varchar(255), 
    PRIMARY KEY (ItemID),
    FOREIGN KEY (ItemID) REFERENCES Items (ItemID)
);

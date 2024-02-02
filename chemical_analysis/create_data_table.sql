-- Active: 1697965526685@@127.0.0.1@3306
USE chemical_analysis;
CREATE TABLE IF NOT EXISTS chemicals_in_cosmetics (
    id INT NOT NULL AUTO_INCREMENT,
    CDPHId VARCHAR(50) NOT NULL,
    ProductName VARCHAR(255) NOT NULL,
    CSFId VARCHAR(45),
    CSF VARCHAR(45),
    CompanyId  VARCHAR(255),
    CompanyName VARCHAR(255),
    BrandName VARCHAR(255),
    PrimaryCategoryId VARCHAR(45),
    PrimaryCategory VARCHAR(255),
    SubCategoryId VARCHAR(45),
    SubCategory VARCHAR(255),
    CASId VARCHAR(255),
    CasNumber VARCHAR(255),
    ChemicalId VARCHAR(50),
    ChemicalName VARCHAR(255),
    InitialDateReported DATE,
    MostRecentDateReported DATE,
    DiscontinuedDate DATE,
    ChemicalCreatedAt DATE,
    ChemicalUpdatedAt DATE,
    ChemicalDateRemoved DATE,
    ChemicalCount INT,
    PRIMARY KEY (id, CDPHId, CSFId, SubCategoryId, ChemicalId)
)

LOAD DATA INFILE "archive.zip/chemicals-in-cosmetics-.csv" INTO TABLE chemicals_in_cosmetics
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS (`CDPHId`, `ProductName`, `CSFId`, `CSF`, `CompanyId`, `CompanyName`, `BrandName`, `PrimaryCategoryId`, `PrimaryCategory`, `SubCategoryId`, `SubCategory`, `CASId`, `CasNumber`,
`ChemicalId`, `ChemicalName`, `InitialDateReported`, `MostRecentDateReported`, `DiscontinuedDate`, `ChemicalCreatedAt`, `ChemicalUpdatedAt`, `ChemicalDateRemoved`, `ChemicalCount`);

SHOW VARIABLES LIKE "secure_file_priv";

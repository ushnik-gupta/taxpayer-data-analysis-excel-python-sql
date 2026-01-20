-- 1. View all taxpayer records
SELECT * FROM taxpayers;

-- 2. Average income by city
SELECT City, AVG(Annual_Income) AS Avg_Income
FROM taxpayers
GROUP BY City
ORDER BY Avg_Income DESC;

-- 3. Tax regime distribution
SELECT Tax_Regime, COUNT(*) AS Count
FROM taxpayers
GROUP BY Tax_Regime;

-- 4. High-income taxpayers (above 10 lakhs)
SELECT Taxpayer_ID, City, Annual_Income, Tax_Payable
FROM taxpayers
WHERE Annual_Income > 1000000
ORDER BY Annual_Income DESC;

-- 5. Compliance status summary
SELECT Compliance_Status, COUNT(*) AS Count
FROM taxpayers
GROUP BY Compliance_Status;

-- 6. Top 5 highest tax payers
SELECT Taxpayer_ID, Annual_Income, Tax_Payable
FROM taxpayers
ORDER BY Tax_Payable DESC
LIMIT 5;

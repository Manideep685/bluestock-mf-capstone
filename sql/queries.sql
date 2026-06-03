--1
SELECT SCHEMA_NAME, aum_core FROM fact_performance fp JOIN dim_fund df on fp.fund_id=df.fund_id
ORDER BY aum_core DESC LIMIT 5;
--2
SELECT strftime('%y-%m',date)month, AVG(nav) from fact_nav fn JOIN dim_date dd on fn.date_id = dd.date.id
 GROUP BY month;

 --3
 SELECT year, sum(amount) FROM fact_transactions ft JOIN dim_date dd on ft.date_id=dd.date_id WHERE TRANSACTION_type = 'SIP'
 GROUP BY YEAR;

 --4
 SELECT state ,COUNT(*) FROM fact_transactions GROUP BY state ORDER BY COUNT(*) DESC;

 --5
 SELECT SCHEMA_NAME,expense_ratio from fact_performance fp join dim_fund df on fp.fund_id=df.fund_id where expense_ratio<1;

 --6
 SELECT SCHEMA_NAME , return_5yr_pct from fact_performance fp JOIN dim_fund df on fp.fund_id=df.fund_id ORDER BY 
 return_5yr_pct DESC LIMIT 5;

 --7
 SELECT category , AVG(aum_core) from fact_performance fp JOIN dim_fund df on fp.fund_id=df.fund_id GROUP BY category

 --8
 SELECT fund_house , COUNT(*) from dim_fund GROUP BY fund_house ORDER BY COUNT(*) DESC;

 --9
 SELECT category,AVG(alpha) FROM fact_performance fp JOIN dim_fund df ON fp.fund_id=df.fund_id GROUP BY category;

 --10
 SELECT SUM(amount) from fact_transactions WHERE transaction_type = 'Redemption';
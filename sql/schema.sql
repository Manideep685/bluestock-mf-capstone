CREATE Table dim_fund(
    fund_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    amfi_code INTEGER,
    fund_house TEXT,
    scheme_name TEXT,
    category TEXT,
    plan TEXT
);

CREATE Table dim_date(
    date_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    date DATE,
    YEAR INTEGER,
    Quarter INTEGER,
    month INTEGER,
    day INTEGER
);

CREATE Table fact_nav(
    nav_id INTEGER PRIMARY key AUTO_INCREMENT,
    fund_id INTEGER,
    date_id INTEGER,
    nav REAL,
    FOREIGN KEY(fund_id) REFERENCES (dim_fund)
    FOREIGN key(date_id) REFERENCES (dim_date)
);
CREATE Table fact_transactions(
    investor_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    date_id INTEGER,
    fund_id INTEGER,
    transaction_type TEXT,
    amount REAL,
    state TEXT,
    kyc_status TEXT
);
CREATE Table fact_performance(
    performance_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    fund_id INTEGER,
    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,
    benchmark_3yr_pct REAL,
    alpha REAL,
    beta REAL,
    sharpe_ratio REAL,
    expense_ratio_pct REAL,
    aum_crore REAL,
    FOREIGN key (fund_id) REFERENCES (dim_fund)
);
CREATE Table fact_aum(
    aum_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    fund_id INTEGER,
    date_id INTEGER,
    aum_crore INTEGER,
    FOREIGN KEY (fund_id) REFERENCES (dim_fund)
    FOREIGN KEY (date_id) REFERENCES (dim_date)
);
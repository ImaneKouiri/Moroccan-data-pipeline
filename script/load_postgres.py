import pandas as pd
from sqlalchemy import create_engine

DB_USER = "imane"
DB_PASSWORD = "daTa_sLop4309!"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "moroccan_data"

CSV_PATH = "data/processed/socio_economic_indicators_clean.csv"

df =pd.read_csv(CSV_PATH)

df = df.rename(columns={
    "Country Name": "country",
    "Indicator Code": "indicator_code",
    "Indicator Name": "indicator_name"
})

df["source"] = "World Bank"

engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

df.to_sql(
    "socio_economic_indicators",
    engine,
    if_exists="append",
    index=False
)

print("Data successfully loaded into PostgreSQL")
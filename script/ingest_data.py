import pandas as pd 

RAW_DATA_PATH = "data/raw/worldbank_morocco.csv"
COUNTRY_NAME = "Morocco"
SELECTED_INDICATORS ={
    "SP.POP.TOTL": "Total population",
    "SL.UEM.TOTL.ZS": "Unemployment rate",
    "NY.GDP.MKTP.CD": "GDP (current USD)",
    "SE.ADT.LITR.ZS": "Literacy rate",
    "SP.DYN.LE00.IN": "Life expectancy"
}
START_YEAR = 2015
END_YEAR = 2024

df = pd.read_csv(RAW_DATA_PATH, skiprows=4)
df = df[df["Country Name"] == COUNTRY_NAME]

df= df[df["Indicator Code"].isin(SELECTED_INDICATORS.keys())]

year_columns = [str(year) for year in range (START_YEAR, END_YEAR + 1)]

columns_to_keep = [
    "Country Name",
    "Indicator Name",
    "Indicator Code"
] + year_columns

df = df[columns_to_keep]

df_long = df.melt(
    id_vars=["Country Name", "Indicator Name", "Indicator Code"],
    var_name="year",
    value_name="value"
)

df_long["year"] = df_long["year"].astype(int)
df_long = df_long.dropna(subset=["value"])

print(df_long.head())
print(f"Total rows after processing: {len(df_long)}")

OUTPUT_PATH = "data/processed/socio_economic_indicators_clean.csv"

df_long.to_csv(OUTPUT_PATH, index=False)

print(f"Processed data saved to {OUTPUT_PATH}")
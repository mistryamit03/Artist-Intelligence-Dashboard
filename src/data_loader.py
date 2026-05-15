# Adding imports
# Path helps work with file paths cleanly.


from pathlib import Path
import pandas as pd

# Address of the path and the file
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"

# Creating function to load CSV

def load_csv(file_name: str) -> pd.DataFrame:
    """Load one CSV file from the data folder."""
    file_path = DATA_DIR / file_name

    if not file_path.exists():
        raise FileNotFoundError(f"Missing file: {file_path}")

    return pd.read_csv(file_path)

# Load all mock CSV files used by the Artist Intelligence Dashboard.  
# Dictionary where each key is a dataset name and each value is a DataFrame.


def load_all_data() -> dict[str, pd.DataFrame]:


    data = {
        "artists": load_csv("artists.csv"),
        "tracks": load_csv("tracks.csv"),
        "daily_streams": load_csv("daily_streams.csv"),
        "campaigns": load_csv("campaigns.csv"),
        "campaign_performance": load_csv("campaign_performance.csv"),
        "playlist_performance": load_csv("playlist_performance.csv"),
        "market_performance": load_csv("market_performance.csv"),
        "audience_retention": load_csv("audience_retention.csv"),
        "recommendations": load_csv("recommendations.csv"),
        "trend_alerts": load_csv("trend_alerts.csv"),
    }

    # Convert date columns once after loading.
    date_columns = {
        "daily_streams": ["date"],
        "campaigns": ["start_date", "end_date"],
        "campaign_performance": ["date"],
        "playlist_performance": ["date"],
        "market_performance": ["date"],
        "trend_alerts": ["alert_timestamp"],
        "tracks": ["release_date"],
    }

# For loop to change the above date_columns in pd.to_datetime


    for dataset_name, columns in date_columns.items():
        for column in columns:
            if column in data[dataset_name].columns:
                data[dataset_name][column] = pd.to_datetime(data[dataset_name][column])

    return data


if __name__ == "__main__":
    all_data = load_all_data()

    for name, df in all_data.items():
        print(f"{name}: {df.shape[0]} rows, {df.shape[1]} columns")



from pathlib import Path
import numpy as np
import pandas as pd


# ============================================================
# Artist Intelligence Dashboard - Mock Data Generator
# ------------------------------------------------------------
# This script creates stable mock CSV files for the Streamlit app.
#
# Important:
# - The Streamlit app will only READ these CSVs.
# - The app will NOT regenerate data.
# - Run this script manually only when you want to recreate mock data:
#
#   python data_generator.py
#
# ============================================================


SEED = 42
rng = np.random.default_rng(SEED)

PROJECT_ROOT = Path(__file__).resolve().parent
DATA_DIR = PROJECT_ROOT / "data"
DATA_DIR.mkdir(exist_ok=True)

DATES = pd.date_range("2024-04-01", "2024-04-30", freq="D")

MARKETS = [
    "Germany",
    "United States",
    "United Kingdom",
    "France",
    "Canada",
    "Brazil",
    "Japan",
]

MARKET_WEIGHTS = {
    "Germany": 0.28,
    "United States": 0.22,
    "United Kingdom": 0.16,
    "France": 0.15,
    "Canada": 0.09,
    "Brazil": 0.05,
    "Japan": 0.05,
}

PLATFORMS = [
    "Spotify",
    "YouTube",
    "TikTok",
    "Apple Music",
    "Others",
]

PLATFORM_WEIGHTS = {
    "Spotify": 0.47,
    "YouTube": 0.24,
    "TikTok": 0.15,
    "Apple Music": 0.09,
    "Others": 0.05,
}


# ============================================================
# 1. ARTISTS
# ============================================================

artists = pd.DataFrame(
    [
        {
            "artist_id": "AR001",
            "artist_name": "LUNA",
            "genre": "Pop",
            "label_team": "Domestic Pop",
            "primary_market": "Germany",
            "debut_year": 2021,
        },
        {
            "artist_id": "AR002",
            "artist_name": "NOVA",
            "genre": "Electronic",
            "label_team": "Dance & Electronic",
            "primary_market": "United Kingdom",
            "debut_year": 2020,
        },
        {
            "artist_id": "AR003",
            "artist_name": "KAI",
            "genre": "Hip-Hop",
            "label_team": "Urban",
            "primary_market": "United States",
            "debut_year": 2019,
        },
        {
            "artist_id": "AR004",
            "artist_name": "MIRA",
            "genre": "Indie Pop",
            "label_team": "International",
            "primary_market": "France",
            "debut_year": 2022,
        },
    ]
)


# ============================================================
# 2. TRACKS
# Internal fields like target_streams are used only for generation.
# They are not exported to tracks.csv.
# ============================================================

track_profiles = [
    # LUNA tracks, designed to match the selected dashboard direction
    {
        "track_id": "TR001",
        "artist_id": "AR001",
        "track_name": "Midnight Drive",
        "release_name": "Midnight Drive",
        "release_type": "Single",
        "release_date": "2024-03-15",
        "genre": "Pop",
        "is_catalog": False,
        "target_streams": 3_450_000,
        "base_save_rate": 0.098,
        "base_skip_rate": 0.221,
    },
    {
        "track_id": "TR002",
        "artist_id": "AR001",
        "track_name": "Never Break",
        "release_name": "Never Break",
        "release_type": "Single",
        "release_date": "2024-03-20",
        "genre": "Pop",
        "is_catalog": False,
        "target_streams": 2_910_000,
        "base_save_rate": 0.086,
        "base_skip_rate": 0.247,
    },
    {
        "track_id": "TR003",
        "artist_id": "AR001",
        "track_name": "Another Life",
        "release_name": "Another Life",
        "release_type": "Single",
        "release_date": "2024-02-14",
        "genre": "Pop",
        "is_catalog": False,
        "target_streams": 2_480_000,
        "base_save_rate": 0.079,
        "base_skip_rate": 0.253,
    },
    {
        "track_id": "TR004",
        "artist_id": "AR001",
        "track_name": "Falling Again",
        "release_name": "Falling Again",
        "release_type": "Single",
        "release_date": "2024-02-05",
        "genre": "Pop",
        "is_catalog": False,
        "target_streams": 2_100_000,
        "base_save_rate": 0.081,
        "base_skip_rate": 0.238,
    },
    {
        "track_id": "TR005",
        "artist_id": "AR001",
        "track_name": "Home",
        "release_name": "Home",
        "release_type": "Single",
        "release_date": "2023-10-30",
        "genre": "Pop",
        "is_catalog": True,
        "target_streams": 1_880_000,
        "base_save_rate": 0.073,
        "base_skip_rate": 0.269,
    },
    {
        "track_id": "TR006",
        "artist_id": "AR001",
        "track_name": "City Lights",
        "release_name": "City Lights",
        "release_type": "Single",
        "release_date": "2024-03-15",
        "genre": "Pop",
        "is_catalog": False,
        "target_streams": 1_260_000,
        "base_save_rate": 0.098,
        "base_skip_rate": 0.226,
    },
    {
        "track_id": "TR007",
        "artist_id": "AR001",
        "track_name": "Before Sunrise",
        "release_name": "Before Sunrise",
        "release_type": "Single",
        "release_date": "2023-09-12",
        "genre": "Pop",
        "is_catalog": True,
        "target_streams": 612_000,
        "base_save_rate": 0.121,
        "base_skip_rate": 0.214,
    },
    {
        "track_id": "TR008",
        "artist_id": "AR001",
        "track_name": "Echo Hearts",
        "release_name": "Echo Hearts",
        "release_type": "Single",
        "release_date": "2023-12-11",
        "genre": "Pop",
        "is_catalog": True,
        "target_streams": 1_500_000,
        "base_save_rate": 0.084,
        "base_skip_rate": 0.233,
    },
    {
        "track_id": "TR009",
        "artist_id": "AR001",
        "track_name": "Neon Rain",
        "release_name": "Neon Rain",
        "release_type": "Single",
        "release_date": "2023-08-18",
        "genre": "Pop",
        "is_catalog": True,
        "target_streams": 1_300_000,
        "base_save_rate": 0.069,
        "base_skip_rate": 0.281,
    },
    {
        "track_id": "TR010",
        "artist_id": "AR001",
        "track_name": "Velvet Sky",
        "release_name": "Velvet Sky",
        "release_type": "Album Track",
        "release_date": "2023-06-02",
        "genre": "Pop",
        "is_catalog": True,
        "target_streams": 1_200_000,
        "base_save_rate": 0.066,
        "base_skip_rate": 0.276,
    },

    # Other artists, included for filters and realistic multi-artist data
    {
        "track_id": "TR011",
        "artist_id": "AR002",
        "track_name": "Signal Blue",
        "release_name": "Signal Blue",
        "release_type": "Single",
        "release_date": "2024-03-05",
        "genre": "Electronic",
        "is_catalog": False,
        "target_streams": 1_250_000,
        "base_save_rate": 0.074,
        "base_skip_rate": 0.252,
    },
    {
        "track_id": "TR012",
        "artist_id": "AR002",
        "track_name": "After Midnight",
        "release_name": "After Midnight",
        "release_type": "Single",
        "release_date": "2024-01-19",
        "genre": "Electronic",
        "is_catalog": False,
        "target_streams": 980_000,
        "base_save_rate": 0.068,
        "base_skip_rate": 0.271,
    },
    {
        "track_id": "TR013",
        "artist_id": "AR003",
        "track_name": "No Limits",
        "release_name": "No Limits",
        "release_type": "Single",
        "release_date": "2024-02-09",
        "genre": "Hip-Hop",
        "is_catalog": False,
        "target_streams": 1_650_000,
        "base_save_rate": 0.058,
        "base_skip_rate": 0.302,
    },
    {
        "track_id": "TR014",
        "artist_id": "AR003",
        "track_name": "Street Echo",
        "release_name": "Street Echo",
        "release_type": "Single",
        "release_date": "2023-11-22",
        "genre": "Hip-Hop",
        "is_catalog": True,
        "target_streams": 890_000,
        "base_save_rate": 0.063,
        "base_skip_rate": 0.294,
    },
    {
        "track_id": "TR015",
        "artist_id": "AR004",
        "track_name": "Paris Morning",
        "release_name": "Paris Morning",
        "release_type": "Single",
        "release_date": "2024-03-01",
        "genre": "Indie Pop",
        "is_catalog": False,
        "target_streams": 1_100_000,
        "base_save_rate": 0.082,
        "base_skip_rate": 0.231,
    },
]

tracks_export = pd.DataFrame(track_profiles)[
    [
        "track_id",
        "artist_id",
        "track_name",
        "release_name",
        "release_type",
        "release_date",
        "genre",
        "is_catalog",
    ]
]


# ============================================================
# 3. DAILY STREAMS
# ============================================================

daily_rows = []

for track in track_profiles:
    temporary_rows = []

    for date in DATES:
        day_number = (date - DATES.min()).days + 1

        # General month curve: gradual growth over the month
        day_curve = 0.85 + (day_number / len(DATES)) * 0.35

        # Small weekly rhythm
        weekly_curve = 1 + 0.08 * np.sin(day_number / 7 * 2 * np.pi)

        for market in MARKETS:
            for platform in PLATFORMS:
                raw_weight = (
                    MARKET_WEIGHTS[market]
                    * PLATFORM_WEIGHTS[platform]
                    * day_curve
                    * weekly_curve
                )

                # Business scenario 1:
                # City Lights is trending in France in the final week.
                if track["track_name"] == "City Lights" and market == "France" and day_number >= 24:
                    raw_weight *= 1.42

                # Business scenario 2:
                # Before Sunrise is an older catalog track resurging on TikTok.
                if track["track_name"] == "Before Sunrise" and platform == "TikTok" and day_number >= 22:
                    raw_weight *= 1.62

                # Business scenario 3:
                # Another Life is losing momentum in the US.
                if track["track_name"] == "Another Life" and market == "United States" and day_number >= 24:
                    raw_weight *= 0.82

                # Controlled noise to avoid perfectly artificial data
                raw_weight *= rng.normal(loc=1.0, scale=0.08)

                temporary_rows.append(
                    {
                        "date": date.date().isoformat(),
                        "artist_id": track["artist_id"],
                        "track_id": track["track_id"],
                        "platform": platform,
                        "market": market,
                        "raw_weight": max(raw_weight, 0.0001),
                    }
                )

    temp_df = pd.DataFrame(temporary_rows)
    scale_factor = track["target_streams"] / temp_df["raw_weight"].sum()
    temp_df["streams"] = (temp_df["raw_weight"] * scale_factor).round().astype(int)

    # Listener logic: repeat listening means streams > listeners
    repeat_factor = rng.uniform(3.8, 7.2)
    temp_df["listeners"] = (temp_df["streams"] / repeat_factor).round().astype(int)
    temp_df["listeners"] = temp_df["listeners"].clip(lower=1)

    # Save and skip logic
    save_noise = rng.normal(loc=1.0, scale=0.05, size=len(temp_df))
    skip_noise = rng.normal(loc=1.0, scale=0.04, size=len(temp_df))

    temp_df["saves"] = (
        temp_df["streams"] * track["base_save_rate"] * save_noise
    ).round().astype(int)

    temp_df["skips"] = (
        temp_df["streams"] * track["base_skip_rate"] * skip_noise
    ).round().astype(int)

    # Follower gain: higher for stronger save-rate tracks
    follower_factor = 0.010 + track["base_save_rate"] * 0.11
    temp_df["followers_gained"] = (
        temp_df["streams"] * follower_factor * rng.normal(loc=1.0, scale=0.04, size=len(temp_df))
    ).round().astype(int)

    temp_df["saves"] = temp_df[["saves", "streams"]].min(axis=1)
    temp_df["skips"] = temp_df[["skips", "streams"]].min(axis=1)

    daily_rows.append(
        temp_df[
            [
                "date",
                "artist_id",
                "track_id",
                "platform",
                "market",
                "streams",
                "listeners",
                "saves",
                "skips",
                "followers_gained",
            ]
        ]
    )

daily_streams = pd.concat(daily_rows, ignore_index=True)


# ============================================================
# 4. CAMPAIGNS
# ============================================================

campaigns = pd.DataFrame(
    [
        {
            "campaign_id": "CA001",
            "artist_id": "AR001",
            "track_id": "TR006",
            "campaign_name": "TikTok Boost",
            "channel": "TikTok Ads",
            "market": "France",
            "start_date": "2024-04-01",
            "end_date": "2024-04-30",
            "spend_eur": 20000,
            "objective": "Awareness",
            "target_streams": 2_030_000,
            "target_new_followers": 21_400,
            "target_save_rate": 0.031,
            "roas_proxy": 1.42,
        },
        {
            "campaign_id": "CA002",
            "artist_id": "AR001",
            "track_id": "TR002",
            "campaign_name": "Instagram Push",
            "channel": "Instagram Ads",
            "market": "Germany",
            "start_date": "2024-04-01",
            "end_date": "2024-04-30",
            "spend_eur": 15000,
            "objective": "Fan Conversion",
            "target_streams": 1_280_000,
            "target_new_followers": 17_800,
            "target_save_rate": 0.092,
            "roas_proxy": 1.98,
        },
        {
            "campaign_id": "CA003",
            "artist_id": "AR001",
            "track_id": "TR003",
            "campaign_name": "YouTube Ads",
            "channel": "YouTube Ads",
            "market": "United States",
            "start_date": "2024-04-01",
            "end_date": "2024-04-30",
            "spend_eur": 15000,
            "objective": "Video Reach",
            "target_streams": 1_020_000,
            "target_new_followers": 5_100,
            "target_save_rate": 0.022,
            "roas_proxy": 0.98,
        },
        {
            "campaign_id": "CA004",
            "artist_id": "AR001",
            "track_id": "TR001",
            "campaign_name": "Spotify Marquee",
            "channel": "Spotify Ads",
            "market": "Germany",
            "start_date": "2024-04-01",
            "end_date": "2024-04-30",
            "spend_eur": 10000,
            "objective": "Release Amplification",
            "target_streams": 810_000,
            "target_new_followers": 3_200,
            "target_save_rate": 0.065,
            "roas_proxy": 1.35,
        },
    ]
)

campaign_performance_rows = []

for _, campaign in campaigns.iterrows():
    campaign_dates = pd.date_range(campaign["start_date"], campaign["end_date"], freq="D")
    raw = rng.normal(loc=1.0, scale=0.15, size=len(campaign_dates))
    raw = np.clip(raw, 0.4, None)
    weights = raw / raw.sum()

    for date, weight in zip(campaign_dates, weights):
        spend = campaign["spend_eur"] * weight
        streams = campaign["target_streams"] * weight
        followers = campaign["target_new_followers"] * weight
        saves = streams * campaign["target_save_rate"]

        # Simple channel-specific assumptions
        if campaign["channel"] == "TikTok Ads":
            ctr = 0.018
            impressions = spend * 950
        elif campaign["channel"] == "Instagram Ads":
            ctr = 0.026
            impressions = spend * 800
        elif campaign["channel"] == "YouTube Ads":
            ctr = 0.014
            impressions = spend * 1050
        else:
            ctr = 0.021
            impressions = spend * 700

        clicks = impressions * ctr

        campaign_performance_rows.append(
            {
                "campaign_id": campaign["campaign_id"],
                "date": date.date().isoformat(),
                "spend_eur": round(spend, 2),
                "impressions": int(round(impressions)),
                "clicks": int(round(clicks)),
                "streams_attributed": int(round(streams)),
                "new_followers": int(round(followers)),
                "saves": int(round(saves)),
                "control_streams": int(round(streams * rng.uniform(0.78, 0.92))),
            }
        )

campaign_performance = pd.DataFrame(campaign_performance_rows)

campaigns_export = campaigns.drop(
    columns=[
        "target_streams",
        "target_new_followers",
        "target_save_rate",
        "roas_proxy",
    ]
)


# ============================================================
# 5. PLAYLIST PERFORMANCE
# ============================================================

playlist_performance = pd.DataFrame(
    [
        {
            "date": "2024-04-30",
            "artist_id": "AR001",
            "track_id": "TR001",
            "playlist_name": "Today's Top Hits",
            "playlist_type": "Editorial",
            "platform": "Spotify",
            "market": "Global",
            "playlist_reach": 12_500_000,
            "playlist_adds": 18_200,
            "playlist_streams": 1_260_000,
            "saves_from_playlist": 118_440,
        },
        {
            "date": "2024-04-30",
            "artist_id": "AR001",
            "track_id": "TR002",
            "playlist_name": "Viral Hits",
            "playlist_type": "Algorithmic",
            "platform": "Spotify",
            "market": "Global",
            "playlist_reach": 8_900_000,
            "playlist_adds": 14_700,
            "playlist_streams": 982_000,
            "saves_from_playlist": 79_542,
        },
        {
            "date": "2024-04-30",
            "artist_id": "AR001",
            "track_id": "TR006",
            "playlist_name": "New Music Friday",
            "playlist_type": "Editorial",
            "platform": "Spotify",
            "market": "Germany",
            "playlist_reach": 5_600_000,
            "playlist_adds": 9_300,
            "playlist_streams": 712_000,
            "saves_from_playlist": 72_624,
        },
        {
            "date": "2024-04-30",
            "artist_id": "AR001",
            "track_id": "TR007",
            "playlist_name": "Fresh Finds",
            "playlist_type": "User Generated",
            "platform": "Spotify",
            "market": "Germany",
            "playlist_reach": 2_400_000,
            "playlist_adds": 5_100,
            "playlist_streams": 432_000,
            "saves_from_playlist": 38_448,
        },
        {
            "date": "2024-04-30",
            "artist_id": "AR001",
            "track_id": "TR003",
            "playlist_name": "Pop Rising",
            "playlist_type": "Algorithmic",
            "platform": "Spotify",
            "market": "United States",
            "playlist_reach": 3_300_000,
            "playlist_adds": 6_800,
            "playlist_streams": 512_000,
            "saves_from_playlist": 38_912,
        },
    ]
)


# ============================================================
# 6. MARKET PERFORMANCE
# Aggregated from daily_streams.
# ============================================================

market_performance = (
    daily_streams.groupby(["date", "artist_id", "market"], as_index=False)
    .agg(
        streams=("streams", "sum"),
        listeners=("listeners", "sum"),
        saves=("saves", "sum"),
        skips=("skips", "sum"),
        new_followers=("followers_gained", "sum"),
    )
)

market_performance["save_rate"] = (
    market_performance["saves"] / market_performance["streams"] * 100
).round(2)

market_performance["skip_rate"] = (
    market_performance["skips"] / market_performance["streams"] * 100
).round(2)


# ============================================================
# 7. AUDIENCE RETENTION
# ============================================================

retention_days = [1, 7, 30, 60, 90]
retention_rows = []

for track in track_profiles:
    if track["artist_id"] != "AR001":
        continue

    base_curve = {
        1: rng.uniform(55, 75),
        7: rng.uniform(24, 38),
        30: rng.uniform(10, 18),
        60: rng.uniform(6, 11),
        90: rng.uniform(3, 8),
    }

    # Stronger save-rate tracks retain better
    if track["base_save_rate"] >= 0.095:
        base_curve = {day: value * 1.12 for day, value in base_curve.items()}

    # High skip-rate tracks retain slightly worse
    if track["base_skip_rate"] >= 0.26:
        base_curve = {day: value * 0.88 for day, value in base_curve.items()}

    previous_value = 100

    for day in retention_days:
        retained_pct = min(base_curve[day], previous_value)
        previous_value = retained_pct

        retention_rows.append(
            {
                "artist_id": track["artist_id"],
                "track_id": track["track_id"],
                "cohort_day": day,
                "retained_listener_pct": round(retained_pct, 2),
            }
        )

audience_retention = pd.DataFrame(retention_rows)


# ============================================================
# 8. RECOMMENDATIONS
# Mock recommendations designed around business logic.
# ============================================================

recommendations = pd.DataFrame(
    [
        {
            "recommendation_id": "REC001",
            "artist_id": "AR001",
            "track_id": "TR006",
            "recommendation_type": "Playlist Amplification",
            "priority": "High",
            "recommendation_text": "Amplify 'City Lights' in France through playlist pitching and paid support.",
            "business_reason": "France shows strong WoW growth and the track has a strong save rate.",
            "estimated_impact": "+320K streams",
        },
        {
            "recommendation_id": "REC002",
            "artist_id": "AR001",
            "track_id": "TR002",
            "recommendation_type": "Retargeting",
            "priority": "High",
            "recommendation_text": "Boost Instagram retargeting for 'Never Break'.",
            "business_reason": "Instagram has lower reach than TikTok, but stronger retention and save behavior.",
            "estimated_impact": "+180K saves",
        },
        {
            "recommendation_id": "REC003",
            "artist_id": "AR001",
            "track_id": "TR007",
            "recommendation_type": "Catalog Revival",
            "priority": "Medium",
            "recommendation_text": "Revive catalog track 'Before Sunrise' with TikTok creator posts.",
            "business_reason": "The track has low reach but high save rate and rising TikTok usage.",
            "estimated_impact": "+140K streams",
        },
        {
            "recommendation_id": "REC004",
            "artist_id": "AR001",
            "track_id": "TR003",
            "recommendation_type": "Budget Reallocation",
            "priority": "Medium",
            "recommendation_text": "Reduce YouTube budget for 'Another Life' in the United States.",
            "business_reason": "The campaign has high reach but weak save rate and declining WoW performance.",
            "estimated_impact": "Avoid inefficient spend",
        },
    ]
)


# ============================================================
# 9. TREND ALERTS
# ============================================================

trend_alerts = pd.DataFrame(
    [
        {
            "alert_id": "AL001",
            "artist_id": "AR001",
            "track_id": "TR006",
            "market": "France",
            "alert_type": "Market Spike",
            "alert_text": "Track 'City Lights' grew +42% WoW in France.",
            "metric_name": "streams_wow_growth",
            "current_value": 1_710_000,
            "previous_value": 1_204_000,
            "change_pct": 42.0,
            "alert_timestamp": "2024-04-30 09:15:00",
            "severity": "High",
        },
        {
            "alert_id": "AL002",
            "artist_id": "AR001",
            "track_id": "TR001",
            "market": "Germany",
            "alert_type": "Follower Growth",
            "alert_text": "LUNA followers in Germany grew +31% in the last 7 days.",
            "metric_name": "followers_growth",
            "current_value": 312_000,
            "previous_value": 238_000,
            "change_pct": 31.0,
            "alert_timestamp": "2024-04-30 08:40:00",
            "severity": "High",
        },
        {
            "alert_id": "AL003",
            "artist_id": "AR001",
            "track_id": "TR003",
            "market": "United States",
            "alert_type": "Decline",
            "alert_text": "'Another Life' streams dropped -18% WoW in the United States.",
            "metric_name": "streams_wow_growth",
            "current_value": 420_000,
            "previous_value": 512_000,
            "change_pct": -18.0,
            "alert_timestamp": "2024-04-30 07:22:00",
            "severity": "Medium",
        },
        {
            "alert_id": "AL004",
            "artist_id": "AR001",
            "track_id": "TR007",
            "market": "Global",
            "alert_type": "Catalog Revival",
            "alert_text": "Catalog track 'Before Sunrise' is spiking on TikTok.",
            "metric_name": "tiktok_streams_growth",
            "current_value": 198_000,
            "previous_value": 120_000,
            "change_pct": 65.0,
            "alert_timestamp": "2024-04-30 06:50:00",
            "severity": "High",
        },
    ]
)


# ============================================================
# 10. VALIDATION CHECKS
# ============================================================

def validate_data() -> None:
    errors = []

    artist_ids = set(artists["artist_id"])
    track_ids = set(tracks_export["track_id"])
    campaign_ids = set(campaigns_export["campaign_id"])

    # Key relationship checks
    if not set(tracks_export["artist_id"]).issubset(artist_ids):
        errors.append("tracks.csv contains artist_id values not found in artists.csv")

    if not set(daily_streams["artist_id"]).issubset(artist_ids):
        errors.append("daily_streams.csv contains artist_id values not found in artists.csv")

    if not set(daily_streams["track_id"]).issubset(track_ids):
        errors.append("daily_streams.csv contains track_id values not found in tracks.csv")

    if not set(campaigns_export["artist_id"]).issubset(artist_ids):
        errors.append("campaigns.csv contains artist_id values not found in artists.csv")

    if not set(campaigns_export["track_id"]).issubset(track_ids):
        errors.append("campaigns.csv contains track_id values not found in tracks.csv")

    if not set(campaign_performance["campaign_id"]).issubset(campaign_ids):
        errors.append("campaign_performance.csv contains campaign_id values not found in campaigns.csv")

    if not set(playlist_performance["track_id"]).issubset(track_ids):
        errors.append("playlist_performance.csv contains track_id values not found in tracks.csv")

    if not set(audience_retention["track_id"]).issubset(track_ids):
        errors.append("audience_retention.csv contains track_id values not found in tracks.csv")

    if not set(recommendations["track_id"]).issubset(track_ids):
        errors.append("recommendations.csv contains track_id values not found in tracks.csv")

    if not set(trend_alerts["track_id"]).issubset(track_ids):
        errors.append("trend_alerts.csv contains track_id values not found in tracks.csv")

    # Non-negative checks
    non_negative_checks = {
        "daily_streams.streams": daily_streams["streams"],
        "daily_streams.listeners": daily_streams["listeners"],
        "daily_streams.saves": daily_streams["saves"],
        "daily_streams.skips": daily_streams["skips"],
        "daily_streams.followers_gained": daily_streams["followers_gained"],
        "campaigns.spend_eur": campaigns_export["spend_eur"],
        "campaign_performance.spend_eur": campaign_performance["spend_eur"],
        "campaign_performance.streams_attributed": campaign_performance["streams_attributed"],
        "playlist_performance.playlist_streams": playlist_performance["playlist_streams"],
        "market_performance.streams": market_performance["streams"],
    }

    for label, values in non_negative_checks.items():
        if (values < 0).any():
            errors.append(f"{label} contains negative values")

    # Logical metric checks
    if (daily_streams["saves"] > daily_streams["streams"]).any():
        errors.append("daily_streams.csv contains saves greater than streams")

    if (daily_streams["skips"] > daily_streams["streams"]).any():
        errors.append("daily_streams.csv contains skips greater than streams")

    if (daily_streams["listeners"] > daily_streams["streams"]).any():
        errors.append("daily_streams.csv contains listeners greater than streams")

    if not market_performance["save_rate"].between(0, 100).all():
        errors.append("market_performance.csv contains invalid save_rate values")

    if not market_performance["skip_rate"].between(0, 100).all():
        errors.append("market_performance.csv contains invalid skip_rate values")

    if not audience_retention["retained_listener_pct"].between(0, 100).all():
        errors.append("audience_retention.csv contains invalid retained_listener_pct values")

    # Campaign date checks
    campaign_dates = campaigns_export.copy()
    campaign_dates["start_date"] = pd.to_datetime(campaign_dates["start_date"])
    campaign_dates["end_date"] = pd.to_datetime(campaign_dates["end_date"])

    if (campaign_dates["start_date"] > campaign_dates["end_date"]).any():
        errors.append("campaigns.csv contains start_date later than end_date")

    # Campaign spend consistency
    campaign_spend_check = (
        campaign_performance.groupby("campaign_id", as_index=False)["spend_eur"]
        .sum()
        .merge(campaigns_export[["campaign_id", "spend_eur"]], on="campaign_id", suffixes=("_daily", "_campaign"))
    )

    campaign_spend_check["difference"] = (
        campaign_spend_check["spend_eur_daily"] - campaign_spend_check["spend_eur_campaign"]
    ).abs()

    if (campaign_spend_check["difference"] > 1.0).any():
        errors.append("campaign_performance spend does not match campaigns spend")

    if errors:
        print("VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        raise ValueError("Mock data validation failed.")

    print("All validation checks passed.")


# ============================================================
# 11. EXPORT CSV FILES
# ============================================================

def export_csv_files() -> None:
    artists.to_csv(DATA_DIR / "artists.csv", index=False)
    tracks_export.to_csv(DATA_DIR / "tracks.csv", index=False)
    daily_streams.to_csv(DATA_DIR / "daily_streams.csv", index=False)
    campaigns_export.to_csv(DATA_DIR / "campaigns.csv", index=False)
    campaign_performance.to_csv(DATA_DIR / "campaign_performance.csv", index=False)
    playlist_performance.to_csv(DATA_DIR / "playlist_performance.csv", index=False)
    market_performance.to_csv(DATA_DIR / "market_performance.csv", index=False)
    audience_retention.to_csv(DATA_DIR / "audience_retention.csv", index=False)
    recommendations.to_csv(DATA_DIR / "recommendations.csv", index=False)
    trend_alerts.to_csv(DATA_DIR / "trend_alerts.csv", index=False)

    print(f"CSV files created in: {DATA_DIR}")


if __name__ == "__main__":
    validate_data()
    export_csv_files()
    print("Mock data generation complete.")
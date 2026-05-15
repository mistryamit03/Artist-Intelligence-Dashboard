import pandas as pd

# Each attributed stream is estimated to be worth €0.012 in this mock project. This will be later used to calculate ROAS Proxy

STIMATED_STREAM_VALUE_EUR = 0.012

#Creatig the divide funtion

def safe_divide(numerator: float, denominator: float) -> float:

    # Why we are doing this: Avoiding errors that come by dividing by zero

    if denominator == 0:
        return 0.0
    return numerator/denominator



# Phase 1: Creating Artist Performance KPIs function to calculate High performance KPIs. 
# Everything here is coming from daily_streams csv
    # - Total Streams
    # - Monthly Listeners
    # - Followers
    # - Average Save Rate
    # - Streams per Listener
    # - Skip Rate

def calculate_artist_performance(daily_streams: pd.DataFrame) -> dict:

    total_streams = daily_streams["streams"].sum()
    monthly_listeners = daily_streams["listeners"].sum()
    followers = daily_streams["followers_gained"].sum()
    total_saves = daily_streams["saves"].sum()
    total_skips = daily_streams["skips"].sum()

    average_save_rate  = safe_divide(total_saves, total_streams) * 100
    streams_per_listener = safe_divide(total_streams,monthly_listeners)
    skip_rate = safe_divide(total_skips, total_streams) * 100


    return {
        "total_streams": round(total_streams),
        "monthly_listeners": round(monthly_listeners),
        "followers": round(followers),
        "average_save_rate": round(average_save_rate, 2),
        "streams_per_listener": round(streams_per_listener, 2),
        "skip_rate": round(skip_rate, 2),
    }


# Phase 2: Audience Retention KPIs: If streams are much higher than listeners, users are replaying tracks. Because its streaming the same song not increasing the number of listners.
# Here we for this we will need 2 tables daily_streams and audience_retention
# KPIs we are adding
# Repeat Listener % = proxy based on streams vs listeners
# D7 Retention = average retained_listener_pct where cohort_day = 7
# D30 Retention = average retained_listener_pct where cohort_day = 30
# Returning Listener Ratio = same proxy as repeat listener %



def calculate_audience_retention(daily_streams: pd.DataFrame, audience_retention: pd.DataFrame,) -> dict:

    total_streams = daily_streams["streams"].sum()
    total_listeners = daily_streams["listeners"].sum()


# If streams are much higher than listeners, people are listening repeatedly.
    repeat_listener_pct = (1 - safe_divide(total_listeners,total_streams) * 100)


# What percentage of listeners are still returning after 7 days?
    d7_retention = audience_retention.loc[audience_retention["cohort_day"] == 7,"retained_listener_pct",].mean()


# What percentage of listeners are still returning after 30 days?
    d30_retention = audience_retention.loc[audience_retention["cohort_day"] == 30, "retained_listener_pct,"].mean()

    returning_listener_ratio = repeat_listener_pct



    return {
        "repeat_listener_pct": round(repeat_listener_pct, 2),
        "d7_retention": round(d7_retention, 2),
        "d30_retention": round(d30_retention, 2),
        "returning_listener_ratio": round(returning_listener_ratio, 2),
    }






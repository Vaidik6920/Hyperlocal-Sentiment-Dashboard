import geopandas as gpd
import folium
from folium.plugins import MarkerCluster


def to_geodataframe(df):
    gdf = gpd.GeoDataFrame(
        df.dropna(subset=["latitude", "longitude"]),
        geometry=gpd.points_from_xy(df.longitude, df.latitude),
        crs="EPSG:4326"
    )
    return gdf


def plot_sentiment_map(gdf):
    sentiment_colors = {"Positive": "green", "Negative": "red", "Neutral": "gray"}
    m = folium.Map(location=[gdf.geometry.y.mean(), gdf.geometry.x.mean()], zoom_start=9)
    marker_cluster = MarkerCluster().add_to(m)

    for _, row in gdf.iterrows():
        folium.Marker(
            location=[row.geometry.y, row.geometry.x],
            popup=row["content"][:200],
            icon=folium.Icon(color=sentiment_colors.get(row["sentiment_label"], "blue"))
        ).add_to(marker_cluster)

    return m


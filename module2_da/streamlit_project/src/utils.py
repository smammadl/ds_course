import plotly.express as px

def to_title(col_name):
    return col_name.replace("_", " ").title()

def get_map(housing_df):
    fig = px.scatter_map(
        housing_df, 
        lat="latitude", 
        lon="longitude", 
        color="median_house_value",
        size="population",
        color_continuous_scale=px.colors.sequential.Jet,
        center={"lat": 37, "lon": -123},
        zoom=5,
        size_max=15,
        map_style="carto-positron",
        title="California Housing Map",
        labels={
            "latitude": "Latitude",
            "longitude": "Longitude",
            "median_house_value": "Median House Value",
            "population": "Population"
        }
    )
    fig.update_layout(
        height=700, 
        margin={"r": 0, "l": 0, "b": 0},
        )
    return fig
    
def get_scatter_plot(housing_df, x_val, y_val, color_val=None, size_val=None, margin_type=None):
    color_val = color_val if color_val not in [None, "", "None"] else None
    size_val = size_val if size_val not in [None, "", "None"] else None
    fig = px.scatter(
        housing_df,
        x=x_val,
        y=y_val,
        color=color_val,
        opacity=0.5,
        size=size_val,
        title=f"{to_title(x_val)} vs {to_title(y_val)}",
        marginal_x=margin_type,
        marginal_y=margin_type,
        template="plotly_white",
        labels={
            x_val: to_title(x_val),
            y_val: to_title(y_val),
            color_val: to_title(color_val) if color_val else None,
            size_val: to_title(size_val) if size_val else None
        }
    )
    fig.update_layout(
        height=600
    )
    fig.update_traces(
        marker={
            "line": {
                "width": 0.5,
                "color": "DarkSlateGray"
            }
        },
    )
    return fig

def get_histogram(housing_df, x_val, nbins_val=100, margin_val=False):
    fig = px.histogram(
        housing_df,
        x=x_val,
        nbins=nbins_val,
        marginal="box" if margin_val else None,
        title=f"Histogram of {to_title(x_val)}",
        template="plotly_white",
        labels={
            x_val: to_title(x_val)
        }
    )
    return fig

def get_correlation_matrix(housing_df):
    corr_matrix = housing_df.select_dtypes(include=['number']).corr()
    fig = px.imshow(
        corr_matrix,
        title="Correlation Matrix",
        origin="lower",
        text_auto=".2f",
        aspect="auto",
        color_continuous_scale=px.colors.sequential.RdBu,
    )
    fig.update_layout(
        height=600,
    )
    return fig

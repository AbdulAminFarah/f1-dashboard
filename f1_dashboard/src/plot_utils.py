import plotly.express as px

def plot_lap_times(laps_df, driver_name, color):
    fig = px.line(
        laps_df,
        x='LapNumber',
        y=laps_df['LapTime'].dt.total_seconds(),
        title=f'{driver_name} Lap Times',
        markers=True
    )
    fig.update_traces(line_color=color)
    fig.update_layout(xaxis_title='Lap Number', yaxis_title='Lap Time (s)')
    return fig


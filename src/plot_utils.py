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

# Add plot_stint_strategy()
import plotly.graph_objects as go

def plot_stint_strategy(stints, driver_code, color):
    """Gantt-style chart of tyre usage by stint."""
    fig = go.Figure()

    for _, row in stints.iterrows():
        fig.add_trace(go.Bar(
            x=[row['EndLap'] - row['StartLap']],
            y=[driver_code],
            base=[row['StartLap']],
            orientation='h',
            marker=dict(color=color),
            name=row['Compound'],
            hovertext=f"{row['Compound']} | Laps {row['StartLap']}–{row['EndLap']}"
        ))

    fig.update_layout(
        title=f"{driver_code} Tyre Strategy",
        xaxis_title='Lap',
        barmode='stack',
        showlegend=False
    )
    return fig

import plotly.express as px
import plotly.graph_objects as go


def plot_lap_times(laps1, laps2, driver1, driver2):
    """Create line chart comparing lap times for two drivers."""
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=laps1['LapNumber'],
        y=laps1['LapTime'].dt.total_seconds(),
        mode='lines+markers',
        name=driver1,
        line=dict(color='red')
    ))

    fig.add_trace(go.Scatter(
        x=laps2['LapNumber'],
        y=laps2['LapTime'].dt.total_seconds(),
        mode='lines+markers',
        name=driver2,
        line=dict(color='blue')
    ))

    fig.update_layout(
        title='Lap Time Comparison',
        xaxis_title='Lap Number',
        yaxis_title='Lap Time (s)',
        height=500
    )

    return fig


def plot_stint_strategy(stints, driver_code):
    """Visualize tyre stints as horizontal bars."""
    colors = {
        'Soft': 'red',
        'Medium': 'yellow',
        'Hard': 'white',
        'Intermediate': 'green',
        'Wet': 'blue'
    }

    fig = go.Figure()

    for _, row in stints.iterrows():
        fig.add_trace(go.Bar(
            x=[row['EndLap'] - row['StartLap'] + 1],
            y=[driver_code],
            base=[row['StartLap']],
            orientation='h',
            marker=dict(color=colors.get(row['Compound'], 'gray')),
            name=row['Compound'],
            hovertext=f"{row['Compound']} | Laps {row['StartLap']}-{row['EndLap']}"
        ))

    fig.update_layout(
        title=f"{driver_code} Tyre Stint Strategy",
        xaxis_title='Lap',
        barmode='stack',
        showlegend=False,
        height=200
    )
    return fig

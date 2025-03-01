import pandas as pd
import plotly.express as px

# Function to create a horizontal bar graph for any categorical column
def create_horizontal_bar_plot(dataframe, column_name):
    df_plot = dataframe[column_name].value_counts().reset_index()
    df_plot.columns = [column_name.replace('_', ' ').title(), 'Count']
    df_plot = df_plot.sort_values('Count', ascending=True)

    fig = px.bar(
        df_plot,
        x='Count',
        y=column_name.replace('_', ' ').title(),
        title=f'Distribution of {column_name.replace("_", " ").title()}',
        labels={'Count': 'Count', column_name.replace('_', ' ').title(): column_name.replace('_', ' ').title()},
        orientation='h',
        color_discrete_sequence=['skyblue']  # Use plain sky blue color
    )

    fig.update_layout(
        template='plotly_white',
        title_font_size=16,
        xaxis_title='Count',
        yaxis_title=column_name.replace('_', ' ').title(),
        height=400,
        width=1200
    )

    fig.show()

# Function to create a box plot for any numeric column
def create_box_plot(dataframe, column_name):
    fig = px.box(
        dataframe,
        x=column_name,
        title=f'Box Plot Distribution of {column_name.title()} Amounts',
        labels={column_name: f'{column_name.title()} Amount'},
        color_discrete_sequence=['skyblue']  # Use plain sky blue color
    )
    fig.update_layout(
        yaxis_title=f'{column_name.title()} Amount',
        template='plotly_white',
        height=400,
        width=1200
    )
    fig.show()

# Function to create a horizontal bar graph for aggregated high values
def create_high_value_bar_plot(dataframe, column_name, aggregation_column, quantile=0.75):
    high_value_threshold = dataframe[aggregation_column].quantile(quantile)

    filtered_df = dataframe[dataframe[aggregation_column] >= high_value_threshold]

    grouped_df = filtered_df.groupby(column_name, as_index=False).agg({
        aggregation_column: 'sum'
    })

    grouped_df = grouped_df.sort_values(aggregation_column, ascending=False).round(2)

    fig = px.bar(
        grouped_df,
        x=aggregation_column,
        y=column_name,
        title=f'High {aggregation_column.title()} by {column_name.title()}',
        labels={column_name: column_name.replace('_', ' ').title(), aggregation_column: aggregation_column.replace('_', ' ').title()},
        orientation='h',
        color_discrete_sequence=['skyblue']  # Use plain sky blue color
    )

    fig.update_layout(
        xaxis_title=aggregation_column.replace('_', ' ').title(),
        yaxis_title=column_name.replace('_', ' ').title(),
        template='plotly_white',
        height=600,
        width=1600
    )

    fig.show()

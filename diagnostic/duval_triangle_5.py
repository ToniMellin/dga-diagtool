# %%
import numpy as np
from pandas import isna
import plotly.graph_objects as go   # plotly is an interactive plotting library

def create_duval_5_colorized():
    # https://community.plotly.com/t/shapes-in-ternary-plot/38566/10
    # https://plotly.com/python/reference/layout/ternary/
    fig = go.Figure(layout=dict(ternary_sum=100))
    #O
    fig.add_trace(go.Scatterternary(a= [0, 0, 36, 46, 0],
                                    b= [100, 90, 54, 54, 100],
                                    c= [0, 10, 10, 0, 0],
                                    name='O',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5,
                                    fill='toself',
                                    fillcolor='rgba(255,211,37, 0.5)'
                                    ))
    #S
    fig.add_trace(go.Scatterternary(a= [46, 36, 76, 86, 46],
                                    b= [54, 54, 14, 14, 54],
                                    c= [0, 10, 10, 0, 0],
                                    name='S',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5,
                                    fill='toself',
                                    fillcolor='rgba(170,156,192, 0.5)'
                                    ))
    #O-2
    fig.add_trace(go.Scatterternary(a= [85, 76, 90, 100, 98, 97, 85, 85],
                                    b= [14, 14, 0, 0, 2, 2, 14, 14],
                                    c= [1, 10, 10, 0, 0, 1, 1, 1],
                                    name='O',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5,
                                    fill='toself',
                                    fillcolor='rgba(255,211,37, 0.5)'
                                    ))
    
    #PD
    fig.add_trace(go.Scatterternary(a= [86, 85, 97, 98, 86],
                                    b= [14, 14, 2, 2, 14],
                                    c= [0, 1, 1, 0, 0],
                                    name='PD',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5,
                                    fill='toself',
                                    fillcolor='rgba(178,255,228, 0.5)'
                                    ))
    #T2-H
    fig.add_trace(go.Scatterternary(a= [90, 78, 53, 65, 90],
                                    b= [0, 12, 12, 0, 0],
                                    c= [10, 10, 35, 35, 10],
                                    name='T2-H',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5,
                                    fill='toself',
                                    fillcolor='rgba(245, 148, 39, 0.5)'
                                    ))
    #C
    fig.add_trace(go.Scatterternary(a= [78, 60, 0, 16, 36, 38, 78],
                                    b= [12, 30, 30, 14, 14, 12, 12],
                                    c= [10, 10, 70, 70, 50, 50, 10],
                                    name='C',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5,
                                    fill='toself',
                                    fillcolor='rgba(92,81,75, 0.6)'
                                    ))
    
    #T3-H
    fig.add_trace(go.Scatterternary(a= [0, 0, 35, 0],
                                    b= [65, 30, 30, 65],
                                    c= [35, 70, 35, 35],
                                    name='T3-H',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5,
                                    fill='toself',
                                    fillcolor='rgba(245, 54, 39, 0.5)'
                                    ))
    #T3-H-2
    fig.add_trace(go.Scatterternary(a= [0, 0, 65, 53, 38, 36, 16],
                                    b= [30, 0, 0, 12, 12, 14, 14],
                                    c= [70, 100, 35, 35, 50, 50, 70 ],
                                    name='T3-H',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5,
                                    fill='toself',
                                    fillcolor='rgba(245, 54, 39, 0.5)'
                                    ))
    fig.add_scatterternary(a=[25, 65, 90, 49, 73, 13, 13], b=[70, 30, 5, 21, 6, 40.5, 9], c=[5, 5, 5, 30, 21, 45.5, 78],
                            mode='text', text=['O', 'S', 'O', 'C', 'T2-H', 'T3-H', 'T3-H'], hoverinfo='none', showlegend=False)
    fig.add_scatterternary(a=[91.5], b=[8], c=[0.5],
                            mode='text', text=['PD'], hoverinfo='none',
                            showlegend=False)
    
    """
    # https://plotly.com/python/text-and-annotations/
    # arrow annotations
    fig.add_annotation(x=0.50, y=0.85,
                text="PD",
                showarrow=True,
                xref='paper',
                yref='paper',
                xanchor='center',
                yanchor='middle',
                ax=40,
                ay=-10,
                arrowhead=1)
    fig.add_annotation(x=0.535, y=0.78,
                text="T1",
                showarrow=True,
                xref='paper',
                yref='paper',
                xanchor='center',
                yanchor='middle',
                ax=40,
                ay=-10,
                arrowhead=1)
    fig.add_annotation(x=0.665, y=0.60,
                text="T2",
                showarrow=True,
                xref='paper',
                yref='paper',
                xanchor='center',
                yanchor='middle',
                ax=40,
                ay=-10,
                arrowhead=1)
    """
    fig.update_ternaries(bgcolor='#FFFFFF', 
                        aaxis=dict(linecolor='#000000', hoverformat='CH4=%%{a}<br>C2H6=%%{b}<br>C2H4=%%{b}<extra></extra>'), 
                        baxis=dict(linecolor='#000000', hoverformat='CH4=%%{a}<br>C2H6=%%{b}<br>C2H4=%%{b}<extra></extra>'), 
                        caxis=dict(linecolor='#000000', hoverformat='CH4=%%{a}<br>C2H6=%%{b}<br>C2H4=%%{b}<extra></extra>'),
                        aaxis_title_text='CH4',
                        baxis_title_text='C2H6',
                        caxis_title_text='C2H4')
    #fig.update_traces(hovertemplate='CH4: %{a}<br>C2H6: %{b}<br>C2H4: %{c}<extra></extra>')
    
    return fig

def create_duval_5_nocolor():
    # https://community.plotly.com/t/shapes-in-ternary-plot/38566/10
    # https://plotly.com/python/reference/layout/ternary/
    fig = go.Figure(layout=dict(ternary_sum=100))
    #O
    fig.add_trace(go.Scatterternary(a= [0, 0, 36, 46, 0],
                                    b= [100, 90, 54, 54, 100],
                                    c= [0, 10, 10, 0, 0],
                                    name='O',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))
    #S
    fig.add_trace(go.Scatterternary(a= [46, 36, 76, 86, 46],
                                    b= [54, 54, 14, 14, 54],
                                    c= [0, 10, 10, 0, 0],
                                    name='S',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))
    #O-2
    fig.add_trace(go.Scatterternary(a= [85, 76, 90, 100, 98, 97, 85, 85],
                                    b= [14, 14, 0, 0, 2, 2, 14, 14],
                                    c= [1, 10, 10, 0, 0, 1, 1, 1],
                                    name='O',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))
    #PD
    fig.add_trace(go.Scatterternary(a= [86, 85, 97, 98, 86],
                                    b= [14, 14, 2, 2, 14],
                                    c= [0, 1, 1, 0, 0],
                                    name='PD',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))
    #T2-H
    fig.add_trace(go.Scatterternary(a= [90, 78, 53, 65, 90],
                                    b= [0, 12, 12, 0, 0],
                                    c= [10, 10, 35, 35, 10],
                                    name='T2-H',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))
    #C
    fig.add_trace(go.Scatterternary(a= [78, 60, 0, 16, 36, 38, 78],
                                    b= [12, 30, 30, 14, 14, 12, 12],
                                    c= [10, 10, 70, 70, 50, 50, 10],
                                    name='C',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))
    #T3-H
    fig.add_trace(go.Scatterternary(a= [0, 0, 35, 0],
                                    b= [65, 30, 30, 65],
                                    c= [35, 70, 35, 35],
                                    name='T3-H',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))
    #T3-H
    fig.add_trace(go.Scatterternary(a= [0, 0, 65, 53, 38, 36, 16],
                                    b= [30, 0, 0, 12, 12, 14, 14],
                                    c= [70, 100, 35, 35, 50, 50, 70 ],
                                    name='T3-H',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))
    fig.add_scatterternary(a=[25, 65, 90, 49, 73, 13, 13], b=[70, 30, 5, 21, 6, 40.5, 9], c=[5, 5, 5, 30, 21, 45.5, 78],
                            mode='text', text=['O', 'S', 'O', 'C', 'T2-H', 'T3-H', 'T3-H'], hoverinfo='skip',
                            showlegend=False)
    fig.add_scatterternary(a=[91.5], b=[8], c=[0.5],
                            mode='text', text=['PD'], hoverinfo='skip',
                            showlegend=False)
    
    """
    # https://plotly.com/python/text-and-annotations/
    # arrow annotations
    fig.add_annotation(x=0.50, y=0.99,
                text="PD",
                showarrow=True,
                ax=40,
                ay=-10,
                arrowhead=1)
    fig.add_annotation(x=0.525, y=0.90,
                text="T1",
                showarrow=True,
                ax=40,
                ay=-10,
                arrowhead=1)
    fig.add_annotation(x=0.643, y=0.65,
                text="T2",
                showarrow=True,
                ax=40,
                ay=-10,
                arrowhead=1)
    """
    fig.update_ternaries(bgcolor='#FFFFFF', 
                        aaxis=dict(linecolor='#000000', hoverformat='CH4=%%{a}<br>C2H6=%%{b}<br>C2H4=%%{b}<extra></extra>'), 
                        baxis=dict(linecolor='#000000', hoverformat='CH4=%%{a}<br>C2H6=%%{b}<br>C2H4=%%{b}<extra></extra>'), 
                        caxis=dict(linecolor='#000000', hoverformat='CH4=%%{a}<br>C2H6=%%{b}<br>C2H4=%%{b}<extra></extra>'),
                        aaxis_title_text='CH4',
                        baxis_title_text='C2H6',
                        caxis_title_text='C2H4')
    #fig.update_traces(hovertemplate='CH4: %{a:.2f}<br>C2H6: %{b:.2f}<br>C2H4: %{c:.2f}<extra></extra>')
    
    return fig

def round_half_up(n, decimals=0):
    # rounding values
    multiplier = 10 ** decimals
    return np.floor(n*multiplier + 0.5) / multiplier

def calculate_duval_5_coordinates(ch4, c2h6, c2h4):

    i = ch4
    j = c2h6
    k = c2h4

    x = (i / (i + j + k))*100
    y = (j / (i + j + k))*100
    z = (k / (i + j + k))*100
    coordinates = round_half_up(np.array([x, y, z]), 2)

    return coordinates

def calculate_duval_5_result(ch4, c2h6, c2h4):
    try:
        if (isna(ch4) is True) or (isna(c2h6) is True) or (isna(c2h4) is True):
            return 'N/A'
        else:
            x, y, z = calculate_duval_5_coordinates(ch4, c2h6, c2h4)
            if z <= 1 and y >= 2 and y <= 14:
                return 'PD'
            elif (z > 1 and z <10 and y >= 2 and y <= 14) or (z < 1 and y < 2) or (z < 10 and y >= 54):
                return 'O'
            elif z < 10 and y >= 14 and y < 54:
                return 'S'
            elif z >= 10 and z <= 35 and y <= 12:
                return 'T2-H'
            elif (z > 35 and y <= 12) or (z >= 49 and y >= 12 and y <= 14) or (z > 70 and y >= 14) or (z >= 35 and y >= 30):
                return 'T3-H'
            elif (z >= 10 and z < 50 and y  > 12 and y <= 14) or (z >= 10 and z <= 70 and y > 14 and y < 30):
                return 'C'
            elif z >= 10 and z < 35 and y >= 30:
                return 'ND'
            else:
                return 'ND'
    except TypeError:
        print('Duval result calculation error!')
        print('{ch4}, {c2h6}, {c2h4}')
        return 'N/A'
    
def create_duval_5_marker(ch4, c2h6, c2h4, marker_name):
    mark_coordinates = calculate_duval_5_coordinates(ch4, c2h6, c2h4)
    return go.Scatterternary(       a= [mark_coordinates[0]],
                                    b= [mark_coordinates[1]],
                                    c= [mark_coordinates[2]],
                                    name= marker_name,
                                    hovertemplate='CH4: %{a:.2f}<br>C2H6: %{b:.2f}<br>C2H4: %{c:.2f}<extra></extra>',
                                    mode='markers',
                                    marker_color='red',
                                    marker_size=10
                                    )

def create_duval_5_result_graph(ch4, c2h6, c2h4):
    fig = create_duval_5_colorized()

    try:
        result_name = calculate_duval_5_result(ch4, c2h6, c2h4)
        fig.add_trace(create_duval_5_marker(ch4, c2h6, c2h4, result_name))
        return fig
    except:
        return fig

# %%
if __name__ == "__main__":
    fig = create_duval_5_nocolor()
    marker_name = calculate_duval_5_result(10, 26, 64)
    fig.add_trace(create_duval_5_marker(10, 26, 64, marker_name))
    fig.show()

    fig2 = create_duval_5_colorized()
    marker_name2 = calculate_duval_5_result(10, 26, 64)
    fig2.add_trace(create_duval_5_marker(10, 26, 64, marker_name2))
    fig2.show()

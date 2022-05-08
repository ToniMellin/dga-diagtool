# %%
import plotly.graph_objects as go   # plotly is an interactive plotting library
import numpy as np
from pandas import isna

def create_duval_4_colorized():
    # https://community.plotly.com/t/shapes-in-ternary-plot/38566/10
    # https://plotly.com/python/reference/layout/ternary/
    fig = go.Figure(layout=dict(ternary_sum=100))
    #O
    fig.add_trace(go.Scatterternary(a= [0, 0, 9, 9, 0],
                                    b= [100, 30, 30, 91, 100],
                                    c= [0, 70, 61, 0, 0],
                                    name='O',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5,
                                    fill='toself',
                                    fillcolor='rgba(255,211,37, 0.5)'
                                    ))
    #C
    fig.add_trace(go.Scatterternary(a= [0, 0, 64, 40, 15, 15, 0],
                                    b= [30, 0, 0, 24, 24, 30, 30],
                                    c= [70, 100, 36, 36, 61, 55, 70],
                                    name='C',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5,
                                    fill='toself',
                                    fillcolor='rgba(92,81,75, 0.6)'
                                    ))
    #PD
    fig.add_trace(go.Scatterternary(a= [98, 97, 84, 85, 98],
                                    b= [0, 1, 1, 0, 0],
                                    c= [2, 2, 15, 15, 2],
                                    name='PD',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5,
                                    fill='toself',
                                    fillcolor='rgba(178,255,228, 0.5)'
                                    ))
    #S
    fig.add_trace(go.Scatterternary(a= [9, 9, 15, 15, 40, 64, 85, 84, 97, 98, 100, 56, 9],
                                    b= [44, 30, 30, 24, 24, 0, 0, 1, 1, 0, 0, 44, 44],
                                    c= [47, 61, 55, 61,  36, 36, 15, 15, 2, 2, 0, 0, 47],
                                    name='S',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5,
                                    fill='toself',
                                    fillcolor='rgba(170,156,192, 0.5)'
                                    ))
    fig.add_scatterternary(a=[4.5, 64, 28], b=[62, 18, 12], c=[33.5, 18, 60],
                            mode='text', text=['O', 'S', 'C'], hoverinfo='none', showlegend=False)
    fig.add_scatterternary(a=[91], b=[0.5], c=[8.5],
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
                        aaxis=dict(linecolor='#000000', hoverformat='H2=%%{a}<br>C2H6=%%{b}<br>CH4=%%{b}<extra></extra>'), 
                        baxis=dict(linecolor='#000000', hoverformat='H2=%%{a}<br>C2H6=%%{b}<br>CH4=%%{b}<extra></extra>'), 
                        caxis=dict(linecolor='#000000', hoverformat='H2=%%{a}<br>C2H6=%%{b}<br>CH4=%%{b}<extra></extra>'),
                        aaxis_title_text='H2',
                        baxis_title_text='C2H6',
                        caxis_title_text='CH4')
    #fig.update_traces(hovertemplate='H2: %{a}<br>C2H6: %{b}<br>CH4: %{c}<extra></extra>')
    
    return fig

def create_duval_4_nocolor():
    # https://community.plotly.com/t/shapes-in-ternary-plot/38566/10
    # https://plotly.com/python/reference/layout/ternary/
    fig = go.Figure(layout=dict(ternary_sum=100))
    #O
    fig.add_trace(go.Scatterternary(a= [0, 0, 9, 9, 0],
                                    b= [100, 30, 30, 91, 100],
                                    c= [0, 70, 61, 0, 0],
                                    name='O',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))
    #C
    fig.add_trace(go.Scatterternary(a= [0, 0, 64, 40, 15, 15, 0],
                                    b= [30, 0, 0, 24, 24, 30, 30],
                                    c= [70, 100, 36, 36, 61, 55, 70],
                                    name='C',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))
    #PD
    fig.add_trace(go.Scatterternary(a= [98, 97, 84, 85, 98],
                                    b= [0, 1, 1, 0, 0],
                                    c= [2, 2, 15, 15, 2],
                                    name='PD',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))
    #S
    fig.add_trace(go.Scatterternary(a= [9, 9, 15, 15, 40, 64, 85, 84, 97, 98, 100, 56, 9],
                                    b= [44, 30, 30, 24, 24, 0, 0, 1, 1, 0, 0, 44, 44],
                                    c= [47, 61, 55, 61,  36, 36, 15, 15, 2, 2, 0, 0, 47],
                                    name='S',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))

    fig.add_scatterternary(a=[4.5, 64, 28], b=[62, 18, 12], c=[33.5, 18, 60],
                            mode='text', text=['O', 'S', 'C'], hoverinfo='skip',
                            showlegend=False)
    fig.add_scatterternary(a=[91], b=[0.5], c=[8.5],
                            mode='text', text=['PD'], hoverinfo='skip',
                            showlegend=False)
    
    """
    # https://plotly.com/python/text-and-annotations/
    # arrow annotations
    fig.add_annotation(x=0.54, y=0.85,
                text="PD",
                showarrow=True,
                ax=40,
                ay=-10,
                arrowhead=1)
    """
    fig.update_ternaries(bgcolor='#FFFFFF', 
                        aaxis=dict(linecolor='#000000', hoverformat='H2=%%{a}<br>C2H6=%%{b}<br>CH4=%%{b}<extra></extra>'), 
                        baxis=dict(linecolor='#000000', hoverformat='H2=%%{a}<br>C2H6=%%{b}<br>CH4=%%{b}<extra></extra>'), 
                        caxis=dict(linecolor='#000000', hoverformat='H2=%%{a}<br>C2H6=%%{b}<br>CH4=%%{b}<extra></extra>'),
                        aaxis_title_text='H2',
                        baxis_title_text='C2H6',
                        caxis_title_text='CH4')
    #fig.update_traces(hovertemplate='CH4: %{a:.2f}<br>C2H2: %{b:.2f}<br>C2H4: %{c:.2f}<extra></extra>')
    
    return fig

def calculate_duval_4_coordinates(h2, c2h6, ch4):

    i = h2
    j = c2h6
    k = ch4

    x = (i / (i + j + k))*100
    y = (j / (i + j + k))*100
    z = (k / (i + j + k))*100
    coordinates = np.array([x, y, z])

    return coordinates

def calculate_duval_4_result(h2, c2h6, ch4):
    try:
        if (isna(h2) is True) or (isna(c2h6) is True) or (isna(ch4) is True):
            return 'N/A'
        else:
            x, y, z = calculate_duval_4_coordinates(h2, c2h6, ch4)
            if z >= 2 and z < 15 and y < 1:
                return 'PD'
            elif (x >= 9 and y >= 30 and y < 46) or (x >= 15 and y >= 24 and y < 30) or (z < 36 and y >= 1 and y < 24) or (z < 36 and z >= 15 and y < 1) or (z < 2 and y < 1):
                return 'S'
            elif x < 9 and y >= 30:
                return 'O'
            elif (z >= 36 and y <= 24) or (x < 15 and y >= 24 and y < 30):
                return 'C'
            elif (x >= 9 and y >= 46):
                return 'ND'
            else:
                return 'ND'
    except TypeError:
        print('Duval result calculation error!')
        print('{h2}, {c2h6}, {ch4}')
        return 'N/A'
    
def create_duval_4_marker(h2, c2h6, ch4, marker_name):
    mark_coordinates = calculate_duval_4_coordinates(h2, c2h6, ch4)
    return go.Scatterternary(       a= [mark_coordinates[0]],
                                    b= [mark_coordinates[1]],
                                    c= [mark_coordinates[2]],
                                    name= marker_name,
                                    hovertemplate='H2: %{a:.2f}<br>C2H6: %{b:.2f}<br>CH4: %{c:.2f}<extra></extra>',
                                    mode='markers',
                                    marker_color='red',
                                    marker_size=10
                                    )

def create_duval_4_result_graph(h2, c2h6, ch4):
    fig = create_duval_4_colorized()

    try:
        result_name = calculate_duval_4_result(h2, c2h6, ch4)
        fig.add_trace(create_duval_4_marker(h2, c2h6, ch4, result_name))
        return fig
    except:
        return fig

# %%
if __name__ == "__main__":
    fig = create_duval_4_nocolor()
    marker_name = calculate_duval_4_result(10, 26, 64)
    fig.add_trace(create_duval_4_marker(10, 26, 64, marker_name))
    fig.show()

    fig2 = create_duval_4_colorized()
    marker_name2 = calculate_duval_4_result(10, 26, 64)
    fig2.add_trace(create_duval_4_marker(10, 26, 64, marker_name2))
    fig2.show()
# %%

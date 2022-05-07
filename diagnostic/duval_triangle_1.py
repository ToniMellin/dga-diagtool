# %%
import plotly.graph_objects as go   # plotly is an interactive plotting library
import numpy as np
from pandas import isna

def create_duval_1_colorized():
    # https://community.plotly.com/t/shapes-in-ternary-plot/38566/10
    # https://plotly.com/python/reference/layout/ternary/
    fig = go.Figure(layout=dict(ternary_sum=100))
    #D1
    fig.add_trace(go.Scatterternary(a= [0, 0, 64, 87, 0],
                                    b= [100, 77, 13, 13, 100],
                                    c= [0, 23, 23, 0, 0],
                                    name='D1',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5,
                                    fill='toself',
                                    fillcolor='rgba(178,244,255, 0.5)'
                                    ))
    #D2
    fig.add_trace(go.Scatterternary(a= [64, 0, 0, 31, 47, 64],
                                    b= [13, 77, 29, 29, 13, 13],
                                    c= [23, 23, 71, 40, 40, 23],
                                    name='D2',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5,
                                    fill='toself',
                                    fillcolor='rgba(178,205,255, 0.5)'
                                    ))
    #DT
    fig.add_trace(go.Scatterternary(a= [87, 47, 31, 0, 0, 35, 46, 96, 87],
                                    b= [13, 13, 29, 29, 15, 15, 4, 4, 13],
                                    c= [0, 40, 40, 71, 85, 50, 50, 0, 0],
                                    name='DT',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5,
                                    fill='toself',
                                    fillcolor='rgba(228,178,255, 0.5)'
                                    ))
    #PD
    fig.add_trace(go.Scatterternary(a= [100, 98, 98],
                                    b= [0, 2, 0],
                                    c= [0, 0, 2],
                                    name='PD',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5,
                                    fill='toself',
                                    fillcolor='rgba(178,255,228, 0.5)'
                                    ))
    #T1
    fig.add_trace(go.Scatterternary(a= [96, 76, 80, 98, 98, 96],
                                    b= [4, 4, 0, 0, 2, 4],
                                    c= [0, 20, 20, 2, 0, 0],
                                    name='T1',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5,
                                    fill='toself',
                                    fillcolor='rgba(245, 243, 39, 0.5)'
                                    ))
    #T2
    fig.add_trace(go.Scatterternary(a= [80, 76, 46, 50, 80],
                                    b= [0, 4, 4, 0, 0],
                                    c= [20, 20, 50, 50, 20],
                                    name='T2',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5,
                                    fill='toself',
                                    fillcolor='rgba(245, 148, 39, 0.5)'
                                    ))
    #T3
    fig.add_trace(go.Scatterternary(a= [50, 35, 0, 0, 50],
                                    b= [0, 15, 15, 0, 0],
                                    c= [50, 50, 85, 100, 50],
                                    name='T3',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5,
                                    fill='toself',
                                    fillcolor='rgba(245, 54, 39, 0.5)'
                                    ))
    fig.add_scatterternary(a=[20, 20, 20, 20], b=[68.5, 42.5, 22, 7.5], c=[11.5, 37.5, 58, 72.5],
                            mode='text', text=['D1', 'D2', 'DT', 'T3'], hoverinfo='none', showlegend=False)
    fig.add_scatterternary(a=[99, 88, 63], b=[0.5, 2, 2], c=[0.5, 10, 35],
                            mode='text', text=['PD', 'T1', 'T2'], hoverinfo='none',
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
                        aaxis=dict(linecolor='#000000', hoverformat='CH4=%%{a}<br>C2H2=%%{b}<br>C2H4=%%{b}<extra></extra>'), 
                        baxis=dict(linecolor='#000000', hoverformat='CH4=%%{a}<br>C2H2=%%{b}<br>C2H4=%%{b}<extra></extra>'), 
                        caxis=dict(linecolor='#000000', hoverformat='CH4=%%{a}<br>C2H2=%%{b}<br>C2H4=%%{b}<extra></extra>'),
                        aaxis_title_text='CH4',
                        baxis_title_text='C2H2',
                        caxis_title_text='C2H4')
    #fig.update_traces(hovertemplate='CH4: %{a}<br>C2H2: %{b}<br>C2H4: %{c}<extra></extra>')
    
    return fig

def create_duval_1_nocolor():
    # https://community.plotly.com/t/shapes-in-ternary-plot/38566/10
    # https://plotly.com/python/reference/layout/ternary/
    fig = go.Figure(layout=dict(ternary_sum=100))
    #D1
    fig.add_trace(go.Scatterternary(a= [0, 0, 64, 87, 0],
                                    b= [100, 77, 13, 13, 100],
                                    c= [0, 23, 23, 0, 0],
                                    name='D1',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))
    #D2
    fig.add_trace(go.Scatterternary(a= [64, 0, 0, 31, 47, 64],
                                    b= [13, 77, 29, 29, 13, 13],
                                    c= [23, 23, 71, 40, 40, 23],
                                    name='D2',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))
    #DT
    fig.add_trace(go.Scatterternary(a= [87, 47, 31, 0, 0, 35, 46, 96, 87],
                                    b= [13, 13, 29, 29, 15, 15, 4, 4, 13],
                                    c= [0, 40, 40, 71, 85, 50, 50, 0, 0],
                                    name='DT',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))
    #PD
    fig.add_trace(go.Scatterternary(a= [100, 98, 98],
                                    b= [0, 2, 0],
                                    c= [0, 0, 2],
                                    name='PD',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))
    #T1
    fig.add_trace(go.Scatterternary(a= [96, 76, 80, 98, 98, 96],
                                    b= [4, 4, 0, 0, 2, 4],
                                    c= [0, 20, 20, 2, 0, 0],
                                    name='T1',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))
    #T2
    fig.add_trace(go.Scatterternary(a= [80, 76, 46, 50, 80],
                                    b= [0, 4, 4, 0, 0],
                                    c= [20, 20, 50, 50, 20],
                                    name='T2',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))
    #T3
    fig.add_trace(go.Scatterternary(a= [50, 35, 0, 0, 50],
                                    b= [0, 15, 15, 0, 0],
                                    c= [50, 50, 85, 100, 50],
                                    name='T3',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))
    fig.add_scatterternary(a=[20, 20, 20, 20], b=[68.5, 42.5, 22, 7.5], c=[11.5, 37.5, 58, 72.5],
                            mode='text', text=['D1', 'D2', 'DT', 'T3'], hoverinfo='skip',
                            showlegend=False)
    fig.add_scatterternary(a=[99, 88, 63], b=[0.5, 2, 2], c=[0.5, 10, 35],
                            mode='text', text=['PD', 'T1', 'T2'], hoverinfo='skip',
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
                        aaxis=dict(linecolor='#000000', hoverformat='CH4=%%{a}<br>C2H2=%%{b}<br>C2H4=%%{b}<extra></extra>'), 
                        baxis=dict(linecolor='#000000', hoverformat='CH4=%%{a}<br>C2H2=%%{b}<br>C2H4=%%{b}<extra></extra>'), 
                        caxis=dict(linecolor='#000000', hoverformat='CH4=%%{a}<br>C2H2=%%{b}<br>C2H4=%%{b}<extra></extra>'),
                        aaxis_title_text='CH4',
                        baxis_title_text='C2H2',
                        caxis_title_text='C2H4')
    #fig.update_traces(hovertemplate='CH4: %{a:.2f}<br>C2H2: %{b:.2f}<br>C2H4: %{c:.2f}<extra></extra>')
    
    return fig

def calculate_duval_1_coordinates(ch4, c2h2, c2h4):

    i = ch4
    j = c2h2
    k = c2h4

    x = (i / (i + j + k))*100
    y = (j / (i + j + k))*100
    z = (k / (i + j + k))*100
    coordinates = np.array([x, y, z])

    return coordinates

def calculate_duval_1_result(ch4, c2h2, c2h4):
    try:
        if (isna(ch4) is True) or (isna(c2h2) is True) or (isna(c2h4) is True):
            return 'N/A'
        else:
            x, y, z = calculate_duval_1_coordinates(ch4, c2h2, c2h4)
            if x >= 98:
                return 'PD'
            elif y < 4 and z < 20 and x < 98:
                return 'T1'
            elif y < 4 and z >= 20 and z < 50:
                return 'T2'
            elif y < 15 and z >= 50:
                return 'T3'
            elif (z < 50 and y >= 4 and y < 13 ) or (z >= 40 and z < 50 and y >= 13 and y < 29) or (z >= 50 and y >= 15 and y < 29):
                return 'DT'
            elif z < 23 and y >= 13:
                return 'D1'
            elif (z >= 23 and y >= 29) or (z < 40 and z >= 23 and y < 29 and y >=13):
                return 'D2'
            else:
                return 'ND'
    except TypeError:
        print('Duval result calculation error!')
        print('{ch4}, {c2h2}, {c2h4}')
        return 'N/A'
    
def create_duval_1_marker(ch4, c2h2, c2h4, marker_name):
    mark_coordinates = calculate_duval_1_coordinates(ch4, c2h2, c2h4)
    return go.Scatterternary(       a= [mark_coordinates[0]],
                                    b= [mark_coordinates[1]],
                                    c= [mark_coordinates[2]],
                                    name= marker_name,
                                    hovertemplate='CH4: %{a:.2f}<br>C2H2: %{b:.2f}<br>C2H4: %{c:.2f}<extra></extra>',
                                    mode='markers',
                                    marker_color='red',
                                    marker_size=10
                                    )

def create_duval_1_result_graph(ch4, c2h2, c2h4):
    fig = create_duval_1_colorized()

    try:
        result_name = calculate_duval_1_result(ch4, c2h2, c2h4)
        fig.add_trace(create_duval_1_marker(ch4, c2h2, c2h4, result_name))
        return fig
    except:
        return fig

# %%
if __name__ == "__main__":
    fig = create_duval_1_nocolor()
    mark1 = calculate_duval_1_coordinates(50, 50, 100)
    fig.add_trace(go.Scatterternary(a= [mark1[0]],
                                    b= [mark1[1]],
                                    c= [mark1[2]],
                                    name='marker1',
                                    hovertemplate='CH4: %{a:.2f}<br>C2H2: %{b:.2f}<br>C2H4: %{c:.2f}<extra></extra>',
                                    mode='markers',
                                    marker_color='red',
                                    marker_size=8
                                    ))
    fig.show()

    fig2 = create_duval_1_colorized()
    mark1 = calculate_duval_1_coordinates(50, 50, 100)
    fig2.add_trace(go.Scatterternary(a= [mark1[0]],
                                    b= [mark1[1]],
                                    c= [mark1[2]],
                                    name='marker1',
                                    hovertemplate='CH4: %{a:.2f}<br>C2H2: %{b:.2f}<br>C2H4: %{c:.2f}<extra></extra>',
                                    mode='markers',
                                    marker_color='red',
                                    marker_size=8
                                    ))
    fig2.show()
# %%

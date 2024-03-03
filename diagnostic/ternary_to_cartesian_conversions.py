# -*- coding: utf-8 -*-
"""ternary_to_cartesian_conversions.py

This module makes ternary coordinate conversions to cartesian coordinates

@Author: https://github.com/ToniMellin

* Copyright (C) 2023-2024 Toni Mellin - All Rights Reserved
* You may use, distribute and modify this code under the
* terms of the MIT license.
*
* See file LICENSE or go to 
* https://github.com/ToniMellin/dga-diagtool/blob/master/LICENSE 
* for full license details.
"""

# %%
import numpy as np


def round_up(n, decimals=2):
    multiplier = 10 ** decimals
    return np.floor(n * multiplier + 0.5) / multiplier

def ternary_to_cartesian_luc(a, b):
    x = 0.5 * a + b
    y = np.cos(np.pi/6) * a

    return x, y

def ternary_to_cartesian_wolfram(a, b, c):
    # https://mathworld.wolfram.com/TernaryDiagram.html
    x = 0.5 * ((a+2*b) / (a+b+c)) * 100
    y = (np.sqrt(3)/2) * (a / (a+b+c)) * 100

    return x, y

def ternary_to_cartesian_wiki(a, b, c):
    # https://handwiki.org/wiki/Barycentric_coordinate_system
    # https://en.wikipedia.org/wiki/Barycentric_coordinate_system
    x1, x2, x3 = 0.5, 1,  0
    y1, y2, y3 = np.sin(np.pi/3), 0, 0 # alternatively (np.sqrt(3) / 2)

    x = (a * x1) + (b * x2) + (c * x3)
    y = (a * y1) + (b * y2) + (c * y3)

    return x, y
  
def ternary_to_cartesian_wiki_rounded(a, b, c, rounding=2):

    wiki_x, wiki_y = ternary_to_cartesian_wiki(a, b, c)
    print(f'Wiki:\n({wiki_x}, {wiki_y})')
    wiki_x_rounded = round_up(wiki_x, rounding)
    wiki_y_rounded = round_up(wiki_y, rounding)
    print(f'Rounded:\n({wiki_x_rounded}, {wiki_y_rounded})')

    return wiki_x_rounded, wiki_y_rounded

def plotly_ternary_to_cartesian(a, b, c):
    # plotly ternary is counter-clockwise abc, with side a on the left

    x, y = ternary_to_cartesian_wiki(a, c, b)

    return x, y

def cartesian_to_ternary_wiki(x, y):
    # cartesian (x,y) coordinates to ternary (a, b, c) coordinates, with side length 100 and even sided triangle 
    x1, x2, x3 = 0.5, 1,  0
    y1, y2, y3 = np.sin(np.pi/3), 0, 0 # alternatively (np.sqrt(3) / 2)

    a_raw = ((y2-y3)*(x-x3) + (x3-x2)*(y-y3)) / ((y2-y3)*(x1+x3) + (x3-x2)*(y1-y3))
    a = round_up(a_raw, 2)

    b_raw = ((y3-y1)*(x-x3) + (x1-x3)*(y-y3)) / ((y2-y3)*(x1-x3) + (x3-x2)*(y1-y3))
    b = round_up(b_raw, 2)

    # side length 100 
    c = round_up((100 - a - b), 2)

    return a, b, c

def cartesian_to_ternary_plotly(x, y):

    # swap abc to acb as plotly uses counter-clockwise ternary coordinates
    a, c, b = cartesian_to_ternary_wiki(x, y)

    return a, b, c

def plotly_abc_to_clockwise_acb(a, b, c):
    # plotly ternary is counter-clockwise abc, with side a on the left
    
    if (type(a) == int) and (type(b) == int) and (type(c) == int):
        return a, c, b
    elif (type(a) == list) and (type(b) == list) and (type(c) == list):
        assert len(a) == len(b) and len(b) == len(c)

        clockwise_acb = []
        for i in range(0, len(a)):
            clockwise_acb.append((a[i], c[i], b[i]))
        return clockwise_acb
    else:
        raise TypeError('Incorrect format')

def plotly_abc_to_clockwise_acb_print(a, b, c):
    s = plotly_abc_to_clockwise_acb(a, b, c)
    for coord in s:
        print(coord)

    return


# %%
if __name__ == '__main__':
    import plotly.express as px
    import plotly.graph_objects as go
    import plotly.io as pio

    # plotly default theme
    pio.templates["custom_theme"] = go.layout.Template(
        layout=go.Layout(
            colorway=px.colors.qualitative.D3
        )
    )

    pio.templates.default = 'plotly_white+custom_theme'
    import duval_triangle_1
    import duval_triangle_4
    import duval_triangle_5

    def comparison_plots(a, b, c, triangle=1):
        if triangle == 1:
            fig = duval_triangle_1.create_duval_1_colorized()
            fig.add_trace(duval_triangle_1.create_duval_1_marker(a, c, b, marker_name='ternary'))
        elif triangle == 4:
            fig = duval_triangle_4.create_duval_4_colorized()
            fig.add_trace(duval_triangle_4.create_duval_4_marker(a, c, b, marker_name='ternary'))
        elif triangle == 5:
            fig = duval_triangle_5.create_duval_5_colorized()
            fig.add_trace(duval_triangle_5.create_duval_5_marker(a, c, b, marker_name='ternary'))
        else:
            raise ValueError('Incorrect Duval triangle number given!')

        fig.show()

        luc_x, luc_y = ternary_to_cartesian_luc(a, b)
        print(f'Luc:\n({luc_x}, {luc_y})')
        wiki_x, wiki_y = ternary_to_cartesian_wiki(a, b, c)
        print(f'Wiki:\n({wiki_x}, {wiki_y})')
        wiki_x_rounded = round_up(wiki_x, 2)
        wiki_y_rounded = round_up(wiki_y, 2)
        print(f'Rounded:\n({wiki_x_rounded}, {wiki_y_rounded})')

        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=[0, 50], y=[0, 86.6], mode='lines', name='side a', marker_color='black'))
        fig2.add_trace(go.Scatter(x=[50, 100], y=[86.6, 0], mode='lines', name='side b', marker_color='black'))
        fig2.add_trace(go.Scatter(x=[100, 0], y=[0, 0], mode='lines', name='side c', marker_color='black'))
        fig2.add_trace(go.Scatter(x=[luc_x], y=[luc_y], mode='markers', name='Luc conversion', marker_color='red'))
        fig2.add_trace(go.Scatter(x=[wiki_x], y=[wiki_y], mode='markers', name='wiki conversion', marker_color='green'))
        fig2.show()

        return

    comparison_plots(10, 25, 65, 1)

# %%
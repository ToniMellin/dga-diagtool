# -*- coding: utf-8 -*-
"""ternary_uncertainty.py

This module makes duval triangle uncertainty estimation lines.

@Author: https://github.com/ToniMellin

* Copyright (C) 2023 Toni Mellin - All Rights Reserved
* You may use, distribute and modify this code under the
* terms of the MIT license.
*
* See file LICENSE or go to 
* https://github.com/ToniMellin/dga-diagtool/blob/master/LICENSE 
* for full license details.
"""
# %%
import plotly.graph_objects as go   # plotly is an interactive plotting library
import numpy as np

def calculate_ternany_uncertainty_lines(a, b, c , uncertainty_list):
    """
      1
     / \\
    2    6
    |    |
    3    5
    \\  /
      4

    1: MaxMinMin
    2: MaxMaxMin
    3: MinMaxMin
    4: MinMaxMax
    5: MinMinMax
    6: MaxMinMax
    7: Copy 1
    """

    if len(uncertainty_list) == 1:
        uncertainty = uncertainty_list[0]

        unc = np.array([[(1+uncertainty), (1-uncertainty), (1-uncertainty)],
        [(1+uncertainty), (1+uncertainty), (1-uncertainty)],
        [(1-uncertainty), (1+uncertainty), (1-uncertainty)],
        [(1-uncertainty), (1+uncertainty), (1+uncertainty)],
        [(1-uncertainty), (1-uncertainty), (1+uncertainty)],
        [(1+uncertainty), (1-uncertainty), (1+uncertainty)],
        [(1+uncertainty), (1-uncertainty), (1-uncertainty)]
        ])

    elif len(uncertainty) == 3:
        unc = np.array([[(1+uncertainty_list[0]), (1-uncertainty_list[1]), (1-uncertainty_list[2])],
                  [(1+uncertainty_list[0]), (1+uncertainty_list[1]), (1-uncertainty_list[2])],
                  [(1-uncertainty_list[0]), (1+uncertainty_list[1]), (1-uncertainty_list[2])],
                  [(1-uncertainty_list[0]), (1+uncertainty_list[1]), (1+uncertainty_list[2])],
                  [(1-uncertainty_list[0]), (1-uncertainty_list[1]), (1+uncertainty_list[2])],
                  [(1+uncertainty_list[0]), (1-uncertainty_list[1]), (1+uncertainty_list[2])],
                  [(1+uncertainty_list[0]), (1-uncertainty_list[1]), (1-uncertainty_list[2])]
                  ])
    else:
        raise Exception('Uncertainty list has to have length 1 or 3!')

    unc_lines = unc.copy()

    for r, row in enumerate(unc_lines):
        i = row[0]*a
        j = row[1]*b
        k = row[2]*c

        x = (i / (i + j + k))*100
        y = (j / (i + j + k))*100
        z = (k / (i + j + k))*100
        unc_lines[r, :] = np.array([x, y, z])

    return unc_lines

def add_ternary_uncertainty_lines(figure, points_and_uncertainties, colors):
    if len(points_and_uncertainties) != len(colors):
        raise Exception('Mismatch between given amount of points and color list!')
    
    a_text = figure['layout']['ternary']['aaxis']['title']['text']
    b_text = figure['layout']['ternary']['baxis']['title']['text']
    print(a_text)
    print(b_text)
    
    if a_text == 'H2':
        hover_t = 'H2: %{a:.2f}%<br>C2H6: %{b:.2f}%<br>CH4: %{c:.2f}%<extra></extra>'
    elif a_text == 'CH4':
        if b_text == 'C2H2':
            hover_t = 'CH4: %{a:.2f}%<br>C2H2: %{b:.2f}%<br>C2H4: %{c:.2f}%<extra></extra>'
        elif b_text == 'C2H6':
            hover_t = 'CH4: %{a:.2f}%<br>C2H6: %{b:.2f}%<br>C2H4: %{c:.2f}%<extra></extra>'

    # https://plotly.com/python/shapes/
    for point_and_uncertainty, color in zip(points_and_uncertainties, colors):
        uncertainty_line = calculate_ternany_uncertainty_lines(point_and_uncertainty[0], point_and_uncertainty[1], point_and_uncertainty[2], point_and_uncertainty[3])
        figure.add_trace(go.Scatterternary(a= uncertainty_line[:, 0],
                                    b= uncertainty_line[:, 1],
                                    c= uncertainty_line[:, 2], 
                                    mode='lines',
                                    hovertemplate=hover_t,
                                    line_color=color,
                                    line_width=0.5
                                    ))

    return figure


# %%
if __name__ == '__main__':
    import duval_triangle_1
    import duval_triangle_4
    import duval_triangle_5

    test_point = [[100, 100, 100, [0.15]],
                  [100, 100, 100, [0.3]],
                  [90, 8, 105, [0.15]],
                  [90, 8, 105, [0.3]],
                  [90, 20, 30, [0.15]],
                  [90, 20, 30, [0.3]],
                  [100, 10, 8, [0.15]],
                  [100, 10, 8, [0.3]],
                  [10, 20, 80, [0.15]],
                  [10, 20, 80, [0.3]]]
    
    test_point2 = [[100, 100, 100, [0.15]],
                  [100, 100, 100, [0.3]]]

    fig = duval_triangle_1.create_duval_1_nocolor()
    marker_name = duval_triangle_1.calculate_duval_1_result(100, 100, 100)
    fig.add_trace(duval_triangle_1.create_duval_1_marker(100, 100, 100, marker_name, marker_color='green'))
    fig.add_trace(duval_triangle_1.create_duval_1_marker(90, 8, 105, marker_name, marker_color='green'))
    fig.add_trace(duval_triangle_1.create_duval_1_marker(90, 20, 30, marker_name, marker_color='green'))
    fig.add_trace(duval_triangle_1.create_duval_1_marker(100, 10, 8, marker_name, marker_color='green'))
    fig.add_trace(duval_triangle_1.create_duval_1_marker(10, 20, 80, marker_name, marker_color='green'))
    fig = add_ternary_uncertainty_lines(fig, test_point, ['blue', 'red', 'blue', 'red', 'blue', 'red', 'blue', 'red', 'blue', 'red'])
    fig.show()

    
    fig4 = duval_triangle_4.create_duval_4_nocolor()
    marker_name = duval_triangle_4.calculate_duval_4_result(100, 100, 100)
    fig4.add_trace(duval_triangle_4.create_duval_4_marker(100, 100, 100, marker_name, marker_color='green'))
    fig4 = add_ternary_uncertainty_lines(fig4, test_point2, ['blue', 'red'])
    fig4.show()

    fig5 = duval_triangle_5.create_duval_5_nocolor()
    marker_name = duval_triangle_5.calculate_duval_5_result(100, 100, 100)
    fig5.add_trace(duval_triangle_5.create_duval_5_marker(100, 100, 100, marker_name, marker_color='green'))
    fig5 = add_ternary_uncertainty_lines(fig5, test_point2, ['blue', 'red'])
    fig5.show()

# -*- coding: utf-8 -*-
"""graphical_distributions.py

This module calculates graphical diagnostic result related distribution lines & coordinates.

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
import scipy
from ternary_to_cartesian_conversions import plotly_ternary_to_cartesian as ternary_to_cartesian
from ternary_to_cartesian_conversions import cartesian_to_ternary_plotly as cartesian_to_ternary

def round_up(n, decimals=2):
    multiplier = 10 ** decimals
    return np.floor(n * multiplier + 0.5) / multiplier

def calculate_ternary_coordinates(i, j, k, rounding=False):

    if (i == 0) and (j == 0) and (k == 0):
        return [0, 0, 0]

    x = (i / (i + j + k))*100
    y = (j / (i + j + k))*100
    z = (k / (i + j + k))*100

    if rounding is False:
        return np.array([x, y, z])
    else:
        coordinates = round_up(np.array([x, y, z]), rounding)
        return coordinates
    
def euclidian_distance(p1, p2, printout=False):
    # euclidian distance between points
    d = np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    if printout is True:
        print(f'Euclidian distance between points ({p1[0]}, {p1[1]}) and ({p2[0]}, {p2[1]}) is:\n{d}')

    return d

def calculate_group_centerpoint(group_coord_a, group_coord_b, group_coord_c, input_ternary_coordinates=False):

    if input_ternary_coordinates is False:
        a_values = group_coord_a
        b_values = group_coord_b
        c_values = group_coord_c

        try:
            assert len(a_values) == len(b_values), 'a values and b values have different lengths!'
            assert len(b_values) == len(c_values), 'b values and c values have different lengths!'
            assert len(a_values) == len(c_values), 'a values and c values have different lengths!'
        except Exception as e:
            print(e)

        values_length = len(a_values)

        coordinates_group = np.zeros(shape=(values_length, 3))
        j = 0
        for a, b, c in zip(a_values, b_values, c_values):
            coordinates_group[j][0], coordinates_group[j][1], coordinates_group[j][2] = calculate_ternary_coordinates(a, b, c)
            j+=1

        group_coord_a = coordinates_group[..., 0]
        group_coord_b = coordinates_group[..., 1]
        group_coord_c = coordinates_group[..., 2]

    try:
        assert len(group_coord_a) == len(group_coord_b), 'a coordinates and b coordinates have different lengths!'
        assert len(group_coord_b) == len(group_coord_c), 'b coordinates and c coordinates have different lengths!'
        assert len(group_coord_a) == len(group_coord_c), 'a coordinates and c coordinates have different lengths!'
        
        if input_ternary_coordinates is False:
            assert values_length == len(group_coord_a), 'coordinates after ternanary conversion have different length!'

        if type(group_coord_a) == list:
            assert np.array(group_coord_a).max() <= 100, 'a coordinate values higher than 100!'
        else:
            assert group_coord_a.max() <= 100, 'a coordinate values higher than 100!'

        if type(group_coord_b) == list:
            assert np.array(group_coord_b).max() <= 100, 'b coordinate values higher than 100!'
        else:
            assert group_coord_b.max() <= 100, 'b coordinate values higher than 100!'

        if type(group_coord_c) == list:
            assert np.array(group_coord_c).max() <= 100, 'c coordinate values higher than 100!'
        else:
            assert group_coord_c.max() <= 100, 'c coordinate values higher than 100!'
    except Exception as e:
        print(e)

    coordinates_length = len(group_coord_a)
    cartesian_group = np.zeros(shape=(coordinates_length, 2))

    i = 0
    for a, b, c in zip(group_coord_a, group_coord_b, group_coord_c):
        cartesian_group[i][0], cartesian_group[i][1] = ternary_to_cartesian(a, b, c)
        i+=1

    centerpoint_x = np.average(cartesian_group[..., 0])
    centerpoint_y = np.average(cartesian_group[..., 1])
    centerpoint_array = np.array([centerpoint_x, centerpoint_y])

    centerpoint_a, centerpoint_b, centerpoint_c = cartesian_to_ternary(centerpoint_x, centerpoint_y)
    centerpoint_ternary_array = np.array([centerpoint_a, centerpoint_b, centerpoint_c])
    
    return centerpoint_array, centerpoint_ternary_array, cartesian_group


def create_group_distribution_data(a_groups, b_groups, c_groups, percentiles=[0, 25, 50, 75, 90, 100], result_in_ternary=True):

    a_groups_len = [len(x) for x in a_groups]
    b_groups_len = [len(x) for x in b_groups]
    c_groups_len = [len(x) for x in c_groups]

    if a_groups_len != b_groups_len or b_groups_len != c_groups_len or a_groups_len != c_groups_len:
        raise Exception('Uneven group coordinates')

    centerpoints = []
    group_data_full = []
    for m, n in enumerate(a_groups_len):
        group_coordinates = np.array([calculate_ternary_coordinates(a_ppm, b_ppm, c_ppm) for a_ppm, b_ppm, c_ppm in zip(a_groups[m], b_groups[m], c_groups[m])])
        group_center, group_center_ternary, group_cartesian_coordinates = calculate_group_centerpoint(group_coordinates[..., 0], group_coordinates[..., 1], group_coordinates[..., 2], input_ternary_coordinates=True)
        centerpoints.append(group_center_ternary)

        distances = []
        for coordinates in group_cartesian_coordinates:
            # euclidian distance between points
            distance_from_center = euclidian_distance(group_center, coordinates)
            distances.append(distance_from_center)
        distances_array = np.array([distances]).transpose()

        group_percentiles = []
        for l, perc in enumerate(percentiles):
            if l == 0:
                continue
            percentile_value_low = np.percentile(distances_array, percentiles[l-1])
            percentile_value_high = np.percentile(distances_array, perc)

            # TODO select percentile relevant points with scipy convexhull
            # https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.ConvexHull.html
            #scipy.spatial.ConvexHull(points, incremental=False, qhull_options=None)
            group_percentiles.append(group_coordinates[np.where((distances_array[..., 0] <= percentile_value_high) & (distances_array[..., 0] >= percentile_value_low))])
            

        group_data_full.append(group_percentiles)
        

    return centerpoints, group_data_full



# %%
if __name__ == '__main__':
    import plotly.graph_objects as go   # plotly is an interactive plotting library

    import duval_triangle_1

    fig = duval_triangle_1.create_duval_1_colorized()
    fig.add_trace(duval_triangle_1.create_duval_1_marker(10, 26, 64, 'test'))
    fig.show()
    

    wiki_x, wiki_y = ternary_to_cartesian(10, 64, 26)
    print(f'wiki: {wiki_x} {wiki_y}')

    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=[0, 50], y=[0, 86.6], mode='lines', marker_color='black'))
    fig2.add_trace(go.Scatter(x=[50, 100], y=[86.6, 0], mode='lines', marker_color='black'))
    fig2.add_trace(go.Scatter(x=[100, 0], y=[0, 0], mode='lines', marker_color='black'))
    fig2.add_trace(go.Scatter(x=[wiki_x], y=[wiki_y], mode='markers', marker_color='green'))
    fig2.show()

    '''
    import duval_triangle_2

    ch4_list= [[200, 50, 100, 200], [0, 20, 41, 60, 66, 80], [15, 60, 160]]
    c2h2_list= [[10, 20, 30, 40], [0, 1, 2, 5, 6, 10], [100, 200, 500]]
    c2h4_list= [[400, 500, 600, 1000], [0, 5, 50, 60, 66, 67], [60, 80, 110]]
    groups_list= ['Group1', 'Group2', 'Group3']

    centerpoints = create_group_distribution_data(ch4_list, c2h2_list, c2h4_list)

    centermass = []
    for ch4, c2h2, c2h4 in zip(ch4_list, c2h2_list, c2h4_list):
        a = np.sum(ch4) / len(ch4)
        b = np.sum(c2h2) / len(c2h2)
        c = np.sum(c2h4) / len(c2h4)
        center_coord = calculate_ternary_coordinates(a, b, c)
        centermass.append(center_coord)

    fig = duval_triangle_2.create_duval_2_group_graph(ch4_list, c2h2_list, c2h4_list, groups_list, colorized=False, group_colors=['rgb(136, 204, 238)', 'rgb(204, 102, 119)', 'rgb(221, 204, 119)', 'rgb(17, 119, 51)'])
    for centerpoint, group_name in zip(centerpoints, groups_list):
        fig.add_trace(go.Scatterternary(a= [centerpoint[0]],
                                            b= [centerpoint[1]],
                                            c= [centerpoint[2]],
                                            name= group_name,
                                            mode='markers',
                                            marker_size=10,
                                            meta= [group_name],
                                            hovertemplate="Center point: %{meta[0]}<br>CH4: %{a:.2f}%<br>C2H2: %{b:.2f}%<br>C2H4: %{c:.2f}%<extra></extra>"
                                            ))
    for centerpoint, group_name in zip(centermass, groups_list):
        fig.add_trace(go.Scatterternary(a= [centerpoint[0]],
                                            b= [centerpoint[1]],
                                            c= [centerpoint[2]],
                                            name= group_name,
                                            mode='markers',
                                            marker_size=10,
                                            meta= [group_name],
                                            hovertemplate="Center mass point: %{meta[0]}<br>CH4: %{a:.2f}%<br>C2H2: %{b:.2f}%<br>C2H4: %{c:.2f}%<extra></extra>"
                                            ))
    fig.show()
    '''

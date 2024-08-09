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
import plotly.graph_objects as go   # plotly is an interactive plotting library
import scipy
from ternary_to_cartesian_conversions import plotly_ternary_to_cartesian as ternary_to_cartesian
from ternary_to_cartesian_conversions import cartesian_to_ternary_plotly as cartesian_to_ternary

def round_up(n, decimals=2):
    multiplier = 10 ** decimals
    return np.floor(n * multiplier + 0.5) / multiplier

def calculate_ternary_coordinates(i, j, k, rounding=False):

    if (i == 0) and (j == 0) and (k == 0):
        return [100/3, 100/3, 100/3]

    a = (i / (i + j + k))*100
    b = (j / (i + j + k))*100
    c = (k / (i + j + k))*100

    if rounding is False:
        return np.array([a, b, c])
    else:
        coordinates = round_up(np.array([a, b, c]), rounding)
        return coordinates
    
def calculate_ternary_coordinates_multi_ppm(i_list, j_list, k_list, rounding=False):
    try:
        assert len(i_list) == len(j_list), 'a values and b values have different lengths!'
        assert len(j_list) == len(k_list), 'b values and c values have different lengths!'
        assert len(i_list) == len(k_list), 'a values and c values have different lengths!'
        assert sum(len(x) for x in i_list) == sum(len(x) for x in j_list), 'Sum of a values and b values have different lengths!'
        assert sum(len(x) for x in j_list) == sum(len(x) for x in k_list), 'Sum of b values and c values have different lengths!'
        assert sum(len(x) for x in i_list) == sum(len(x) for x in k_list), 'Sum of a values and c values have different lengths!'
    except Exception as e:
        print(e)

    
    coordinates_list = []

    # Check for a multilevel list
    if type(i_list[0]) is list:
        for i_group, j_group, k_group in zip(i_list, j_list, k_list):
            coordinates_group = np.empty(shape=(len(i_group), 3))
            j = 0
            for a, b, c in zip(i_group, j_group, k_group):
                coordinates_group[j][0], coordinates_group[j][1], coordinates_group[j][2] = calculate_ternary_coordinates(a, b, c)
                j+=1
            
            coordinates_list.append(coordinates_group)
    else:
        coordinates_group = np.empty(shape=(len(i_list), 3))
        j = 0
        for a, b, c in zip(i_list, j_list, k_list):
            coordinates_group[j][0], coordinates_group[j][1], coordinates_group[j][2] = calculate_ternary_coordinates(a, b, c)
            j+=1
        
        coordinates_list.append(coordinates_group)


    if rounding is False:
        return coordinates_list
    else:
        rounded_coordinates_list = []
        for coord in coordinates_list:
            rounded_coordinates_list.append(round_up(coord, rounding))
        return rounded_coordinates_list

    
def euclidian_distance(p1, p2, printout=False):
    # euclidian distance between points
    d = np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    if printout is True:
        print(f'Euclidian distance between points ({p1[0]}, {p1[1]}) and ({p2[0]}, {p2[1]}) is:\n{d}')

    return d

def calculate_ternary_group_centerpoint(group_coord_a, group_coord_b, group_coord_c, input_ternary_coordinates=False):

    # if given ppm values in groups, convert to ternary coordinates
    if input_ternary_coordinates is False:
        a_values = group_coord_a
        b_values = group_coord_b
        c_values = group_coord_c

        # Check for a multilevel list
        coordinates_list = calculate_ternary_coordinates_multi_ppm(a_values, b_values, c_values)

        print(coordinates_list)

        ternary_group_a = []
        ternary_group_b = []
        ternary_group_c = []
        for coordinates_group in coordinates_list:
            ternary_group_a.append(coordinates_group[..., 0].tolist())
            ternary_group_b.append(coordinates_group[..., 1].tolist())
            ternary_group_c.append(coordinates_group[..., 2].tolist())

        group_coord_a = ternary_group_a
        group_coord_b = ternary_group_b
        group_coord_c = ternary_group_c


    # if not nested list of groups, make into nested list
    if type(group_coord_a[0]) is not list:
        group_coord_a = [group_coord_a]
        group_coord_b = [group_coord_b]
        group_coord_c = [group_coord_c]

    try:
        assert len(group_coord_a) == len(group_coord_b), 'a coordinates and b coordinates have different lengths!'
        assert len(group_coord_b) == len(group_coord_c), 'b coordinates and c coordinates have different lengths!'
        assert len(group_coord_a) == len(group_coord_c), 'a coordinates and c coordinates have different lengths!'

        assert sum(len(x) for x in a_values) == sum(len(x) for x in b_values), 'Sum of a values and b values have different lengths!'
        assert sum(len(x) for x in b_values) == sum(len(x) for x in c_values), 'Sum of b values and c values have different lengths!'
        assert sum(len(x) for x in a_values) == sum(len(x) for x in c_values), 'Sum of a values and c values have different lengths!'
    
        assert np.array(group_coord_a).max() <= 100, 'a coordinate values higher than 100!'
        assert np.array(group_coord_b).max() <= 100, 'b coordinate values higher than 100!'
        assert np.array(group_coord_c).max() <= 100, 'c coordinate values higher than 100!'
    except Exception as e:
        print(e)

    cartesian_coordinates_array = []

    g = 0
    for a_coordinates, b_coordinates, c_coordinates in zip(group_coord_a, group_coord_b, group_coord_c):

        coordinates_length = len(a_coordinates)
        cartesian_group = np.empty(shape=(coordinates_length, 2))

        i = 0
        for a, b, c in zip(a_coordinates, b_coordinates, c_coordinates):
            cartesian_group[i][0], cartesian_group[i][1] = ternary_to_cartesian(a, b, c)
            i+=1

        centerpoint_x = np.average(cartesian_group[..., 0])
        centerpoint_y = np.average(cartesian_group[..., 1])

        centerpoint_a, centerpoint_b, centerpoint_c = cartesian_to_ternary(centerpoint_x, centerpoint_y)

        if g == 0:
            centerpoint_array = np.array([[centerpoint_x, centerpoint_y]])
            centerpoint_ternary_array = np.array([[centerpoint_a, centerpoint_b, centerpoint_c]])
        else:
            previous_centerpoints = centerpoint_array
            new_centerpoint = np.array([centerpoint_x, centerpoint_y])
            centerpoint_array = np.vstack([previous_centerpoints, new_centerpoint])

            previous_centerpoints_ternary = centerpoint_ternary_array
            new_centerpoint_ternary = np.array([centerpoint_a, centerpoint_b, centerpoint_c])
            centerpoint_ternary_array = np.vstack([previous_centerpoints_ternary, new_centerpoint_ternary])

        cartesian_coordinates_array.append(cartesian_group)
        g+=1
    
    
    return centerpoint_array, centerpoint_ternary_array, cartesian_coordinates_array


def create_ternary_group_distribution_data(a_groups, b_groups, c_groups, percentiles=[0, 25, 50, 75, 90, 100], edge_result_in_ternary=True):

    a_groups_len = [len(x) for x in a_groups]
    b_groups_len = [len(x) for x in b_groups]
    c_groups_len = [len(x) for x in c_groups]

    if a_groups_len != b_groups_len or b_groups_len != c_groups_len or a_groups_len != c_groups_len:
        raise Exception('Uneven group coordinates')

    centerpoints = []
    group_ternary_data_full = []
    group_data_lines_full = []
    for m, n in enumerate(a_groups_len):
        group_coordinates = np.array([calculate_ternary_coordinates(a_ppm, b_ppm, c_ppm) for a_ppm, b_ppm, c_ppm in zip(a_groups[m], b_groups[m], c_groups[m])])
        group_center, group_center_ternary, group_cartesian_coordinates = calculate_ternary_group_centerpoint(group_coordinates[..., 0], group_coordinates[..., 1], group_coordinates[..., 2], input_ternary_coordinates=True)
        centerpoints.append(group_center_ternary)

        distances = []
        for coordinates in group_cartesian_coordinates:
            # euclidian distance between points
            distance_from_center = euclidian_distance(group_center, coordinates)
            distances.append(distance_from_center)
        distances_array = np.array([distances]).transpose()

        data_grouped_in_percentiles = []
        for l, perc in enumerate(percentiles):
            if l == 0:
                continue
            percentile_value_low = np.percentile(distances_array, percentiles[l-1])
            percentile_value_high = np.percentile(distances_array, perc)

            data_grouped_in_percentiles.append(group_coordinates[np.where((distances_array[..., 0] <= percentile_value_high) & (distances_array[..., 0] >= percentile_value_low))])
            
        group_outer_edges_all = []
        for perc_data_group in data_grouped_in_percentiles:
            group_outer_edge = calculate_group_outer_edges(perc_data_group)
            if edge_result_in_ternary is True:
                ternary_outer_edge = np.empty(shape=(outer_edge.shape[0], 3))
                for a, arr in enumerate(outer_edge):
                    ternary_outer_edge[a] = cartesian_to_ternary(arr[0], arr[1])
                
                group_outer_edges_all.append(ternary_outer_edge)
            else:
                group_outer_edges_all.append(group_outer_edge)

        group_ternary_data_full.append(group_coordinates)
        group_data_lines_full.append(group_outer_edges_all)
        
    return centerpoints, group_data_lines_full, group_ternary_data_full


def calculate_group_outer_edges(group_array):
    hull = scipy.spatial.ConvexHull(group_array)

    # Get the outer edges of the hull from vertices of the original points
    # copy first point to last point for a fully connecting outer edge
    outer_edge = np.empty(shape=(len(hull.vertices)+1, 2))
    for v, vert in enumerate(hull.vertices):
        outer_edge[v] = points[vert]
    outer_edge[-1] = outer_edge[0]

    return outer_edge

# %%
if __name__ == '__main__':
    

    points = np.array([[10, 10], [-10, -10], [-10, 10], [10, -10], [5, 5], [-5, 5], [-5, -5], [5, -5]])
    hull = scipy.spatial.ConvexHull(points)
    outer_edge = np.empty(shape=(len(hull.vertices)+1, 2))
    for v, vert in enumerate(hull.vertices):
        outer_edge[v] = points[vert]
    outer_edge[-1] = outer_edge[0]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=points[...,0], y=points[...,1], mode='markers', name='test points', marker_size=15, marker_color='red'))
    fig.add_trace(go.Scatter(x=outer_edge[...,0], y=outer_edge[...,1], mode='lines', name='outer edge of points', marker_color='green'))
    fig.show()

    cartesian_array = np.array([[10, 10], [60, 40], [40, 50]])
    centerpoint_x = np.average(cartesian_array[..., 0])
    centerpoint_y = np.average(cartesian_array[..., 1])
    hull = scipy.spatial.ConvexHull(cartesian_array)
    outer_edge = np.empty(shape=(len(hull.vertices)+1, 2))
    for v, vert in enumerate(hull.vertices):
        outer_edge[v] = cartesian_array[vert]
    outer_edge[-1] = outer_edge[0]

    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=[0, 50], y=[0, 86.6], mode='lines', name='side a', marker_color='black'))
    fig2.add_trace(go.Scatter(x=[50, 100], y=[86.6, 0], mode='lines', name='side b', marker_color='black'))
    fig2.add_trace(go.Scatter(x=[100, 0], y=[0, 0], mode='lines', name='side c', marker_color='black'))
    fig2.add_trace(go.Scatter(x=cartesian_array[...,0], y=cartesian_array[...,1], mode='markers', name='test points', marker_size=15, marker_color='red'))
    fig2.add_trace(go.Scatter(x=[centerpoint_x], y=[centerpoint_y], mode='markers', name='center point', marker_size=15, marker_color='green'))
    fig2.add_trace(go.Scatter(x=outer_edge[...,0], y=outer_edge[...,1], mode='lines', name='outer edge of points', marker_color='green'))
    fig2.show()

    ternary_array = np.empty(shape=(len(cartesian_array), 3))
    for p, point in enumerate(cartesian_array):
        ternary_array[p][0], ternary_array[p][1], ternary_array[p][2] = cartesian_to_ternary(point[0], point[1])

    centerpoint_array, centerpoint_ternary_array, cartesian_group = calculate_ternary_group_centerpoint(ternary_array[..., 0].tolist(), ternary_array[..., 1].tolist(), ternary_array[..., 2].tolist(), input_ternary_coordinates=True)

    fig3 = go.Figure(layout=dict(ternary_sum=100))
    fig3.add_trace(go.Scatterternary(a= ternary_array[..., 0],
                                        b= ternary_array[..., 1],
                                        c= ternary_array[..., 2],
                                        name= 'test points',
                                        mode='markers',
                                        marker_color='red',
                                        marker_size=10))
    fig3.add_trace(go.Scatterternary(a=[centerpoint_ternary_array[0][0]],
                                        b=[centerpoint_ternary_array[0][1]],
                                        c=[centerpoint_ternary_array[0][2]],
                                        name= 'center point',
                                        mode='markers',
                                        marker_color='green',
                                        marker_size=10))
    fig3.show()

    import duval_triangle_2

    ch4_list= [[200, 50, 100, 200], [0, 20, 41, 60, 66, 80], [15, 60, 160, 200]]
    c2h2_list= [[10, 20, 30, 40], [0, 1, 2, 5, 6, 10], [100, 200, 500, 1000]]
    c2h4_list= [[400, 500, 600, 1000], [0, 5, 50, 60, 66, 67], [60, 80, 110, 200]]
    groups_list= ['Group1', 'Group2', 'Group3']

    centerpoints, centerpoint_ternary, cartesian_group = calculate_ternary_group_centerpoint(ch4_list, c2h2_list, c2h4_list)

    # TODO fix the addition of all centerpoints, stuck on g=0

    fig4 = duval_triangle_2.create_duval_2_group_graph(ch4_list, c2h2_list, c2h4_list, groups_list, colorized=False, group_colors=['rgb(136, 204, 238)', 'rgb(204, 102, 119)', 'rgb(221, 204, 119)', 'rgb(17, 119, 51)'])
    for centerpoint, group_name in zip(centerpoint_ternary, groups_list):
        fig4.add_trace(go.Scatterternary(a= [centerpoint[0]],
                                            b= [centerpoint[1]],
                                            c= [centerpoint[2]],
                                            name= f'{group_name} centerpoint',
                                            mode='markers',
                                            marker_size=10,
                                            meta= [f'{group_name}'],
                                            hovertemplate="Center point: %{meta[0]}<br>CH4: %{a:.2f}%<br>C2H2: %{b:.2f}%<br>C2H4: %{c:.2f}%<extra></extra>"
                                            ))
    fig4.show()
    

# %%

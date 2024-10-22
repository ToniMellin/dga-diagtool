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
import plotly.figure_factory as ff
from plotly.subplots import make_subplots
from scipy.spatial import ConvexHull
from scipy.stats import gaussian_kde
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from ternary_to_cartesian_conversions import plotly_ternary_to_cartesian as ternary_to_cartesian
from ternary_to_cartesian_conversions import cartesian_to_ternary_plotly_rounded as cartesian_to_ternary_rounded

# point & polygon comparison accuracy
EPSILON = 1e-15

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
        if type(i_list[0]) is list:
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
    
def transform_multi_array_cartesian_to_ternary(array_groups_list, rounding=2):

    transformed_list = []

    for group in array_groups_list:
        group_arr_list = []
        for array in group:
            array_section = np.empty(shape=(len(array), 3))
            k = 0
            for coord in array:
                array_section[k][0], array_section[k][1], array_section[k][2] = cartesian_to_ternary_rounded(coord[0], coord[1], rounding) 
                k+=1

            group_arr_list.append(array_section)
        
        transformed_list.append(group_arr_list)

    return transformed_list

    
def euclidian_distance(p1, p2, printout=False):
    # euclidian distance between points
    d = np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    if printout is True:
        print(f'Euclidian distance between points ({p1[0]}, {p1[1]}) and ({p2[0]}, {p2[1]}) is:\n{d}')

    return d

def check_points_needed_for_percentile_division(points, perc_list, min_allowed_points):
    if points < (2*min_allowed_points):
        return False

    relative_sizes = []
    for i, curr_perc in enumerate(perc_list):
        if i == 0:
            continue
        relative_size = perc_list[i-1] - curr_perc
        relative_sizes.append(relative_size)

    smallest_divider = np.min(relative_sizes)
    min_point_count = np.floor(points / (100/smallest_divider))

    

    if min_point_count < min_allowed_points:
        return False
    else:
        return True

def percentile_validity_check(dataset_size, percentile_list, min_req_size):

    perc_length = len(percentile_list)
    acceptable_perc_list = False

    if check_points_needed_for_percentile_division(dataset_size, percentile_list, min_req_size) is True:
        return percentile_list

    current_percentile_partition_size = (len(percentile_list) - 1)
    perc_length = len(percentile_list)

    if perc_length <= 2:
        print(f'Unable to generate valid percentile list for {dataset_size} points!\n')
        return False

    percentile_list = np.flip(np.arange(0, 101, 100/current_percentile_partition_size)).tolist()

    if check_points_needed_for_percentile_division(dataset_size, percentile_list, min_req_size) is True:
        return percentile_list

    while (perc_length > 2) and (acceptable_perc_list is False):
        new_percentile_size = (len(percentile_list) - 2)
        percentile_list = np.flip(np.arange(0, 101, 100/new_percentile_size)).tolist()
        perc_length = len(percentile_list)
        acceptable_perc_list = check_points_needed_for_percentile_division(dataset_size, percentile_list, min_req_size)

    if acceptable_perc_list is True:
        return percentile_list
    else:
        print(f'Unable to generate valid percentile list for {dataset_size} points!\n')
        return False

def calculate_ternary_group_centerpoint(group_coord_a, group_coord_b, group_coord_c, input_ternary_coordinates=False, ternary_rounding=2):

    # if given ppm values in groups, convert to ternary coordinates
    if input_ternary_coordinates is False:
        a_values = group_coord_a
        b_values = group_coord_b
        c_values = group_coord_c

        # Check for a multilevel list
        coordinates_list = calculate_ternary_coordinates_multi_ppm(a_values, b_values, c_values, ternary_rounding)

        #print(coordinates_list)

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

        assert sum(len(x) for x in group_coord_a) == sum(len(x) for x in group_coord_b), 'Sum of a values and b values have different lengths!'
        assert sum(len(x) for x in group_coord_b) == sum(len(x) for x in group_coord_c), 'Sum of b values and c values have different lengths!'
        assert sum(len(x) for x in group_coord_a) == sum(len(x) for x in group_coord_c), 'Sum of a values and c values have different lengths!'
    
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

        centerpoint_a, centerpoint_b, centerpoint_c = cartesian_to_ternary_rounded(centerpoint_x, centerpoint_y, ternary_rounding)

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
    
    
    return centerpoint_array.tolist(), centerpoint_ternary_array.tolist(), cartesian_coordinates_array

def create_ternary_group_distribution_data(a_groups, b_groups, c_groups, inverted_percentiles=[100, 75, 50, 25, 0], ternary_rounding=2, **kwargs):

    if type(a_groups[0]) is not list:
        a_groups = [a_groups]
        b_groups = [b_groups]
        c_groups = [c_groups]

    a_groups_len = [len(x) for x in a_groups]
    b_groups_len = [len(x) for x in b_groups]
    c_groups_len = [len(x) for x in c_groups]

    if a_groups_len != b_groups_len or b_groups_len != c_groups_len or a_groups_len != c_groups_len:
        raise Exception('Uneven group coordinates')
    
    if 100 not in inverted_percentiles:
        perc_100 = [0]
        perc_100.extend(inverted_percentiles)
        inverted_percentiles = perc_100

    if 0 not in inverted_percentiles:
        inverted_percentiles.extend([0])

    for a_grp in a_groups:
        points = len(a_grp)
        percentile_check = percentile_validity_check(points, inverted_percentiles, 3) # distribution edge calculation requires at least 3 points per percentile group
        if percentile_check is False:
            return False
        else:
            inverted_percentiles = percentile_check

    if 'discard_zeros' in kwargs:
        discard_zeros = kwargs['discard_zeros']
    else:
        discard_zeros = False

    if 'cutoff' in kwargs:
        cutoff = kwargs['cutoff']
    else:
        cutoff = False

    if 'cutoff_direction' in kwargs:
        cutoff_direction = kwargs['cutoff_direction']
    else:
        cutoff_direction = '>'

    # data cleanup by cutoff or discard zeros
    # if cutoff active discard zeros is skipped
    if  cutoff != False:
        new_a = []
        new_b = []
        new_c = []

        for a_grp, b_grp, c_grp in zip(a_groups, b_groups, c_groups):
            grp_data = np.array((a_grp, b_grp, c_grp))
            grp_data_t = np.transpose(grp_data)

            # if smaller than direction, the cutoff will drop based on if ALL are smaller than
            if cutoff_direction == '<':
                clean_grp_data = grp_data_t[~np.all(grp_data_t < cutoff, axis=1)]

            elif cutoff_direction == '<=':
                clean_grp_data = grp_data_t[~np.all(grp_data_t <= cutoff, axis=1)]

            # if greater than direction, the cutoff will drop based on if ANY of the values isn't greater than 
            elif cutoff_direction == '>=':
                clean_grp_data = grp_data_t[np.any(grp_data_t >= cutoff, axis=1)]

            else:
                clean_grp_data = grp_data_t[np.any(grp_data_t > cutoff, axis=1)]

            new_a.append(clean_grp_data[:, 0].tolist())
            new_b.append(clean_grp_data[:, 1].tolist())
            new_c.append(clean_grp_data[:, 2].tolist())

        a_groups = new_a
        b_groups = new_b
        c_groups = new_c

    elif discard_zeros != False:
        new_a = []
        new_b = []
        new_c = []

        for a_grp, b_grp, c_grp in zip(a_groups, b_groups, c_groups):
            grp_data = np.array((a_grp, b_grp, c_grp))
            grp_data_t = np.transpose(grp_data)

            clean_grp_data = grp_data_t[~np.all(grp_data_t == 0, axis=1)]

        a_groups = new_a
        b_groups = new_b
        c_groups = new_c


    group_center, group_center_ternary, group_cartesian_coordinates = calculate_ternary_group_centerpoint(a_groups, b_groups, c_groups, False, False)

    # create groups with distances data
    distances_groups = []
    for centerpoint, coordinates_array in zip(group_center, group_cartesian_coordinates):
        coordinates = coordinates_array.tolist()

        distances = []
        # euclidian distance between points
        for coord in coordinates:
            distance_from_center = euclidian_distance(centerpoint, coord)
            distances.append(distance_from_center)
        distances_groups.append(distances)

    # create percentile separated groups of data
    all_groups_data_grouped_in_percentiles = []
    all_groups_distances_in_percentiles = []
    all_groups_cartesian_in_percentiles = []
    for dist_list, a_group, b_group, c_group, cartesian_group in zip(distances_groups, a_groups, b_groups, c_groups, group_cartesian_coordinates):
        distances_array = np.array(dist_list)
        group_ternary_coord = calculate_ternary_coordinates_multi_ppm(a_group, b_group, c_group)

        data_grouped_in_percentiles = []
        distances_in_percentiles = []
        cartesian_in_percentiles = []
        for l, perc in enumerate(inverted_percentiles):
            if l == 0:
                continue
            else:
                percentile_value_high = np.percentile(distances_array, inverted_percentiles[l-1])
                percentile_value_low = np.percentile(distances_array, perc)

            data_sequence = np.where((distances_array <= percentile_value_high) & (distances_array > percentile_value_low))
            data_seq_len = data_sequence[0].size

            if data_seq_len < 3:
                raise Exception(f"One percentile group has < 3 data sequence length [{inverted_percentiles[l-1]}, {perc}])")

            data_grouped_in_percentiles.append(group_ternary_coord[0][data_sequence])
            distances_in_percentiles.append(distances_array[data_sequence])
            cartesian_in_percentiles.append(cartesian_group[data_sequence])
        all_groups_data_grouped_in_percentiles.append(data_grouped_in_percentiles)
        all_groups_distances_in_percentiles.append(distances_in_percentiles)
        all_groups_cartesian_in_percentiles.append(cartesian_in_percentiles)

    # https://stackoverflow.com/questions/16750618/whats-an-efficient-way-to-find-if-a-point-lies-in-the-convex-hull-of-a-point-cl
    all_groups_edges_cartesian = []
    all_groups_edges_ternary = []
    for p_groups, full_group in zip(all_groups_cartesian_in_percentiles, group_cartesian_coordinates):
        group_edges_all=[]
        group_size = len(p_groups)

        total_group_outer_edge = calculate_group_outer_edges(full_group)
        
        for p, perc_group in enumerate(p_groups):
            if p == 0:
                group_edges_all.append(total_group_outer_edge)
                continue

            group_outer_edge = calculate_group_outer_edges(perc_group)
            

            # checking for points left out of the current outer edge in the next groups outer edge
            
            if p < (group_size-1):
                grp_polygon = Polygon(group_outer_edge)

                smaller_percentile_edges = []
                for r in range(p+1, group_size):
                    next_group_outer_edge = calculate_group_outer_edges(p_groups[r])
                    smaller_percentile_edges.append(next_group_outer_edge)
                    
                outside_points = np.array([])
                for small_p_edge in smaller_percentile_edges:
                
                    for n, nxt_point in enumerate(small_p_edge):

                        if n > (len(small_p_edge) - 2):
                            continue

                        point = Point(nxt_point)

                        if ((grp_polygon.contains(point) is False) or (point.distance(grp_polygon) > EPSILON)):
                            if outside_points.size == 0:
                                outside_points = np.array([nxt_point])
                            else:
                                outside_points = np.append(outside_points, [nxt_point], axis=0)

                # adding points left outside the current groups outer edge and recalculating outer edge
                if outside_points.shape[0] > 0:
                    new_perc_group = np.append(perc_group, outside_points, axis=0)
                    group_outer_edge = calculate_group_outer_edges(new_perc_group)


            group_edges_all.append(group_outer_edge)

        all_groups_edges_cartesian.append(group_edges_all)

    # TODO fix rounding bug
    all_groups_edges_ternary = transform_multi_array_cartesian_to_ternary(all_groups_edges_cartesian, ternary_rounding)
        
    return group_center_ternary, all_groups_edges_ternary, all_groups_edges_cartesian


def calculate_group_outer_edges(group_array):
    hull = ConvexHull(group_array)

    # Get the outer edges of the hull from vertices of the original points
    # copy first point to last point for a fully connecting outer edge
    outer_edge = np.empty(shape=(len(hull.vertices)+1, 2))
    for v, vert in enumerate(hull.vertices):
        outer_edge[v] = group_array[vert]
    outer_edge[-1] = outer_edge[0]

    return outer_edge

def simple_cartesian_outer_edge_test(points, mark_size=15):

    outer_edge = calculate_group_outer_edges(points)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=points[...,0], y=points[...,1], mode='markers', name='test points', marker_size=mark_size, marker_color='red'))
    fig.add_trace(go.Scatter(x=outer_edge[...,0], y=outer_edge[...,1], mode='lines', name='outer edge of points', marker_color='green'))

    return fig

def simple_cartesian_triangle_outer_edge_with_center_test(cartesian_array, mark_size=15):
    
    centerpoint_x = np.average(cartesian_array[..., 0])
    centerpoint_y = np.average(cartesian_array[..., 1])

    outer_edge = calculate_group_outer_edges(cartesian_array)

    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=[0, 50], y=[0, 86.6], mode='lines', name='side a', marker_color='black'))
    fig2.add_trace(go.Scatter(x=[50, 100], y=[86.6, 0], mode='lines', name='side b', marker_color='black'))
    fig2.add_trace(go.Scatter(x=[100, 0], y=[0, 0], mode='lines', name='side c', marker_color='black'))
    fig2.add_trace(go.Scatter(x=cartesian_array[...,0], y=cartesian_array[...,1], mode='markers', name='test points', marker_size=mark_size, marker_color='red'))
    fig2.add_trace(go.Scatter(x=[centerpoint_x], y=[centerpoint_y], mode='markers', name='center point', marker_size=mark_size, marker_color='green'))
    fig2.add_trace(go.Scatter(x=outer_edge[...,0], y=outer_edge[...,1], mode='lines', name='outer edge of points', marker_color='green'))

    return fig2

def point_density_calculation(xy_tuple_array):

    x = xy_tuple_array[:, 0]
    y = xy_tuple_array[:, 1]

    # https://stackoverflow.com/questions/20105364/how-can-i-make-a-scatter-plot-colored-by-density
    xy = np.vstack([x,y])
    z = gaussian_kde(xy)(xy)

    return z

def create_ternary_density_distribution_graph(a_groups, b_groups, c_groups, axis_names, **kwargs):

    if type(a_groups[0]) is not list:
        a_groups = [a_groups]
        b_groups = [b_groups]
        c_groups = [c_groups]

    a_groups_len = [len(x) for x in a_groups]
    b_groups_len = [len(x) for x in b_groups]
    c_groups_len = [len(x) for x in c_groups]

    if a_groups_len != b_groups_len or b_groups_len != c_groups_len or a_groups_len != c_groups_len:
        raise Exception(f'Uneven group coordinates!! {a_groups_len}, {b_groups_len}, {c_groups_len}')

    group_n = len(a_groups)

    if group_n > 4:
        raise Exception(f'Max 4 groups allowed for ternanry density plotting!! Given {group_n} groups!')

    if 'colorscale' in kwargs:
        color_scale = kwargs['colorscale']
    else:
        color_scale = 'Bluered'

    if 'show_markers' in kwargs:
        show_markers = kwargs['show_markers']
    else:
        show_markers = False

    if 'contour_n' in kwargs:
        contour_n = kwargs['contour_n']
    else:
        contour_n = 20

    if 'discard_zeros' in kwargs:
        discard_zeros = kwargs['discard_zeros']
    else:
        discard_zeros = False

    if 'cutoff' in kwargs:
        cutoff = kwargs['cutoff']
    else:
        cutoff = False

    if 'cutoff_direction' in kwargs:
        cutoff_direction = kwargs['cutoff_direction']
    else:
        cutoff_direction = '>'

    if 'group_names' in kwargs:
        group_names = kwargs['group_names']
        if group_names is False:
            group_names = []
            group_range= len(a_groups) + 1
            for grp in range(1, group_range):
                group_names.append(f'group_{grp}')
    else:
        group_names = []
        group_range= len(a_groups) + 1
        for grp in range(1, group_range):
            group_names.append(f'group_{grp}')

    if 'marker_compare' in kwargs:
        marker_compare = kwargs['marker_compare']
    else:
        marker_compare = False

    # data cleanup by cutoff or discard zeros
    # if cutoff active discard zeros is skipped
    if  cutoff != False:
        new_a = []
        new_b = []
        new_c = []

        for a_grp, b_grp, c_grp in zip(a_groups, b_groups, c_groups):
            grp_data = np.array((a_grp, b_grp, c_grp))
            grp_data_t = np.transpose(grp_data)

            # if smaller than direction, the cutoff will drop based on if ALL are smaller than
            if cutoff_direction == '<':
                clean_grp_data = grp_data_t[~np.all(grp_data_t < cutoff, axis=1)]

            elif cutoff_direction == '<=':
                clean_grp_data = grp_data_t[~np.all(grp_data_t <= cutoff, axis=1)]

            # if greater than direction, the cutoff will drop based on if ANY of the values isn't greater than 
            elif cutoff_direction == '>=':
                clean_grp_data = grp_data_t[np.any(grp_data_t >= cutoff, axis=1)]

            else:
                clean_grp_data = grp_data_t[np.any(grp_data_t > cutoff, axis=1)]

            new_a.append(clean_grp_data[:, 0].tolist())
            new_b.append(clean_grp_data[:, 1].tolist())
            new_c.append(clean_grp_data[:, 2].tolist())

        a_groups = new_a
        b_groups = new_b
        c_groups = new_c

    elif discard_zeros != False:
        new_a = []
        new_b = []
        new_c = []

        for a_grp, b_grp, c_grp in zip(a_groups, b_groups, c_groups):
            grp_data = np.array((a_grp, b_grp, c_grp))
            grp_data_t = np.transpose(grp_data)

            clean_grp_data = grp_data_t[~np.all(grp_data_t == 0, axis=1)]

        a_groups = new_a
        b_groups = new_b
        c_groups = new_c

    centerpoints, centerpoint_ternary, cartesian_group = calculate_ternary_group_centerpoint(a_groups, b_groups, c_groups)

    group_ternary_coords = calculate_ternary_coordinates_multi_ppm(a_groups, b_groups, c_groups)

    if len(a_groups) > 1:
        rows_needed = int(round_up(len(a_groups)/2, 0))

        if rows_needed == 1:
            fig = make_subplots(rows=rows_needed, cols=2, start_cell="top-left", 
                                specs=[[{"type": "scatterternary"}, {"type": "scatterternary"}]]
            )
            
        elif rows_needed == 2:
            fig = make_subplots(rows=rows_needed, cols=2, start_cell="top-left", 
                                specs=[[{"type": "scatterternary"}, {"type": "scatterternary"}], 
                                        [{"type": "scatterternary"}, {"type": "scatterternary"}]]
            )
            

        for g, group_name, group_data, cart_group in zip(range(1, len(a_groups)+1), group_names, group_ternary_coords, cartesian_group):
            z_data = point_density_calculation(cart_group)
            
            row_n = int(round_up(g/2, 0)) 
            col_n = 1 + ((g - 1) % 2)
            fig_c = ff.create_ternary_contour(np.array([group_data[:, 0], group_data[:, 1], group_data[:, 2]]), z_data,
                                        pole_labels=axis_names,
                                        ncontours=contour_n,
                                        coloring='lines',
                                        colorscale=color_scale,
                                        showmarkers=show_markers)

                
            for trace_data in fig_c['data']:
                fig.append_trace(trace_data, row=row_n, col=col_n)

            t_x = ((g - 1) % 2) * 0.5
            t_y = 0.98 / row_n
            fig.add_annotation(dict(x=t_x, y=t_y,   ax=0, ay=0,
                    xref = "paper", yref = "paper",
                    font_size=18, 
                    text= f"{group_name}"
                  ))
    
    elif marker_compare is True:
        z_data = point_density_calculation(cartesian_group[0])

        fig = make_subplots(rows=1, cols=2, start_cell="top-left", 
                            specs=[[{"type": "scatterternary"}, {"type": "scatterternary"}]])

        fig_c1 = ff.create_ternary_contour(np.array([group_ternary_coords[0][:, 0], group_ternary_coords[0][:, 1], group_ternary_coords[0][:, 2]]), z_data,
                                        pole_labels=axis_names,
                                        ncontours=contour_n,
                                        coloring='lines',
                                        colorscale=color_scale,
                                        showmarkers=False)
            
        fig_c2 = ff.create_ternary_contour(np.array([group_ternary_coords[0][:, 0], group_ternary_coords[0][:, 1], group_ternary_coords[0][:, 2]]), z_data,
                                        pole_labels=axis_names,
                                        ncontours=contour_n,
                                        coloring='lines',
                                        colorscale=color_scale,
                                        showmarkers=True)
            
        for fig_s1 in fig_c1['data']:
            fig.append_trace(fig_s1, 1, 1)
        
        for fig_s2 in fig_c2['data']:
            fig.append_trace(fig_s2, 1, 2)
            
    
    else:
        z_data = point_density_calculation(cartesian_group[0])

        fig = ff.create_ternary_contour(np.array([group_ternary_coords[0][:, 0], group_ternary_coords[0][:, 1], group_ternary_coords[0][:, 2]]), z_data,
                                        pole_labels=axis_names,
                                        ncontours=contour_n,
                                        coloring='lines',
                                        colorscale=color_scale,
                                        showmarkers=show_markers)
        

    fig.update_layout(template=None, ternary_sum=100, showlegend=False)
    return fig


# %%
if __name__ == '__main__':

    '''
    points = np.array([[10, 10], [-10, -10], [-10, 10], [10, -10], [5, 5], [-5, 5], [-5, -5], [5, -5]])
    
    test_fig = simple_cartesian_outer_edge_test(points)
    test_fig.show()
    '''

    cartesian_array = np.array([[10, 10], [60, 40], [40, 50]])
    #cartesian_array = np.array([[10, 10], [60, 40], [40, 50], [50, 60], [50, 10], [40, 20], [30, 10], [25, 20]])
    test_fig2 = simple_cartesian_triangle_outer_edge_with_center_test(cartesian_array)
    test_fig2.show()

    cartesian_array_big = np.array([[10, 10], [60, 40], [40, 50], [50, 60], [50, 10], 
                            [40, 20], [35, 15], [30, 10], [25, 20], [20, 20], 
                            [20, 15], [30, 20], [30, 30], [47, 26], [30, 30],
                            [40, 40], [45, 50], [47, 51], [55, 42], [56, 40],
                            [43, 38], [50, 37], [45, 35], [35, 38], [40, 27],
                            [46, 15], [25, 12], [50, 25], [33, 20], [15, 12]])
    
    test_fig3 = simple_cartesian_triangle_outer_edge_with_center_test(cartesian_array_big, mark_size=10)
    test_fig3.update_layout(modebar_add='togglespikelines')
    test_fig3.show()

    ternary_array = np.empty(shape=(len(cartesian_array), 3))
    for p, point in enumerate(cartesian_array):
        ternary_array[p][0], ternary_array[p][1], ternary_array[p][2] = cartesian_to_ternary_rounded(point[0], point[1], 2)

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

    ch4_long = [11.55, 46.19, 57.74, 69.28, 11.55, 23.09, 17.32, 11.55, 23.09, 23.09, 17.32, 
                23.09, 34.64, 30.02, 34.64, 46.19, 57.74, 58.89, 48.5, 46.19, 43.88, 42.72, 
                40.41, 43.88, 31.18, 17.32, 13.86, 28.87, 23.09, 13.86]
    
    c2h2_long = [84.22, 16.9, 31.13, 15.36, 44.22, 48.46, 56.34, 64.22, 63.46, 68.46, 71.34, 
                 58.46, 52.68, 37.99, 52.68, 36.9, 26.13, 23.55, 20.75, 20.9, 35.06, 28.64, 
                 34.8, 43.06, 44.41, 45.34, 68.07, 35.56, 55.46, 78.07]
    
    c2h4_long = [4.23, 36.91, 11.13, 15.36, 44.23, 28.45, 26.34, 24.23, 13.45, 8.45, 11.34, 
                 18.45, 12.68, 31.99, 12.68, 16.91, 16.13, 17.56, 30.75, 32.91, 21.06, 28.64, 
                 24.79, 13.06, 24.41, 37.34, 18.07, 35.57, 21.45, 8.07]
    
    a_groups = [[11.55, 46.19, 57.74, 69.28, 11.55, 23.09, 17.32, 11.55, 23.09, 23.09, 17.32, 
                23.09, 34.64, 30.02, 34.64, 46.19, 57.74, 58.89, 48.5, 46.19, 43.88, 42.72, 
                40.41, 43.88, 31.18, 17.32, 13.86, 28.87, 23.09, 13.86]]

    b_groups = [[84.22, 16.9, 31.13, 15.36, 44.22, 48.46, 56.34, 64.22, 63.46, 68.46, 71.34, 
                58.46, 52.68, 37.99, 52.68, 36.9, 26.13, 23.55, 20.75, 20.9, 35.06, 28.64, 
                34.8, 43.06, 44.41, 45.34, 68.07, 35.56, 55.46, 78.07]]

    c_groups = [[4.23, 36.91, 11.13, 15.36, 44.23, 28.45, 26.34, 24.23, 13.45, 8.45, 11.34, 
                18.45, 12.68, 31.99, 12.68, 16.91, 16.13, 17.56, 30.75, 32.91, 21.06, 28.64, 
                24.79, 13.06, 24.41, 37.34, 18.07, 35.57, 21.45, 8.07]]
    

    center, ternary_edge, cartesian_edge = create_ternary_group_distribution_data(ch4_long, c2h2_long, c2h4_long, [100, 75, 50, 25, 0], 3)

# %%

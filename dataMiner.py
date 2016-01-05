import csv
import pygal
from pygal.style import CleanStyle
from datetime import datetime
import numpy as np
import urllib
import random

def download_data(url):
    file = urllib.urlretrieve (url, "test.csv")
    return file

def get_csv_from_file(file):
    file_c = open(file)
    csv_file = csv.reader(file_c)
    return csv_file

def remove_table_headers (csv_file_row):
    return csv_file_row.remove(csv_file_row[0])

def cast_int(csv_file_row):
    return [int(x) for x in csv_file_row]

def create_numpy_array(csv_file_row):
    return np.array(csv_file_row)

def trim_data(data):
    return data [0:29]

def replace_negative_values(data):
    data[data < 0] = 0
    return data

def prepare_data(csv_file):
    crimes_count = []
    solved = []
    recidivism = []
    all = []

    for row in csv_file:
        all.append(row[0])
        crimes_count.append(row[1])
        solved.append(row[2])
        recidivism.append(row[6])

    remove_table_headers(crimes_count)
    remove_table_headers(solved)
    remove_table_headers(recidivism)
    remove_table_headers(all)

    crimes_count = cast_int(crimes_count)
    solved = cast_int(solved)
    recidivism = cast_int(recidivism)
    #all = cast_int(all) - cant go to int because float type

    crimes_count = create_numpy_array(crimes_count)
    replace_negative_values(crimes_count)

    solved = create_numpy_array(solved)
    replace_negative_values(solved)

    recidivism = create_numpy_array(recidivism)
    replace_negative_values(recidivism)

    all = create_numpy_array(all)
    replace_negative_values(all)

    trim_data(crimes_count)
    trim_data(solved)
    trim_data(recidivism)
    trim_data(all)

    final_data = [crimes_count, solved, recidivism, all]

    return final_data

def get_solved_crimes_count(csv_file):
    region_csv = prepare_data(get_csv_from_file(csv_file))
    region_criminality_index = region_csv[1]
    return region_criminality_index

def get_crimes_count(csv_file):
    region_csv = prepare_data(get_csv_from_file(csv_file))
    region_criminality_index = region_csv[0]
    return region_criminality_index

def get_recidive_count(csv_file):
    region_csv = prepare_data(get_csv_from_file(csv_file))
    region_criminality_index = region_csv[2]
    return region_criminality_index

# for region allover data
def get_criminality_index(csv_file):
    region_csv = prepare_data(get_csv_from_file(csv_file))
    region_criminality_index = region_csv[3]
    return region_criminality_index


def create_graph_x_labels(chart):
    chart.x_labels = map(lambda d: d.strftime('%Y-%m-%d'), [
    datetime(2013, 1, 1),
    datetime(2013, 2, 1),
    datetime(2013, 3, 1),
    datetime(2013, 4, 1),
    datetime(2013, 5, 1),
    datetime(2013, 6, 1),
    datetime(2013, 7, 1),
    datetime(2013, 8, 1),
    datetime(2013, 9, 1),
    datetime(2013, 10, 1),
    datetime(2013, 11, 1),
    datetime(2013, 12, 1),
    datetime(2014, 1, 1),
    datetime(2014, 2, 1),
    datetime(2014, 3, 1),
    datetime(2014, 4, 1),
    datetime(2014, 5, 1),
    datetime(2014, 6, 1),
    datetime(2014, 7, 1),
    datetime(2014, 8, 1),
    datetime(2014, 9, 1),
    datetime(2014, 10, 1),
    datetime(2014, 11, 1),
    datetime(2014, 12, 1),
    datetime(2015, 1, 1),
    datetime(2015, 2, 1),
    datetime(2015, 3, 1),
    datetime(2015, 4, 1),
    datetime(2015, 5, 1),
    datetime(2015, 6, 1),
    datetime(2015, 7, 1),
    datetime(2015, 8, 1),
    datetime(2015, 9, 1),
])

def add_graph_chart(caption, data, chart):
    for i in range (caption.__len__()):
        return chart.add(caption, data)

def render_graph(file_name, graph):
    graph.render_to_file(file_name + random.randint(1,10000) + ".svg")

def plot_line_chart(title, data):
    bar_chart = pygal.Line(style=CleanStyle)

    # TODO: implement add_graph_chart_method

    i = 0
    while i <= len(data[0]):
        bar_chart.add(data[[0][i]], data[[1][i]])
        i+= 1

    create_graph_x_labels(bar_chart)

    return bar_chart.render_to_file("test" + str(random.randint(1000,9999)) + ".svg")


solved_crimes = get_solved_crimes_count("fyzicky_utok_praha_full.csv")
recidive_count = get_recidive_count("fyzicky_utok_praha_full.csv")
plot_line_chart("Recidivist at physical attacks", [["Attacks", "Recidivism"],[solved_crimes, recidive_count]])

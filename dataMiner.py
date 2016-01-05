import csv
import pygal
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

get_csv_from_file(download_data("http://www.mapakriminality.cz/data/csv?areacode=001214&crimetype=101-903&timefrom=120&timeto=130"))

def remove_table_headers (csv_file_row):
    return csv_file_row.remove(csv_file_row[0])

def cast_int(csv_file_row):
    return [int(x) for x in csv_file_row]

def create_numpy_array(csv_file_row):
    return np.array(csv_file_row)

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
    all = cast_int(all)

    crimes_count = create_numpy_array(crimes_count)
    crimes_count[crimes_count < 0] = 0
    solved = create_numpy_array(solved)
    solved[solved < 0] = 0
    recidivism = create_numpy_array(recidivism)
    recidivism[recidivism < 0] = 0
    all = create_numpy_array(all)
    all[all < 0] = 0

    trim_data(crimes_count)
    trim_data(solved)
    trim_data(recidivism)
    trim_data(all)

    final_data = [crimes_count, solved, recidivism, all]

    return final_data

def trim_data(data):
    return data [0:29]

def prepare_graph_data():
    pass

def get_solved_crimes_count(csv_file):
    region_csv = prepare_data(get_csv_from_file(file))
    region_criminality_index = region_csv[1]
    return region_criminality_index

def get_crimes_count(csv_file):
    region_csv = prepare_data(get_csv_from_file(file))
    region_criminality_index = region_csv[0]
    return region_criminality_index

def get_recidive_count(csv_file):
    region_csv = prepare_data(get_csv_from_file(file))
    region_criminality_index = region_csv[2]
    return region_criminality_index

def get_criminality_index(csv_file):
    region_csv = prepare_data(get_csv_from_file(file))
    region_criminality_index = region_csv[3]
    return region_criminality_index


date_chart = pygal.Line(x_label_rotation=45)
date_chart._title = 'Marijuana planting'

def create_graph_x_labels():

    year, month, day = (2013, 1, 1)
    i = 0

    date_chart.x_labels = map(lambda d: d.strftime('%Y-%m-%d'), [

    # while i < 29:
    #     month += 1
    #     datetime = datetime(year, month, day)
    #     if i > 12:
    #         month = 1
    #         year += 1
    #         datetime = datetime(year, month, day)


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
])

# date_chart.add("Recidivist", attacks_recidive)
def add_graph_chart(caption, data):

    for i in range (caption):
        date_chart.add(caption, data)

def create_pie_chart(title,caption,data):
    pie_chart = pygal.Pie()
    pie_chart.title = title

    for i in range (caption):
        pie_chart.add(caption, data)

def render_graph(file_name, graph):
    graph.render_to_file(file_name + random.randint(1,10000))



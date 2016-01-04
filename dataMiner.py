import csv
import pygal
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

def get_csv_from_file(file):
    file_c = open(file)
    csv_file = csv.reader(file_c)
    return csv_file

def prepare_data(csv_file):
    crimes = []
    solved = []
    recidivism = []
    all = []

    for row in csv_file:
        all.append(row[0])
        crimes.append(row[1])
        solved.append(row[2])
        recidivism.append(row[6])

    crimes.remove(crimes[0])
    solved.remove(solved[0])
    recidivism.remove(recidivism[0])
    all.remove(all[0])

    crimes = [int(x) for x in crimes]
    solved = [int(x) for x in solved]
    recidivism = [int(x) for x in recidivism]
    all = [float(x) for x in all]

    crimes = np.array(crimes)
    crimes[crimes < 0] = 0
    solved = np.array(solved)
    solved[solved < 0] = 0
    recidivism = np.array(recidivism)
    recidivism[recidivism < 0] = 0
    all = np.array(all)
    all[all < 0] = 0

    crimes = crimes [0:29]
    solved = solved [0:29]
    recidivism = recidivism [0:29]
    all = all [0:29]


    out = [crimes, solved, recidivism, all]

    return out

# murders = prepare_data(get_csv_from_file('vrazdy_praha_full.csv'))
# murders_found = murders[0]
# murders_recidive = murders[2]
#
# rapes = prepare_data(get_csv_from_file('znasilneni_praha_full.csv'))
# rapes_found = rapes[0]
# rapes_recidive = rapes[2]
#
# all = prepare_data(get_csv_from_file('znasilneni_praha_full.csv'))
# rapes_found = rapes[0]


# attacks = prepare_data(get_csv_from_file('fyzicky_utok_praha_full.csv'))
# attacks_found = attacks[0]
# attacks_recidive = attacks[2]
# attacks_found_sum = sum(attacks_found)
# print attacks_found_sum
# attacks_recidive_sum = sum(attacks_recidive)
# print attacks_recidive_sum
# print attacks

cr = prepare_data(get_csv_from_file('celkova_cr.csv'))
cr1 = cr[3]
print (cr1)
hk = prepare_data(get_csv_from_file('celkova_hk.csv'))
hk1 = hk[3]
jc = prepare_data(get_csv_from_file('celkova_jc.csv'))
jc1 = jc[3]
jmk = prepare_data(get_csv_from_file('celkova_jmk.csv'))
jmk1 = jmk[3]
karlov = prepare_data(get_csv_from_file('celkova_karlov.csv'))
karlov1 = karlov[3]
lib = prepare_data(get_csv_from_file('celkova_lib.csv'))
lib1 = lib[3]
mszk = prepare_data(get_csv_from_file('celkova_mszk.csv'))
mszk1 = mszk[3]
olm = prepare_data(get_csv_from_file('celkova_olm.csv'))
olm1 = olm[3]
pard = prepare_data(get_csv_from_file('celkova_pard.csv'))
pard1 = pard[3]
plz = prepare_data(get_csv_from_file('celkova_plz.csv'))
plz1 = plz[3]
praha = prepare_data(get_csv_from_file('celkova_praha.csv'))
praha1 = praha[3]
stred = prepare_data(get_csv_from_file('celkova_stredocesky.csv'))
stred1 = stred[3]
usti = prepare_data(get_csv_from_file('celkova_usti.csv'))
usti1 = usti[3]
vys = prepare_data(get_csv_from_file('celkova_vys.csv'))
vys1 = vys[3]
zlin = prepare_data(get_csv_from_file('celkova_zlin.csv'))
zlin1 = zlin[3]



date_chart = pygal.Line(x_label_rotation=45)
date_chart._title = 'Marijuana planting'
date_chart.x_labels = map(lambda d: d.strftime('%Y-%m-%d'), [
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
datetime(2014, 10,1),
datetime(2014, 11, 1),
datetime(2014, 12, 1),
datetime(2015, 1, 1),
datetime(2015, 2, 1),
datetime(2015, 3, 1),
datetime(2015, 4, 1),
datetime(2015, 5, 1)])

# date_chart.add("Recidivist", attacks_recidive)
date_chart.add('CR', cr1)
date_chart.add('Hradecky', hk1)
date_chart.add('Jihocesky', jc1)
date_chart.add('Jihomoravsky', jmk1)
date_chart.add('Karlovarsky', karlov1)
date_chart.add('Liberecky', lib1)
date_chart.add('Moravskoslezsky', mszk1)
date_chart.add('Olomoucky', olm1)
date_chart.add('Pardubicky', pard1)
date_chart.add('Plzensky', plz1)
date_chart.add('Praha', praha1)
date_chart.add('Stredocesky', stred1)
date_chart.add('Ustecky', usti1)
date_chart.add('Vysocina', vys1)
date_chart.add('Zlin', zlin1)


# date_chart.add('Olomouc', gandza_found_2)
# date_chart.add('Stredocesky', gandza_found_3)
# date_chart.add('Jihomoravsky', gandza_found_4)
# date_chart.add('Jihocesky', gandza_found_5)
# date_chart.add('Attacks', attacks_found)

date_chart.render_to_file('example.svg')

# pie_chart = pygal.Pie()
# pie_chart.title = 'Recidivists in physical attack (in %)'
# pie_chart.add('Recidivists', 66.11)
# pie_chart.add('New', 33.89)
# pie_chart.render_to_file('example2.svg')



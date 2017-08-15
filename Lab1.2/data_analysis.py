from matplotlib import pyplot
from openpyxl import load_workbook


def getvalue(x):
    return x.value

wb=load_workbook('data_analysis_lab-1.xlsx')
sheet=wb['Data']
years=list(map(getvalue, sheet['A'][1:]))
relations=list(map(getvalue,sheet['B'][1:]))
sunactivity=list(map(getvalue, sheet['C'][1:]))

pyplot.plot(years, relations, label='отношения')
pyplot.plot(years, sunactivity, label = 'активность')
pyplot.show()

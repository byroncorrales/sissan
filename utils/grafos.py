from pygooglechart import PieChart3D, PieChart2D 
from pygooglechart import StackedHorizontalBarChart, StackedVerticalBarChart
from pygooglechart import GroupedHorizontalBarChart, GroupedVerticalBarChart
from pygooglechart import Axis, SimpleLineChart
from django.utils import simplejson
from django.http import HttpResponse

pie_types = [PieChart3D, PieChart2D]
bar_types = [StackedHorizontalBarChart, StackedVerticalBarChart,
             GroupedHorizontalBarChart, GroupedVerticalBarChart]
line_types = [SimpleLineChart]


def make_graph(data, legends, message=None, 
               axis_labels=None, steps=4, return_json = True,
               type=PieChart3D, size=(600, 350), multiline=False):

    if (type in pie_types):
        graph = __pie_graphic__(data, legends, size, type)
    elif (type in bar_types):
        graph = __bar_graphic__(data, legends, axis_labels, size,
                               steps, type, multiline)
    elif(type in line_types):
        graph = __line_strip_graphic__(data, legends, axis_labels,
                                       size, steps, type, multiline)

    graph.set_title(message)

    if return_json:
        dicc = {'url': graph.get_url()}
        return HttpResponse(simplejson.dumps(dicc), mimetype='application/javascript')
    else:
        return graph.get_url()


def __pie_graphic__(data, legends, size, type=PieChart3D):
    graph = type(size[0], size[1])
    graph.set_colours([ 'FFBC13','22A410','E6EC23','2B2133','BD0915','3D43BD'])
    graph.add_data(data)
    graph.set_legend(legends)
    porcentajes = saca_porcentajes(data)
    graph.set_pie_labels(porcentajes)
    graph.set_legend_position("b")

    return graph

def __bar_graphic__(data, legends, axis_labels, size, steps,  
                    type=StackedVerticalBarChart, multiline=False):
    
    if multiline:
        max_values = []
        min_values = [] 
        for row in data:
            max_values.append(max(row))
            min_values.append(min(row))
        max_value = max(max_values)
        min_value = min(min_values)
    else:
        max_value = max(data)
        min_value = min(data)

    step = ((max_value*1.05)-(min_value*0.95))/steps
    left_axis = range(int(min_value*0.95), int(max_value*1.05), int(step))
    left_axis[0]=''

    if type==StackedHorizontalBarChart:
        graph = StackedHorizontalBarChart(size[0], size[1], x_range=(0, max_value*1.05))
        graph.set_axis_labels(Axis.BOTTOM, left_axis)
        graph.set_axis_labels(Axis.LEFT, axis_labels)
    elif type==StackedVerticalBarChart:
        graph = StackedVerticalBarChart(size[0], size[1], y_range=(0, max_value*1.05))
        graph.set_axis_labels(Axis.LEFT, left_axis)
        graph.set_axis_labels(Axis.BOTTOM, axis_labels)
    elif type==GroupedHorizontalBarChart:
        graph = GroupedHorizontalBarChart(size[0], size[1], x_range=(0, max_value*1.05))
        graph.set_axis_labels(Axis.BOTTOM, left_axis)
        graph.set_axis_labels(Axis.LEFT, axis_labels)
        graph.set_bar_spacing(5)
    elif type==GroupedVerticalBarChart:
        graph = GroupedVerticalBarChart(size[0], size[1], y_range=(0, max_value*1.05))
        graph.set_axis_labels(Axis.LEFT, left_axis)
        graph.set_axis_labels(Axis.BOTTOM, axis_labels)
        graph.set_bar_spacing(5)
    else:
        pass #raise exception


    if multiline:
        for fila in data:
            graph.add_data(fila)
    else:
        graph.add_data(data)
    
    graph.set_colours([ 'FFBC13','22A410','E6EC23','2B2133','BD0915','3D43BD'])
    graph.set_bar_width(40)
    graph.set_legend(legends)
    graph.set_legend_position('b')
    
    
    return graph

def __line_strip_graphic__(data, legends, axis_labels, size, steps, 
                           type=SimpleLineChart, multiline=False):
    if multiline:
        max_values = []
        min_values = [] 
        for row in data:
            max_values.append(max(row))
            min_values.append(min(row))
        max_y = max(max_values)
        min_y = min(min_values)
    else:
        max_y = max(data)
        min_y = min(data)

    chart = SimpleLineChart(size[0], size[1], y_range=[0, max_y*1.05])

    if multiline:
        for row in data:
            chart.add_data(row)
    else:
        chart.add_data(data)
    
    step = ((max_y*1.05)-(min_y*0.95))/steps
    left_axis = range(int(min_y*0.95), int(max_y*1.05), int(step))
    left_axis[0]=''
    chart.set_axis_labels(Axis.LEFT, left_axis)
    chart.set_colours([ 'FFBC13','22A410','E6EC23','2B2133','BD0915','3D43BD'])

    chart.set_axis_labels(Axis.BOTTOM, axis_labels)
    chart.set_legend(legends)
    chart.set_legend_position('b')

    return chart


def saca_porcentajes(values):
    """sumamos los valores y devolvemos una lista con su porcentaje"""
    total = sum(values)
    valores = [] 
    for i in range(len(values)):
        porcentaje = (float(values[i])/total)*100
        valores.append("%.2f" % porcentaje + '%')
    return valores

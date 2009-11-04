from pygooglechart import PieChart3D, PieChart2D 
from pygooglechart import StackedHorizontalBarChart, StackedVerticalBarChart
from pygooglechart import Axis, SimpleLineChart
from django.utils import simplejson
from django.http import HttpResponse

def make_graph(data, legends, message=None, 
               axis_labels=None, steps=4, return_json = True,
               type=PieChart3D, size=(600, 350)):

    if (type==PieChart3D or type==PieChart2D):
        graph = __pie_graphic__(data, legends, size, type)
    elif (type==StackedHorizontalBarChart or type==StackedVerticalBarChart):
        graph = __bar_graphic__(data, legends, type, size)

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

def __bar_graphic__(data, legends, axis_labels, size,  type=StackedVerticalBarChart):
    #if type==StackedHorizontalBarChart:
    #    graph = StackedHorizontalBarChart(size[0], size[1], x_range=range)
    #else
    #    graph = StackedVerticalBarChart(size[0], size[1], y_range=range)
    
    #graph.set_colours(['FF0000', '00FF00'])
    #graph.set_bar_width(5)
    #graph.set_bar_spacing(5)
    #graph.set_legend(legends)
    #graph.set_axis_labels(Axis.BOTTOM, axis_labels)

    #for fila in data:
    #    if (type(foo)==type([])):
    #        graph.add_data(fila)
    #    else:
    #        #raise exception
    #        pass
    pass

def __line_strip_graphic__(data, legends, axis_labels, size, steps, 
                           type=SimpleLineChart, multi_line=False):
    if multi_line:
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

    chart = SimpleLineChart(size[0], size[1], y_range=[0, max_y*1.15])

    if multi_line:
        for row in data:
            chart.add_data(row)
    else:
        chart.add_data(data)
    
    step = ((max_y*1.25)-(min_y*0.75))/steps
    left_axis = range(int(min_y*0.75), int(max_y*1.25), int(step))
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

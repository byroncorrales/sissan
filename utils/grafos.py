from pygooglechart import PieChart3D, PieChart2D, StackedHorizontalBarChart, StackedVerticalBarChart
from django.utils import simplejson
from django.http import HttpResponse

def make_graphic(data, legends, message=None, return_json = True, type=PieChart3D, size=(600, 350)):
    if (type==PieChart3D or type==PieChart2D):
        graph = __pie_graphic__(data, legends, size, type)
    elif (type==StackedHorizontalBarChart or type==StackedVerticalBarChart):
        graph = __bar_graphic__(data, legends, type, size)

    graph.set_title(message)

    if return_json:
        dicc = {'url': graph.get_url()}
        return HttpResponse(simplejson.dumps(dict), mimetype='application/javascript')
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

def __bar_graphic__(data, legends, size,  type=StackedVerticalBarChart):
    #if type==StackedHorizontalBarChart:
    #    graph = StackedHorizontalBarChart(size[0], size[1], x_range=range)
    #else
    #    graph = StackedVerticalBarChart(size[0], size[1], y_range=range)
    
    #graph.set_colours(['FF0000', '00FF00'])
    #graph.set_bar_width(5)
    #graph.set_bar_spacing(5)
    #graph.set_legend(legends)

    #for fila in data:
    #    if (type(foo)==type([])):
    #        graph.add_data(fila)
    #    else:
    #        #raise exception
    #        pass
    pass

def saca_porcentajes(values):
    """sumamos los valores y devolvemos una lista con su porcentaje"""
    total = sum(values)
    valores = [] 
    for i in range(len(values)):
        porcentaje = (float(values[i])/total)*100
        valores.append("%.2f" % porcentaje + '%')
    return valores

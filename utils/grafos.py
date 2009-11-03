from pygooglechart import PieChart3D, PieChart2D
from django.utils import simplejson
from django.http import HttpResponse

def make_graphic(data, legends, message=None, return_json = True, type=PieChart3D):
    graph = type(600,350)
    graph.set_colours([ 'FFBC13','22A410','E6EC23','2B2133','BD0915','3D43BD'])
    graph.add_data(data)
    graph.set_legend(legends)
    porcentajes = saca_porcentajes(data)
    graph.set_pie_labels(porcentajes)
    graph.set_legend_position("b")
    graph.set_title(message)

    if return_json:
        dicc = {'url': graph.get_url()}
        return HttpResponse(simplejson.dumps(dict), mimetype='application/javascript')
    else:
        return graph.get_url()

def saca_porcentajes(values):
    """sumamos los valores y devolvemos una lista con su porcentaje"""
    total = sum(values)
    valores = [] 
    for i in range(len(values)):
        porcentaje = (float(values[i])/total)*100
        valores.append("%.2f" % porcentaje + '%')
    return valores

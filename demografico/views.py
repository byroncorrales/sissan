from django.shortcuts import render_to_response
from demografico.models import Poblacion
from lugar.models import Departamento
from django.db.models import Avg, Sum
import datetime

CHOICESANO=[]
for i in range (datetime.date.today().year,1989,-1):
	CHOICESANO.append((i,str(i)))

def poblacion(request):
	return render_to_response('demografico/poblacion.html')

def consulta_ano (request):
	ano_consulta = request.GET.get('ano_form', '')
	dept_consulta = request.GET.get('dept_form', '')
	tipo_consulta = request.GET.get('tipo_form', '')
	dept = Departamento.objects.all()
	if ano_consulta and dept_consulta and tipo_consulta:
		if dept_consulta=="Nacional":
			query= Poblacion.objects.filter(ano=ano_consulta)
			dept_caption=""
			total = Poblacion.objects.filter(ano=ano_consulta).aggregate(Sum('total_ambos_sexos'),Sum('total_hombre'),Sum('total_mujer'),Sum('urbano_hombre'),Sum('urbano_mujer'),Sum('rural_mujer'),Sum('rural_hombre'),Sum('rural_ambos_sexos'),Sum('urbano_ambos_sexos'))
		else:
			dept_caption = Departamento.objects.get(pk=dept_consulta)
			query= Poblacion.objects.filter(ano=ano_consulta).filter(departamento=dept_consulta)
			total=0
		if tipo_consulta=="ubicacion":
			return render_to_response('demografico/poblacion_ubicacion.html', {'q':query,'ano_salida':ano_consulta,'dept_salida':dept_consulta, 'tipo_salida':tipo_consulta,'ano':CHOICESANO,'dept':dept,'dept_caption':dept_caption,'total':total})
		if tipo_consulta=="sexo":
			return render_to_response('demografico/poblacion_sexo.html', {'q':query,'ano_salida':ano_consulta,'dept_salida':dept_consulta, 'tipo_salida':tipo_consulta,'ano':CHOICESANO,'dept':dept,'dept_caption':dept_caption,'total':total})
		if tipo_consulta=="sexoyubic":
			return render_to_response('demografico/poblacion_sexoyubic.html', {'q':query,'ano_salida':ano_consulta,'dept_salida':dept_consulta, 'tipo_salida':tipo_consulta,'ano':CHOICESANO,'dept':dept,'dept_caption':dept_caption,'total':total})
	else:
		return render_to_response('demografico/poblacion_consulta_ano.html', {'ano':CHOICESANO,'dept':dept})

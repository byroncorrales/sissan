from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from models import *
from utils import convertir_mes
from django.template.defaultfilters import slugify
from django.db.models import Avg, Min, Max, Sum
#from forms import AnoFilterForm

def index(request):
    return render_to_response('economico/index.html')

def salario_minimo(request, ano_inicial=None, ano_final=None, sector=None):
    dicc = __salario_minimo__(request, ano_inicial, ano_final, sector)
    return render_to_response('economico/salario_minimo.html', dicc)
    
def __salario_minimo__(request, ano_inicial=None, ano_final=None, sector=None):
    rango = SalarioMinimo.objects.all().aggregate(minimo=Min('ano'), maximo=Max('ano'))
    sectores_all = Sector.objects.all()
    try:
        rango_anos = range(rango['minimo'], rango['maximo']+1)
    except:
        rango_anos=None
    mes = False
    if sector:
        sector = get_object_or_404(Sector, slug=sector)
        sectores = [sector]
    else:
        sectores = sectores_all 

    resultados = [] 
    promedios = []

    if ano_inicial and ano_final:
        for ano in range(int(ano_inicial), int(ano_final)+1):
            fila = {'ano':ano ,'datos': []}
            for sector in sectores:
                try:
                    salario = SalarioMinimo.objects.filter(ano=ano, sector=sector).aggregate(valor=Avg('salario'))
                    tmp = salario['valor']
                    fila['datos'].append("%.2f" % tmp)
                except:
                    fila['datos'].append(0)
            resultados.append(fila)
            
    elif ano_inicial:
        fila = {'ano': ano_inicial, 'mes':0, 'datos': []}
        mes = True
        for sector in sectores:
            promedio = SalarioMinimo.objects.filter(ano=ano_inicial, sector=sector).aggregate(prom=Avg('salario'))
            promedios.append(promedio['prom'])

        for i in range(1,13):
            fila['mes'] = convertir_mes(i)
            fila['datos']=[]
            for sector in sectores:
                try:
                    dato = SalarioMinimo.objects.get(ano=ano_inicial, mes=i, sector=sector)
                    fila['datos'].append(dato.salario)
                except:
                    fila['datos'].append(0)
            temp = dict.copy(fila)
            resultados.append(temp)
    else:
        try:
            for ano in rango_anos:
                fila = {'ano':ano ,'datos': []}
                for sector in sectores:
                    try:
                        salario = SalarioMinimo.objects.filter(ano=ano, sector=sector).aggregate(valor=Avg('salario'))
                        tmp = salario['valor']
                        fila['datos'].append("%.2f" % tmp)
                    except:
                        fila['datos'].append(0)
                resultados.append(fila)
        except TypeError:
                fila = {'ano':0 ,'datos': []}
    
    #variaciones
    variaciones = []
    if fila.has_key('mes')==False:
        tope = len(resultados)-1
        for i in range(len(sectores)):
            try:
                variacion = ((float(resultados[tope]['datos'][i]) - float(resultados[0]['datos'][i]))/float(resultados[0]['datos'][i])*100) if resultados[0]['datos'][i]!= None else 0
            except:
                variacion = 0
            variaciones.append("%.2f" % variacion)
    
    dicc = {'datos': resultados, 'sectores': sectores, 'rango': rango_anos, 'sectores_all': sectores_all,
            'variaciones': variaciones, 'tiene_mes': mes, 'promedios': promedios}
    return dicc

def empleo(resquest, ano_inicial=None, ano_final=None):
    dicc = __empleo__(resquest, ano_inicial, ano_final)
    return render_to_response("economico/empleo.html", dicc)
    
def __empleo__(resquest, ano_inicial=None, ano_final=None):
    anos = []
    anos = FuerzaTrabajo.objects.all().aggregate(minimo = Min('ano'), maximo = Max('ano'))
    try:
        rango_anos = range(rango_anos['minimo'], rango_anos['maximo']+1)
    except:
        rango_anos = None
    if ano_inicial and ano_final:
        #rango de aos
        datos = FuerzaTrabajo.objects.filter(ano__range=(ano_inicial, ano_final))
        anos = range(int(ano_inicial), int(ano_final)+1)
        mensaje = 'Empleo (%s-%s)'  % (ano_inicial, ano_final)
    elif ano_inicial:
        #ano especifico
        datos = FuerzaTrabajo.objects.filter(ano=ano_inicial)
        anos.append(ano_inicial)
        mensaje = 'Empleo (%s)'
    else:
        #todos los anos
        #sacar ano max y ano min!
        datos = FuerzaTrabajo.objects.all()
        mensaje = 'Empleo ' 

    pea_poblacion = []  #PEA/Poblacion
    tasa_de_ocupacion = []#total_ocupados/total PEA
    tasa_de_desempleo = []  #100-tasa ocupacion || desempleo abierto/poblacion
    tasa_sub_empleo = [] #sabra Dios...

    for dato in datos:
        calc_pea_poblacion = (float(dato.pea_general)/dato.poblacion_total)*100 
        pea_poblacion.append("%.2f" % calc_pea_poblacion)
        calc_tasa_de_ocupacion = (float(dato.total_ocupados)/dato.pea_general) * 100
        tasa_de_ocupacion.append("%.2f" % calc_tasa_de_ocupacion)
        calc_tasa_de_desempleo = 100-calc_pea_poblacion
        tasa_de_desempleo.append("%.2f" % calc_tasa_de_desempleo)
        #calc_tasa_sub_empleo = #???
        #tasa_sub_empleo.append("%.2f" % calc_tasa_sub_empleo)
    
    dicc = {'datos': datos, 'pea_poblacion': pea_poblacion, 
            'tasa_de_ocupacion': tasa_de_ocupacion, 'tasa_de_desempleo': tasa_de_desempleo,
            'tasa_sub_empleo': tasa_sub_empleo, 'anos': rango_anos, 'mensaje': mensaje}
    return dicc

def canasta_basica(request, tipo=None, ano_inicial=None, ano_final=None):
    dicc = __canasta_basica__(request, tipo, ano_inicial, ano_final)
    template_name = dicc['template']
    del(dicc['template'])
    return render_to_response(template_name, dicc)
    
def __canasta_basica__(request, tipo=None, ano_inicial=None, ano_final=None):
    columnas = []
    anos = CanastaBasica.objects.all().aggregate(maximo=Max('ano'), minimo=Min('ano'))
    try:
        rango_anos = range(anos['minimo'], anos['maximo']+1)
    except:
        rango_anos = None

    tipos_all = TipoCanastaBasica.objects.all()

    if tipo:
        tipo = get_object_or_404(TipoCanastaBasica, slug__iexact=tipo)
        tipos = [tipo]
    else:
        tipos = tipos_all

    resultados = []
    template_name = 'economico/canasta_basica.html'
    if ano_inicial and ano_final:
        for ano in range(int(ano_inicial), int(ano_final)+1):
            filita = {'ano': ano, 'datos': []}
            for tipo in tipos:
                canastas = CanastaBasica.objects.filter(ano=ano, tipo=tipo).aggregate(costo=Avg('costo'))
                filita['datos'].append(canastas['costo'])
            resultados.append(filita)
    elif ano_inicial:
        filita = {'ano': ano_inicial,'mes': 0, 'datos': []}
        for i in range(1,13):
            filita['mes']=convertir_mes(i)
            filita['datos'] = []
            for tipo in tipos:
                try:
                    canastas = CanastaBasica.objects.get(ano=ano_inicial, tipo=tipo, mes=i)
                    filita['datos'].append(canastas.costo)
                except:
                    filita['datos'].append(0)
            temp = dict.copy(filita)#para romper la byref
            resultados.append(temp)
        template_name='economico/canasta_basica_mes.html'
    else:
        try:
            for ano in rango_anos:
                filita = {'ano': ano, 'datos': []}
                for tipo in tipos:
                    canastas = CanastaBasica.objects.filter(ano=ano, tipo=tipo).aggregate(costo=Avg('costo'))
                    filita['datos'].append(canastas['costo'])
                resultados.append(filita)
        except TypeError:
            pass
    
    variaciones = [] 
    for tipo in tipos:
        columnas.append(tipo.tipo)

    tope = len(resultados)-1
    for i in range(len(tipos)):
        #variaciones
        try:
            variacion = ((resultados[tope]['datos'][i] - resultados[0]['datos'][i])/ resultados[0]['datos'][i])*100
            variaciones.append(variacion)
        except:
            variaciones.append(0)
        
    dicc = {'datos':resultados, 'columnas': columnas, 'variaciones': variaciones,
            'tipos_all': tipos_all, 'rango': rango_anos, 'template': template_name}
    return dicc

def mercados(request, departamento=None, municipio=None):
    dicc = __mercados__(request, departamento, municipio)
    return render_to_response("economico/mercados.html", dicc)

def __mercados__(request, departamento=None, municipio=None):
    departamentos = Departamento.objects.all()
    if departamento:
        datos = get_list_or_404(Mercado, departamento__id=departamento)
        mensaje = "Mercados del departamento de %s" % datos[0].departamento.nombre
    elif municipio:
        datos = get_list_or_404(Mercado, municipio__id=municipio)
        mensaje = "Mercados del municipio de %s" % datos[0].municipio.nombre
    else:
        datos = Mercado.objects.all()
        mensaje="Todos los mercados"

    dicc = {'mercados': datos, 'mensaje': mensaje, 'departamentos': departamentos}
    return dicc

def salario_nominal_real(request, ano_inicial=None, ano_final=None):
    dicc = __salario_nominal_real__(request, ano_inicial, ano_final)
    return render_to_response('economico/salario_nominal_real.html', dicc)

def __salario_nominal_real__(request, ano_inicial=None, ano_final=None):
    mes = False
    resultados = [] 

    if ano_inicial and ano_final:
        for ano in range(int(ano_inicial), int(ano_final)+1):
            fila = {'ano':ano ,'datos': []}
            try:
                salario_nominal = SalarioNominal.objects.filter(ano=ano).aggregate(asegurados=Avg('asegurados_inss'),
                                                                                   gobierno=Avg('gobierno_central'),
                                                                                   nacional=Avg('salario_nacional'))
                fila['datos'].append(salario_nominal['asegurados'])
                fila['datos'].append(salario_nominal['gobierno'])
                fila['datos'].append(salario_nominal['nacional'])
            except:
                salario_nominal = {'asegurados': 0, 'gobierno': 0, 'nacional':0}
                for key in salario_nominal.keys():
                    fila['datos'].append(0)
                
            try:
                salario_real= SalarioReal.objects.filter(ano=ano).aggregate(asegurados=Avg('asegurados_inss'),
                                                                                           gobierno=Avg('gobierno_central'),
                                                                                           nacional=Avg('salario_nacional'))
                fila['datos'].append(salario_real['asegurados'])
                fila['datos'].append(salario_real['gobierno'])
                fila['datos'].append(salario_real['nacional'])
            except:
                salario_real = {'asegurados': 0, 'gobierno': 0, 'nacional':0}
                for key in salario_real.keys():
                    fila['datos'].append(0)

            #variaciones del salario real 
            for key in salario_nominal.keys():
                variacion = ((salario_nominal[key] - salario_real[key])/salario_nominal[key])*100
                fila['datos'].append(variacion)
            temp = dict.copy(fila)
            resultados.append(temp)
            
    elif ano_inicial:
        fila = {'ano': ano_inicial, 'mes':0, 'datos': []}
        mes = True
        for i in range(1,13):
            fila['mes'] = convertir_mes(i)
            fila['datos']=[]
            try:
                dato = SalarioNominal.objects.get(ano=ano_inicial, mes=i)
                fila['datos'].append(dato.asegurados_inss)
                fila['datos'].append(dato.gobierno_central)
                fila['datos'].append(dato.salario_nacional)
            except:
                fila['datos'].append(0)
                fila['datos'].append(0)
                fila['datos'].append(0)
            try:
                dato = SalarioReal.objects.get(ano=ano_inicial, mes=i)
                fila['datos'].append(dato.asegurados_inss)
                fila['datos'].append(dato.gobierno_central)
                fila['datos'].append(dato.salario_nacional)
            except:
                fila['datos'].append(0)
                fila['datos'].append(0)
                fila['datos'].append(0)
            temp = dict.copy(fila)
            resultados.append(temp)
    else:
        rango_nominal = SalarioNominal.objects.all().aggregate(minimo=Min('ano'), maximo=Max('ano'))
        rango_real = SalarioNominal.objects.all().aggregate(minimo=Min('ano'), maximo=Max('ano'))
        rango = {'minimo':0, 'maximo':0}

        if rango_nominal['minimo'] == None and rango_nominal['maximo']==None:
            rango_nominal={'minimo': 0, 'maximo': 0}
        if rango_real['minimo'] == None and rango_real['maximo']==None:
            rango_real={'minimo': 0, 'maximo': 0}

        if rango_nominal['minimo']<=rango_real['minimo']:
            rango['minimo']=rango_nominal['minimo']
        else:
            rango['minimo']=rango_real['minimo']

        if rango_nominal['maximo']<=rango_real['maximo']:
            rango['maximo']=rango_nominal['maximo']
        else:
            rango['maximo']=rango_real['maximo']
        
        for ano in range(rango['minimo'], rango['maximo']+1):
            fila = {'ano':ano ,'datos': []}
            try:
                salario_nominal = SalarioNominal.objects.filter(ano=ano).aggregate(asegurados=Avg('asegurados_inss'), 
                                                                                                 gobierno=Avg('gobierno_central'),
                                                                                                 nacional=Avg('salario_nacional'))
                for key in salario_nominal.keys():
                    fila['datos'].append(salario_nominal[key])
            except:
                salario_nominal = {'asegurados': 0, 'gobierno': 0, 'nacional':0}
                for key in salario_nominal.keys():
                    fila['datos'].append(0)
                
            try:
                salario_real= SalarioReal.objects.filter(ano=ano).aggregate(asegurados=Avg('asegurados_inss'),
                                                                                           gobierno=Avg('gobierno_central'),
                                                                                           nacional=Avg('salario_nacional'))
                for key in salario_real.keys():
                    fila['datos'].append(salario_real[key])
            except:
                salario_real = {'asegurados': 0, 'gobierno': 0, 'nacional':0}
                for key in salario_real.keys():
                    fila['datos'].append(0)
            #variaciones del salario real 
            for key in salario_nominal.keys():
                try:
                    variacion = ((salario_nominal[key] - salario_real[key])/salario_nominal[key])*100
                except TypeError:
                    variacion = 0
                fila['datos'].append(variacion)
            temp = dict.copy(fila)
            resultados.append(temp)
        

    #variaciones
    variaciones = []
    if fila.has_key('mes')==False:
        tope = len(resultados)-1
        for i in range(len(resultados[0]['datos'])):
            try:
                variacion = ((float(resultados[tope]['datos'][i]) - 
                              float(resultados[0]['datos'][i]))/float(resultados[0]['datos'][i])*100) 
            except:
                variacion=0
            variaciones.append(variacion)
    
    dicc = {'datos': resultados, 'variaciones': variaciones,
            'tiene_mes': mes}
    return dicc

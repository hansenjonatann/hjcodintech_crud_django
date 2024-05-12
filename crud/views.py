from django.shortcuts import render , redirect
from .models import BahasaPemograman , Sintaks , Variabel , Program

# Create your views here.
def getBahasaPemograman(request):
  bahasa_pemograman = BahasaPemograman.objects.all()
  return render(request=request , template_name='bahasa_pemograman/index.html' , context={'list_bahasa_pemograman': bahasa_pemograman})

def addBahasaPemograman(request):
  return render(request=request , template_name='bahasa_pemograman/create.html')

def storeBahasaPemograman(request):
  nama_bahasa_field = request.POST['nama_bahasa_pemograman']
  tahun_rilis_field = request.POST['tahun_rilis_bahasa']
  bahasa_pemograman = BahasaPemograman(nama_bahasa = nama_bahasa_field , tahun_rilis = tahun_rilis_field)
  bahasa_pemograman.save()
  return redirect('/bahasapemograman')

def editBahasaPemograman(request , id):
  bahasa_pemograman = BahasaPemograman.objects.get(id=id)
  return render(request=request , template_name='bahasa_pemograman/edit.html' , context={'bahasa': bahasa_pemograman})

def updateBahasaPemograman(request , id):
  nama_bahasa_field = request.POST['nama_bahasa_pemograman']
  tahun_rilis_field = request.POST['tahun_rilis_bahasa']
  bahasa_pemograman = BahasaPemograman.objects.get(id=id)
  bahasa_pemograman.nama_bahasa = nama_bahasa_field
  bahasa_pemograman.tahun_rilis = tahun_rilis_field
  bahasa_pemograman.save()
  return redirect('/bahasapemograman')

def deleteBahasaPemograman(request , id):
  bahasa_pemograman = BahasaPemograman.objects.get(id=id)
  bahasa_pemograman.delete()
  return redirect('/bahasapemograman')


#  Views Sintaks
def getSintaks(request):
  sintaks = Sintaks.objects.all()
  return render(request=request , template_name='sintaks/index.html' , context={'list_sintak': sintaks})

def addSintaks(request):
  return render(request=request , template_name='sintaks/create.html')

def storeSintaks(request):
  nama_sintaks_field = request.POST['nama_sintaks']
  sintaks = Sintaks(nama_sintaks = nama_sintaks_field)
  sintaks.save()
  return redirect('/sintaks')

def editSintaks(request , id):
  sintaks = Sintaks.objects.get(id=id)
  return render(request=request , template_name='sintaks/edit.html' , context={'sintaks': sintaks})

def updateSintaks(request , id):
  nama_sintaks_field = request.POST['nama_sintaks_field']
  sintaks = Sintaks.objects.get(id=id)
  sintaks.nama_sintaks = nama_sintaks_field
  sintaks.save()
  return redirect('/sintaks')

def deleteSintaks(request , id):
  sintaks = Sintaks.objects.get(id=id)
  sintaks.delete()
  return redirect('/sintaks')


#  Views Variabel 
def getVariabel(request):
  variabel = Variabel.objects.all()
  return render(request=request , template_name='variabel/index.html' , context={'list_variabel': variabel})

def addVariabel(request):
  return render(request=request , template_name='variabel/create.html')

def storeVariabel(request):
  nama_variabel_field = request.POST['nama_variabel']
  variabel = Variabel(nama_variabel = nama_variabel_field)
  variabel.save()
  return redirect('/variabel')

def editVariabel(request , id):
  variabel = Variabel.objects.get(id=id)
  return render(request=request , template_name='variabel/edit.html' , context={'variabel': variabel})

def updateVariabel(request , id):
  nama_variabel_field = request.POST['nama_variabel_field']
  variabel = Variabel.objects.get(id=id)
  variabel.nama_variabel = nama_variabel_field
  variabel.save()
  return redirect('/variabel')

def deleteVariabel(request , id):
    variabel = variabel.objects.get(id=id)
    variabel.delete()
    return redirect('/variabel')

#  Views Program
def getProgram(request):
  program = Program.objects.select_related('bahasa' , 'sintaks' , 'variabel').all()
  return render(request=request , template_name='index.html' , context={'list_program' : program})

def createProgram(request):
  bahasa = BahasaPemograman.objects.all()
  sintaks = Sintaks.objects.all()
  variabel = Variabel.objects.all()
  return render(request=request , template_name='create.html', context={'list_bahasa' : bahasa , 'list_sintaks' : sintaks , 'list_variabel' : variabel})

def storeProgram(request):
  nama_program_field = request.POST['nama_program']
  bahasa_field = request.POST['bahasa_field']
  sintaks_field = request.POST['sintaks_field']
  variabel_field = request.POST['variabel_field']

  try: 
    bahasa_instance = BahasaPemograman.objects.get(id=bahasa_field)
  except BahasaPemograman.DoesNotExist:
    bahasa_instance = None
  
  try: 
    sintaks_instance = Sintaks.objects.get(id=sintaks_field)
  except Sintaks.DoesNotExist:
    sintaks_instance = None

  try: 
    variabel_instance = Variabel.objects.get(id=variabel_field)
  except BahasaPemograman.DoesNotExist:
    variabel_instance = None

  program = Program(nama_program = nama_program_field , bahasa=bahasa_instance , sintaks=sintaks_instance , variabel=variabel_instance)
  program.save()
  return redirect('/')


def editProgram(request, id):
  program = Program.objects.get(id=id)
  return render(request=request , template_name='edit.html' , context={'program' : program})

def updateProgram(request, id):
  nama_program_field = request.POST['nama_program_field_input']
  program = Program.objects.get(id=id)
  program.nama_program = nama_program_field
  program.save()
  return redirect('/')

def deleteProgram(request , id):
  program = Program.objects.get(id=id)
  program.delete()
  return redirect('/')

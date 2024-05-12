from django.urls import path 
from . import views

urlpatterns = [
  path('bahasapemograman/' , views.getBahasaPemograman , name='getbahasapemograman'),
  path('bahasapemograman/addbahasapemograman' , views.addBahasaPemograman , name='addbahasapemograman'),
  path('bahasapemograman/storebahasapemograman' , views.storeBahasaPemograman , name='storebahasapemograman'),
  path('bahasapemograman/editbahasapemograman/<int:id>' , views.editBahasaPemograman , name='editbahasapemograman'),
  path('bahasapemgoraman/updatebahasapemograman/<int:id>' , views.updateBahasaPemograman , name='updatebahasapemograman'),
  path('bahasapemograman/deletebahasapemograman/<int:id>' , views.deleteBahasaPemograman , name='deletebahasapemograman'),

  #  Path Sintaks
  path('sintaks/' , views.getSintaks , name='getsintaks'),
  path('sintaks/addsintaks' , views.addSintaks , name='addsintaks'),
  path('sintaks/storesintaks' , views.storeSintaks , name='storesintaks'),
  path('sintaks/editsintaks/<int:id>' , views.editSintaks , name='editsintaks'),
  path('sintaks/updatesintaks/<int:id>' , views.updateSintaks , name='updatesintaks'),
  path('sintaks/deletesintaks/<int:id>' , views.deleteSintaks , name='deletesintaks'),

  # Path Variabel 
   path('variabel/' , views.getVariabel , name='getvariabel'),
  path('variabel/addvariabel' , views.addVariabel , name='addvariabel'),
  path('variabel/storevariabel' , views.storeVariabel , name='storevariabel'),
  path('variabel/editvariabel/<int:id>' , views.editVariabel , name='editvariabel'),
  path('variabel/updatevariabel/<int:id>' , views.updateVariabel , name='updatevariabel'),
  path('variabel/deletevariabel/<int:id>' , views.deleteVariabel , name='deletevariabel'),

  # Path Program
  path('' , views.getProgram , name='getprogram'),
  path('createprogram' , views.createProgram , name='createprogram'),
  path('storeprogram' , views.storeProgram , name='storeprogram'),
  path('editprogram/<int:id>' , views.editProgram , name='editprogram'),
  path('updateprogram/<int:id>' , views.updateProgram , name='updateprogram'),
  path('deleteprogram/<int:id>' , views.deleteProgram , name='deleteprogram'),
]
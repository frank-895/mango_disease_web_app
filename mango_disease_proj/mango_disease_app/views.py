from django.shortcuts import render
from .author_card import AuthorCard
from .data_model import data_model
import os
    
######### Define Authors #########
frank = AuthorCard("Frank Snelling",
                   "S367853",
                   "Computer Science",
                   "Travel, Food & Wine",
                   50,
                   30,
                   10,
                   90,
                   "Frank.png")

michael = AuthorCard("Michael Lewis",
                   "S342724",
                   "Secondary Education",
                   "Ludology, Squash, Hiking",
                   50,
                   80,
                   60,
                   70)


authors = [frank, michael]



######### Define Diseases / Pests #########
fakepest = data_model("Name (PEST)",True,4,8,"SDESC-P","LDESC-P","CONTROL-P")
fakepest2 = data_model("NAME 2 (PEST)",True,4,8,"SDESC-P 2","LDESC-P 2","CONTROL-P 2")
fakedisease = data_model("NAME (DISEASE)",False,2,7,"SDESC-D","LDESC-D","CONTROL-D")
fakedisease2 = data_model("NAME 2 (DISEASE)",False,2,7,"SDESC-D 2","LDESC-D 2","CONTROL-D 2")
disease1 = data_model("Mango Pink Scale",False,4,6,
                      "Small pink insects which are common all year round throughout the growth cycle. ",
                      "Mango scale is caused by mango scale insects; the female mango scale insects can lay up to 200 eggs in a spot which look like a tiny pink mound. After hatching the insects will suck the sap from the plant. Heavy infestation can cause drying of leaves and twigs, poor flowers and reduce quality of fruit due to pink blemishes forming on the fruit. ",
                      "Due to Mango scale being a threat throughout the growth cycle, frequent monitoring is recommended every fortnight, inspecting leaves and twigs less than 1 year old,  5 Branches on 10 tress per hectare. Pyriproxyfen is the recommended sprayed, targeted on the insects locations and additionally throughout the branches, fruit and foliage. No more than 2 applications per season with 4 weeks between.",
                      'Mangoscale.png')
disease2 = data_model("Bacterial Black Spot",False,4,4,
                      "A fungal infection that is common in southern areas of Australia or where there has been unseasonal wet conditions. ",
                      "Bacterial Black Spot is caused by the fungus Xanthomonas campestris pv. mangiferae-indicae and causes black scabby spots to form on leaves. These spots commonly develop into secondary rots and futher form into deep fruit decay. In extreme cases fruit with Bacterial Black Spot can become unmarketable. ",
                      "The bacteria can lie dormant on stem lesions and as the mango trees develop it then spreads to the leaves and fruit; it can then further spread from tree to tree in a field by strong winds in rain or tools used for management. Copper Oxychloride spray recommends for treatment every 4 weeks during the flowering to fruit stages. To reduce the risk of initial infection it is also recommended to frequently clean pruning and harvesting equipment or plant resistant fruit.",
                      'BlackSpot.png')


disease_list = [disease1, disease2, fakepest,fakedisease,fakepest2,fakedisease2]

def home(request):
    return render(request, 'mango_disease_app/index.html')

def diseases(request):
    page_data = {'diseases': disease_list}
    return render(request, 'mango_disease_app/diseases.html', page_data)

def ind_disease(request, name):
    page_data={}
    for i in disease_list:
        if name == i.name:
            page_data['disease'] = i
    return render(request, 'mango_disease_app/ind_disease.html',page_data)

def about(request):       
    page_data = {'cards': authors}
    return render(request, 'mango_disease_app/about.html', page_data)
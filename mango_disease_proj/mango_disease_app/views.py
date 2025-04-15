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
                   70,
                   "Michael.jpg")

opeoluwa = AuthorCard("Opeoluwa Adebiyi",
                      "S373330",
                      "Computer Science",
                      "Puzzles, Event planning, Fishing",
                      50,
                      70,
                      90,
                      70)

patrick = AuthorCard("Patrick Dunn",
                     "S378262",
                     "Computer Science",
                     "Gaming, Animation, Cooking",
                     80,
                     70,
                     80,
                     40,
                     "Patrick.jpg")


authors = [frank, michael, opeoluwa, patrick]

######### Define Diseases / Pests #########
examplepest = data_model("Name (PEST)",True,4,8,"SDESC-P","LDESC-P","CONTROL-P")
exampledisease = data_model("NAME (DISEASE)",False,2,7,"SDESC-D","LDESC-D","CONTROL-D")
disease1 = data_model("Mango Pink Scale",True,4,6,
                      "Small insects that cause pink scale which are common all year round throughout the growth cycle. ",
                      "Mango scale is caused by mango scale insects; the female mango scale insects can lay up to 200 eggs in a spot which look like a tiny pink mound. After hatching the insects will suck the sap from the plant. Heavy infestation can cause drying of leaves and twigs, poor flowers and reduce quality of fruit due to pink blemishes forming on the fruit. ",
                      "Due to Mango scale being a threat throughout the growth cycle, frequent monitoring is recommended every fortnight, inspecting leaves and twigs less than 1 year old,  5 Branches on 10 tress per hectare. Pyriproxyfen is the recommended sprayed, targeted on the insects locations and additionally throughout the branches, fruit and foliage. No more than 2 applications per season with 4 weeks between.",
                      'Mangoscale.png')
disease2 = data_model("Bacterial Black Spot",False,4,4,
                      "A fungal infection that is common in southern areas of Australia or where there has been unseasonal wet conditions.",
                      "Bacterial Black Spot is caused by the fungus Xanthomonas campestris pv. mangiferae-indicae and causes black scabby spots to form on leaves. These spots commonly develop into secondary rots and futher form into deep fruit decay. In extreme cases fruit with Bacterial Black Spot can become unmarketable. ",
                      "The bacteria can lie dormant on stem lesions and as the mango trees develop it then spreads to the leaves and fruit; it can then further spread from tree to tree in a field by strong winds in rain or tools used for management. Copper Oxychloride spray recommends for treatment every 4 weeks during the flowering to fruit stages. To reduce the risk of initial infection it is also recommended to frequently clean pruning and harvesting equipment or plant resistant fruit.",
                      'BlackSpot.png')
disease3 = data_model("Mango Scab",False,4,7,
                      "Mango scab is a fungal infection that appears in damp, low-lying orchards and only young tissue is susceptible to infection.  ",
                      "Mango scab is caused by the fungus of Elsinoe Mangiferae and it causes small black lesions, especially on young fruit. These infected fruits are unmarketable and orchards without chemical control have been known to lose 90% of their crop. ",
                      "To control the spread of mango scab, infected plant parts (i.e., fruit, leaves or stems) must be removed and destroyed. Ideally, resistant varieties should be planted to prevent the formation of this disease in the first place. ",
                      "MangoScab.jpg"
)
disease4 = data_model("Mango Seed Weevil",True,3,4,
                      "Mango seed weevils are 6-9mm long with a lifespan of 2 years, meaning they can survive a crop failure into the following year. ",
                      "The mango seed weevil causes minimal damage to fruit and is therefore classified as a minor pest. However, the mango seed weevil does increase early fruit drop and decrease germination, causing a financial impact to mango growers.",
                      "The mango seed weevil can be controlled with chemical sprays. The weevil has a limited ability to fly, so spread of the pest is only done via the transport of infected fruit, which should be properly contained.",
                      "MangoSeedWeevil.jpg"
)
disease5 = data_model("Mango Shoot Caterpillar",True,4,7,
                      "Brown and white moths signified by affected branches dying or breaking off. Their eggs are a bright yellow and the larvae are light green; both are often seen on leaves or new growths. ",
                      "Mango shoot caterpillars are brown and white moths which damage young fruit and can especially hurt new growths. They are often signified by branches they have affected dying or breaking off. The eggs and larvae are both brightly coloured, bright yellow and light green respectively, and often found on new growths or leaves. ",
                      "Insecticide is the recommended control method for mango shoot caterpillars but is only to be used if eggs or larvae are found. If there is only branch damage or not enough eggs or larvae present, insecticide should still be avoided. ",
                      "MangoShootCaterpillar.png"
)
disease6 = data_model("Mango Anthracnose",False,4,7,
                      "Most widespread and serious postharvest disease of tropical fruits, including mango",
                      "Mango shoot caterpillars are brown and white moths which damage young fruit and can especially hurt new growths. They are often signified by branches they have affected dying or breaking off. The eggs and larvae are both brightly coloured, bright yellow and light green respectively, and often found on new growths or leaves. ",
                      "Insecticide is the recommended control method for mango shoot caterpillars but is only to be used if eggs or larvae are found. If there is only branch damage or not enough eggs or larvae present, insecticide should still be avoided. ",
                      "MangoAnthracnose.jpg"
)
disease7 = data_model("Mango Planthopper",True,4,7,
                      "Small Nymphs roughly 1 to 7mm with pointed triangular heads and a tent-like body",
                      "Both adults and nymphs are plant suckers sometimes transferring plant diseases. They are a pest of a range of plants, attacking maturing fruit and causing spotting on new leaves and flowers. They need to be in great numbers to cause significant damage. They produce honeydew which causes sooty mould on the leaves and stems of the plant.",
                      "- Spray with neem - Spray with pyrethrum - Diatomaceous earth - Keep weeds down to reduce breeding areas - They like warm dry conditions so keep water up to plants.",
                      "MangoPlanthopper.jpg"
)

disease_list = [disease1, disease2, disease3, disease4, disease5, disease6, disease7]

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
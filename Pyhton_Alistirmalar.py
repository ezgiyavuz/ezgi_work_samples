#1_Verilen değerlerin veri yapılarını inceleyiniz.
from typing import List, Any

x=8
type(x)
y=3.2
type(y)
z=8j+18
type(z)
b=True
type(b)
c=23<22
type(c)
l=[1,2,3,4]
type(l)
d={"name":"Jake",
   "Age":27,
   "Adress":"Downtown"}
type(d)
t=("Machine Learning","Data Science")
type(t)
s={"Pyhton","Machine Learning","Data Sicence"}
type(s)
#################################################
#2_Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz,kelime kelime ayırınız.

text="The goal is to turn data into information , and information into insight"
text.replace(","," ")
text.replace("."," ")
text2=text.upper()
text2
A=list(text2.split())
A
#############################################################
#3_Verilen listeye aşağıdaki adımları uygulayınız.

lst=["D","A","T","A","S","C","I","E","N","C","E"]

#Adım1
len(lst)
#Adım2
lst[0]
lst[10]
#Adım3
lst[0:4]
#Adım4
lst.pop(8)
lst.append("A")
lst
lst.insert(8,"N")
################################################################
#4_Verilen sözlük yapısına aşağıdaki adımları uygulayınız.

dict = {"Christian": ["America",18],
        "Daisy": ["England",12],
        "Antonio": ["Spain",22],
        "Dante": ["Italy", 23]}
#Adım1
dict.keys()
#Adım2
dict.values()
#Adım3
dict["Daisy"][1]=13
dict
#Adım4
dict["Ahmet"]=["Turkey",24]
dict
#Adım5
dict.pop("Antonio")
dict

#5_Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri return eden fonksiyon yazınız.

l=[2,13,18,93,22]

def func(l):
    clist = []
    tlist = []
    for i in l:
        if i % 2 == 0:
            clist.append(i)
        else:
            tlist.append(i)
    print(tlist,clist)
    func(l)
l=[2,13,18,93,22]
func(l)
#6_List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz.

import seaborn as sns
df=sns.load_dataset("car_crashes")
df.columns

s_col = [col for col in df.columns if df[col].dtypes != "O"]
s_col

df_columns = ["NUM_" + col.upper() if col in s_col else col.upper() for col in df.columns ]
df_columns

#7_List Comprehension yapısı kullanarak car_crashes verisinde isminde
# "no" barındırmayan değişkenlerin isimlerinin sonuna "FLAG" yazınız.

import seaborn as sns
df=sns.load_dataset("car_crashes")
df.columns


[col.upper() + "_FLAG"  for col in df.columns if "no" not in col]

#8List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan
#değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns


og_list = ["no_previous", "no_previous"]
new_cols = []
new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]
new_df





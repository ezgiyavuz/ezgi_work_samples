################################################################
#######################################################################################
#Görev 1: Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.
#########################################################################################
import pandas as pd
import seaborn as sns
df = sns.load_dataset("titanic")
df.head()
#######################################################################################
#Görev 2: Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.
#########################################################################################
df["sex"].value_counts()
#######################################################################################
#Görev 3: Her bir sutuna ait unique değerlerin sayısını bulunuz.
#########################################################################################
df.nunique()
#######################################################################################
#Görev 4: pclass değişkeninin unique değerlerinin sayısını bulunuz.
#########################################################################################
df["pclass"].nunique()
#######################################################################################
#Görev 5: pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.
#########################################################################################
df[["pclass","parch"]].nunique()
#######################################################################################
#Görev 6: embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz ve tekrar kontrol ediniz.
#########################################################################################
df["embarked"]=df["embarked"].astype("category")
df["embarked"].dtype
#######################################################################################
#Görev 7: embarked değeri C olanların tüm bilgelerini gösteriniz.
#########################################################################################
df
pd.set_option('display.max_columns', None)
"C" in df["embarked"]
df[df["embarked"]=="C"]
#######################################################################################
#Görev 8: embarked değeri S olmayanların tüm bilgelerini gösteriniz.
#########################################################################################
df[df["embarked"]!="C"]
#######################################################################################
#Görev 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.
#########################################################################################
df[ (df["age"]< 30) & (df["sex"]=="female")]
df["age"].dtype
#######################################################################################
#Görev 10: Fare'i 500'den büyük veya yaşı 70’den büyük yolcuların bilgilerini gösteriniz.
#########################################################################################
df.columns
df[ (df["fare"] > 30) | (df["age"]>70)]
#######################################################################################
#Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz.
#########################################################################################
df.isnull().sum()
#######################################################################################
#Görev 12: who değişkenini dataframe’den çıkarınız.
#########################################################################################
df.drop("who",axis=1, inplace=True)
df.columns
#######################################################################################
#Görev 13: deck değikenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz.
#########################################################################################
df["deck"] = df["deck"].fillna(df["deck"].mode())
df["deck"]
#######################################################################################
#Görev 14: age değikenindeki boş değerleri age değişkenin medyanı ile doldurunuz.
#########################################################################################
df["age"] = df["age"].fillna(df["age"].median())
df["age"]
#######################################################################################
#Görev 15: survived değişkeninin pclass ve cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.
#########################################################################################
df.groupby(["pclass","sex"]).agg({"survived": ["sum" , "count" , "mean"]})
#######################################################################################
#Görev 16: 30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 verecek bir fonksiyon yazın. Yazdığınız fonksiyonu kullanarak titanik veri
#setinde age_flag adında bir değişken oluşturunuz oluşturunuz. (apply ve lambda yapılarını kullanınız)
#########################################################################################
df["age_flag"] = df.apply(lambda x: (1 if x['age'] < 30 else 0), axis=1)
#######################################################################################
#Görev 17:Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.
#########################################################################################
import seaborn as sns
df = sns.load_dataset("tips")
df.head()
#######################################################################################
#Görev 18:Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill değerinin sum, min, max ve mean değerlerini bulunuz.
#########################################################################################
df.groupby("time").agg({"total_bill":["sum","min","max","mean"]})
#######################################################################################
#Görev 19:Day ve time’a göre total_bill değerlerinin sum, min, max ve mean değerlerini bulunuz.
#########################################################################################
df.groupby(["day","time"]).agg({"total_bill":["sum","min","max","mean"]})
#######################################################################################
#Görev 20:Lunch zamanına ve kadın müşterilere ait total_bill ve tip değerlerinin day'e göre sum, min, max ve mean değerlerini bulunuz.
#########################################################################################
df[(df["sex"] == "Female") & (df["time"] == "Lunch")].groupby("day").agg({"tip": ["sum", "min", "max", "mean"]})
#######################################################################################
#Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir? (loc kullanınız)
#########################################################################################
df.loc[(df["size"] < 3) & (df["total_bill"] > 10), ["total_bill"]].mean()
#######################################################################################
#Görev22:total_bill_tip_sum adında yeni bir değişken oluşturunuz. Her bir müşterinin ödediği totalbill ve tip in toplamını versin.
#########################################################################################
df["total_bill_tip_sum"]=df["total_bill"]+df["tip"]
#######################################################################################
#Görev23:Total_bill değişkeninin kadın ve erkek için ayrı ayrı ortalamasını bulunuz. Bulduğunuz ortalamaların altında olanlara 0, üstünde ve eşit
#olanlara 1 verildiği yeni bir total_bill_flag değişkeni oluşturunuz.
#Kadınlar için Female olanlarının ortalamaları, erkekler için ise Male olanların ortalamaları dikkate alınacktır. Parametre olarak cinsiyet ve total_bill
#alan bir fonksiyon yazarak başlayınız. (If-else koşulları içerecek)
#########################################################################################
df.groupby("sex")["total_bill"].mean()
male_bill = df[df["sex"] == "Male"]["total_bill"].mean()
female_bill = df[df["sex"] == "Female"]["total_bill"].mean()
df["total_bill_flag"]=df.apply(lambda x: (1 if x['total_bill'] > (female_bill if x['sex'] == "Female" else male_bill) else 0), axis=1)
#######################################################################################
#Görev 24: total_bill_flag değişkenini kullanarak cinsiyetlere göre ortalamanın altında ve üstünde olanların sayısını gözlemleyiniz.
#########################################################################################
df.groupby("sex").agg({"total_bill_flag":"value_counts"})
#######################################################################################
#Görev Görev 25: Veriyi total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız
# ve ilk 30 kişiyi yeni bir dataframe'e atayınız.
#########################################################################################
new_df=df.sort_values(by="total_bill_tip_sum",ascending=False).head(30)

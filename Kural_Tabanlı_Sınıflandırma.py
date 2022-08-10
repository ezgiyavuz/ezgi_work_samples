#Persona.csv veri seti uluslararası bir oyun şirketinin sattığı ürünlerin fiyatlarını ve bu
#ürünleri satın alan kullanıcıların bazı demografik bilgilerini barındırmaktadır. Veri
#seti her satış işleminde oluşan kayıtlardan meydana gelmektedir. Bunun anlamı
#tablo tekilleştirilmemiştir. Diğer bir ifade ile belirli demografik özelliklere sahip bir
#kullanıcı birden fazla alışveriş yapmış olabilir.#
##GOREV_1##
#######################################################################################
#Soru 1:persona.csv dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz.
#########################################################################################

import pandas as pd
df=pd.read_csv("/Users/EAY/PycharmProjects/pythonProject/dsmlbc_9_abdulkadir/Homeworks/ezgi_yavuzay/Odev_2/persona.csv")
df
df.ndim
df.size
df.shape
df.dtypes
df.info
#######################################################################################
#Soru 2:Kaç unique SOURCE vardır? Frekansları nedir?
#######################################################################################
df["SOURCE"].nunique()
df["SOURCE"].value_counts()
#######################################################################################
#Soru 3:Kaç unique PRICE vardır?
#######################################################################################
df["PRICE"].nunique()
#######################################################################################
#Soru 4:Hangi PRICE'dan kaçar tane satış gerçekleşmiş?
#######################################################################################
df.groupby("PRICE").agg({"PRICE":["count"]})
#######################################################################################
#Soru 5:Hangi ülkeden kaçar tane satış olmuş?
#######################################################################################
df.groupby("COUNTRY").agg({"PRICE":["count"]})
#######################################################################################
#Soru 6:Ülkelere göre satışlardan toplam ne kadar kazanılmış?
#######################################################################################
df.groupby("COUNTRY").agg({"PRICE":["sum"]})
#######################################################################################
#Soru 7:SOURCE türlerine göre satış sayıları nedir?
#######################################################################################
df.groupby("SOURCE").agg({"SOURCE":["count"]})
df["SOURCE"].value_counts()
#######################################################################################
#Soru 8:Ülkelere göre PRICE ortalamaları nedir?
#######################################################################################
df.groupby("COUNTRY").agg({"PRICE":["mean"]})
#######################################################################################
#Soru 9:SOURCE'lara göre PRICE ortalamaları nedir?
#######################################################################################
df.groupby("SOURCE").agg({"PRICE":["mean"]})
#######################################################################################
#Soru 10:COUNTRY-SOURCE kırılımında PRICE ortalamaları nedir?
#######################################################################################
df.pivot_table("PRICE","COUNTRY","SOURCE")
########################################################################################
##GOREV_2## COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?
#######################################################################################
df.groupby(["COUNTRY","SOURCE","SEX","AGE"]).agg({"PRICE":["mean"]})
########################################################################################
##GOREV_3## Önceki sorudaki çıktıyı daha iyi görebilmek için sort_values metodunu azalan olacak şekilde PRICE’a göre uygulayınız.Çıktıyı agg_df olarak kaydediniz.
#######################################################################################
agg_df=df.groupby(["COUNTRY","SOURCE","SEX","AGE"]).agg({"PRICE":["mean"]}).sort_values(by=("PRICE","mean"), ascending=False)
agg_df
########################################################################################
##GOREV_4## Üçüncü sorunun çıktısında yer alan PRICE dışındaki tüm değişkenler index isimleridir.
# Bu isimleri değişken isimlerine çeviriniz.
# #################################################################################
agg_df.reset_index()
########################################################################################
##GOREV_5## Age değişkenini kategorik değişkene çeviriniz ve agg_df’e ekleyiniz.??
#Age sayısal değişkenini kategorik değişkene çeviriniz.
#• Aralıkları ikna edici şekilde oluşturunuz.
#• Örneğin: ‘0_18', ‘19_23', '24_30', '31_40', '41_70'
# #################################################################################
List=[0,18,19,23,24,30,31,40,41,70]
df["AGE"].astype("category")
import pandas as pd
agg_df["AGE_CAT"] = pd.cut(agg_df["AGE"], List)

agg_df["AGE_CAT"].isnull().sum()
agg_df.shape
########################################################################################
##GOREV_6## Yeni seviye tabanlı müşterileri (persona) tanımlayınız.
#Age sayısal değişkenini kategorik değişkene çeviriniz.
#• Yeni eklenecek değişkenin adı: customers_level_based
#• Önceki soruda elde edeceğiniz çıktıdaki gözlemleri bir araya getirerek customers_level_based değişkenini oluşturmanız gerekmektedir.
# #################################################################################
import pandas as pd
pd.read_csv("/Users/EAY/PycharmProjects/pythonProject/dsmlbc_9_abdulkadir/Homeworks/ezgi_yavuzay/Odev_2/persona.csv")
df.values[0]
df.reset_index()
df["customer_level_based"]=[str(x[3]).upper() + "_" + str(x[1]).upper() +"_" + str(x[2]).upper() + "_" + str(x[5]).upper() for x in df.values]
df.values[0]
########################################################################################
##GOREV_7## Yeni müşterileri (personaları) segmentlere ayırınız.
#• Yeni müşterileri (Örnek: USA_ANDROID_MALE_0_18) PRICE’a göre 4 segmente ayırınız.
#• Segmentleri SEGMENT isimlendirmesi ile değişken olarak agg_df’e ekleyiniz.
#• Segmentleri betimleyiniz (Segmentlere göre group by yapıp price mean, max, sum’larını alınız).
# #################################################################################
df
df["SEGMENT"] = pd.qcut(df["PRICE"], 4, labels=["D", "C", "B", "A"])
df.groupby(["SEGMENT"]).agg({"PRICE": ["mean", "max", "sum"]})

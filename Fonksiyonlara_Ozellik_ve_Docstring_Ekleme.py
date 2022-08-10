#Görev: cat_summary() fonksiyonuna 1 özellik ekleyiniz. Bu özellik argümanla biçimlendirilebilir olsun. Var olan
#özelliği de argümanla kontrol edilebilir hale getirebilirsiniz.
#Fonksiyona arguman ile biçimlendirilebilen bir özellik eklemek ne demek?
#Örnek olarak aşağıdaki check_df fonksiyonuna argümanla biçimlendirilebilen 2 özellik eklenmiştir.
#Bu özellikler ile tail fonksiyonunun kaç gözlemi göstereceği ve quantile değerlerinin gösterilip gösterilmeyeceği fonksiyona özellik olarak
#girilmiştir. Bu özellikleri kullanıcı argümanlarla biçimlendirebilmektedir.
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]

num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int", "float"]]

cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]

cat_cols = cat_cols + num_but_cat

cat_cols = [col for col in cat_cols if col not in cat_but_car]
for col in df.columns:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)

def cat_summary(dataframe, col_name,quan=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    if quan:
    print(dataframe.quantile([0,0.30,0.60,0.90,1]).T)
    print("##########################################")

cat_summary(df, "sex")

for col in cat_cols:
    cat_summary(df, col,quan=True)
###################################################################
#####Görev: check_df(), cat_summary() fonksiyonlarına 4 bilgi (uygunsa) barındıran numpy tarzı docstring
######yazınız. (task, params, return, example)#############################
 def cat_summary(dataframe,col_name,quan):
 """

 Parameters
 ----------
 dataframe:üzerinde işlem yapılacak dataframe'dir.

 col_name:seçilen kolon bilgisidir
 quan: yuzdelik dilimleri ifade eder. int,float

 Returns kategorik değişkenlerde oranı ve adeti getirir.
 -------

 """



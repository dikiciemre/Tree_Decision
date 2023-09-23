import pandas as pd
from math import sqrt
oyuncular = {

    "boy": [175,177,178,181,182,183,184,188,190],
    "deneyim": [4,6,3,2,6,3,7,2,6],
    "maas": [12,18,15,16,24,20,28,24,32]
}
df = pd.DataFrame(oyuncular)
print("DATA FRAME :")
print(df)


print("DATA FRAME ORTALAMA MAAŞ: " + str(df['maas'].mean())) # 21.0


print(df.maas - df.maas.mean())


error = (df.maas-df.maas.mean()).pow(2).sum()
print("İLK ERROR PUANI : " + str(error)) #340.0




# ilk filtre yani bölme işlemi burada oluyor
filt = (df.boy <= 180)
df1 = df[filt]
df2 = df[~filt]

print("\nboyu 180 den az olanlar")
print(df1)
print("\nboyu 180 den fazla olanlar")
print(df2)


df1.maas.mean() # 15.0
df2.maas.mean() # 24.0


print("****** BİRİNCİ BÖLME ******")
error1 = (df1.maas-df1.maas.mean()).pow(2).sum()+(df2.maas-df2.maas.mean()).pow(2).sum()
print(error1) # 178.0

print("\n\n\n--------------------------------\n\n\n")






# ikinci filtre yani bölme işlemi burada oluyor
filt2 = (df2.boy <= 185)
df3 = df2[filt2]
df4 = df2[~filt2]

print("\nboyu 185 den az olanlar")
print(df3)
print("\nboyu 185 den fazla olanlar")
print(df4)


df3.maas.mean() # 22.0
df4.maas.mean() # 28.0


print("****** İKİNCİ BÖLME ******")
error2 = (df1.maas-df1.maas.mean()).pow(2).sum()+(df3.maas-df3.maas.mean()).pow(2).sum()+(df4.maas-df4.maas.mean()).pow(2).sum()
print(error2) # 130.0


print("\n\n\n--------------------------------\n\n\n")






# üçüncü filtre yani bölme işlemi burada oluyor
filt3 = (df3.deneyim <= 5)
df5 = df3[filt3]
df6 = df3[~filt3]

print("\ndeneyimi 5 den az olanlar")
print(df5)
print("\ndeneyimi 5 den fazla olanlar")
print(df6)


df5.maas.mean() # 18.0
df6.maas.mean() # 26.0



print("****** ÜÇÜNCÜ BÖLME ******")
error3 = (df1.maas-df1.maas.mean()).pow(2).sum()+(df5.maas-df5.maas.mean()).pow(2).sum()+(df6.maas-df6.maas.mean()).pow(2).sum()+(df4.maas-df4.maas.mean()).pow(2).sum()
print(error3) # 66.0





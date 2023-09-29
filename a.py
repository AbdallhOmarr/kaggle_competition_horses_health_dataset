
plt.figure(figsize=(12, 6)) 

sns.catplot(
    data=df, x="outcome", y="pulse", hue="surgery",
            kind="violin", split=True, col="cp_data", aspect=.7, )



sns.catplot(
    data=df, x="outcome", y="rectal_temp", hue="surgery",
            kind="violin", split=True, col="cp_data", aspect=.7, )

sns.catplot(
    data=df, x="outcome", y="respiratory_rate", hue="surgery",
            kind="violin", split=True, col="cp_data", aspect=.7, )

sns.catplot(
    data=df, x="outcome", y="hospital_number", hue="surgery",
            kind="violin", split=True, col="cp_data", aspect=.7, )



sns.catplot(
    data=df, x="outcome", y="nasogastric_reflux_ph", hue="surgery",
            kind="violin", split=True, col="cp_data", aspect=.7, )


sns.catplot(
    data=df, x="outcome", y="packed_cell_volume", hue="surgery",
            kind="violin", split=True, col="cp_data", aspect=.7, )




sns.catplot(
    data=df, x="outcome", y="total_protein", hue="surgery",
            kind="violin", split=True, col="cp_data", aspect=.7, )




sns.catplot(
    data=df, x="outcome", y="abdomo_protein", hue="surgery",
            kind="violin", split=True, col="cp_data", aspect=.7, )


plt.show()

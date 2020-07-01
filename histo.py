import matplotlib.pyplot as plt

y_views=[100,482,145,736,483,635,264,108,296,193,875,275,846,752,330,800]
days=[100,200,300,400,500,600,700,800,900,1000]

plt.hist(y_views,days,label="YouTube Views")

plt.xlabel('Days')
plt.ylabel('Views')
plt.title("Daily Views On YouTube")
plt.legend(loc='upper left')
plt.xticks(days)

plt.savefig('histo_img.png', dpi=200)
plt.show()

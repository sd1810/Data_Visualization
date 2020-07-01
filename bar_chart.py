import matplotlib.pyplot as plt

y_views=[100,482,145,736,483,635,264,108,296,193,875,275,846,598]
f_views=[100,482,145,736,483,635,264,108,296,193,875,275,846,598]
days=range(1,15)

plt.bar(days,y_views,label="YouTube Views",width=0.25,align='edge')
plt.bar(days,f_views,label="Facebook Views",width=-0.25,align='edge')

plt.xlabel('Days')
plt.ylabel('Views')
plt.title("Daily Views On YouTube")
plt.legend(loc='upper left')
plt.xticks(days)

plt.savefig('bar_img.png', dpi=200)
plt.show()

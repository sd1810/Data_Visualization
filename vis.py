import matplotlib.pyplot as plt

y_views=[200,600,450,367,129,243,654]
f_views=[100,140,690,470,365,743,392]
t_views=[645,274,862,164,365,107,396]
days= range(1,8)

plt.plot(days, y_views,label='YouTube Views',marker='o')
plt.plot(days, f_views,label='Facebook Views',marker='o')
plt.plot(days, t_views,label='Twitter Views',marker='o')
	
plt.xlabel('Days')
plt.ylabel('Views')
plt.legend(loc ='upper left')
plt.title('YouTube Views on daily basis')
plt.grid(True)
plt.savefig('vis_img.png',dpi=500)

plt.show()


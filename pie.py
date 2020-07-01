import matplotlib.pyplot as plt
import numpy as np

labels=['Facebook','Youtube','Linkedin','Instagram']
views=[398,237,690,400]
explode=[0,0,0,0.2]

plt.pie(views , labels=labels , explode=explode , autopct='%1.1f%%',shadow=True)
plt.savefig('pie_img.png',dpi=200)
plt.show()

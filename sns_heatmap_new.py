import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# генерация двумерной матрицы случайных чисел размером 10x10
# от 1 до 100
data = np.random.randint(low=1,
                         high=100,
                         size=(10, 10))

# установка значений параметров
vmin = 30
vmax = 70

# построение тепловой карты
hm = sns.heatmap(data=data,
                vmin=vmin,
                vmax=vmax)

# отображение построенной тепловой карты
plt.show()

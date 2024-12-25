import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# генерация двумерной матрицы случайных чисел размером 10x10
# от 1 до 100
data = np.random.randint(low=1,
                         high=100,
                         size=(10, 10))
print("Данные, которые будут нанесены на график:\n")
print(data)

# построение тепловой карты
hm = sns.heatmap(data=data)

# отображение построенной тепловой карты
plt.show()

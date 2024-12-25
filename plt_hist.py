import matplotlib.pyplot as plt
import pandas as pd

# Добавляем датасет
data = pd.read_csv('tips.csv')

# Построение графика
x = data['total_bill']


plt.hist(x)

# Добавляем заголовок графика
plt.title("Чаевые в ресторане")

# Описание y-оси
plt.ylabel('Частота')

# Описание x-оси
plt.xlabel('Сумма')

plt.show()
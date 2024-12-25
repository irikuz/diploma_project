import matplotlib.pyplot as plt
import pandas as pd

# Добавляем датасет
data = pd.read_csv('tips.csv')

# Построение графика
x = data['day']
y = data['total_bill']

plt.scatter(x, y)

# Добавляем заголовок графика
plt.title("Чаевые в ресторане")

# Описание y-оси
plt.ylabel('Сумма')

# Описание x-оси
plt.xlabel('День')

# Отображение графика
plt.show()
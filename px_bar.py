import plotly.express as px

# Загрузка данных
df = px.data.tips()

# Создаем таблицу
fig = px.bar(df, x='day', y="total_bill")

# Отображение графика
fig.show()

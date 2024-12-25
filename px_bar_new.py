import plotly.express as px

# Загружаем данные
df = px.data.tips()

# Создаем диаграмму
fig = px.bar(df, x='day', y="total_bill", color='sex',
             facet_row='time', facet_col='sex')

# Отображение графика
fig.show()

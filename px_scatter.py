import plotly.express as px

# Загружаем данные
df = px.data.tips()

# Создаем график
fig = px.scatter(df, x='total_bill', y="tip")

# Отображаем график
fig.show()
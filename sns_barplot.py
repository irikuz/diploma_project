import seaborn as sns

# Импорт данных
diamonds = sns.load_dataset("diamonds")

# Строим график
sns.barplot(data=diamonds, x="carat", y="price")
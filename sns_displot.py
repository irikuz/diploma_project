import seaborn as sns

# Импорт данных
diamonds = sns.load_dataset("diamonds")

# Строим график распределения значений массы в каратах
sns.displot(diamonds, x="carat")
import scipy.stats as stats
import numpy as np
# Данные задачи
sigma = 16 # Стандартное отклонение генеральной совокупности
M = 80 # Выборочная средняя
n = 256 # Объем выборки
alpha = 0.05 # Уровень значимости для 95% доверительного интервала
# Критическое значение для Z-распределения
z_crit = stats.norm.ppf(1 - alpha / 2)
# Рассчет стандартной ошибки
standard_error = sigma / np.sqrt(n)
# Доверительный интервал
margin_of_error = z_crit * standard_error
confidence_interval = (M - margin_of_error, M + margin_of_error)
print(f"Доверительный интервал: {confidence_interval}")

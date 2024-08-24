import pandas as pd
import quantstats as qs
qs.extend_pandas()

# Вместо Your_file.csv вставьте Ваш файл
price = pd.read_csv("example.csv")
price["pct"] = (100000.0 + price["cumm_pnl"]).pct_change()
price["date"] = pd.to_datetime(price["date"], format="%Y-%m-%d")
price = price.set_index("date")


# Генерация полного отчета со всеми графиками и метриками с базовыми настройками в формате html
# Вместо Your_title укажите название отчета
# Вместо Your_directory/Your_file_name.html укажите Вашу директорию и название файла, которое хотите
qs.reports.html(price["pct"], title="Your_title", output="Your_directory/Your_file_name.html")


# Генерация полного отчета со всеми графиками и метриками с базовыми настройками прямо в IDE
qs.reports.full(price["pct"])


# Расчет CAGR для каждого года
yearly_returns = price["pct"].groupby(pd.Grouper(freq='Y'))
cagr_yearly = yearly_returns.apply(lambda x: qs.stats.cagr(x)) * 100
cagr_yearly.to_csv("Your_directory/Your_file_name.csv")


# Вывод avg_return
# print(qs.stats.avg_return(price["pct"]))


# Вывод графика monthly_heatmap
qs.plots.monthly_heatmap(price["pct"], show=True)

# Вывод общего CAGR
print(qs.stats.cagr(price["pct"]))


# Вывод коэффициента Кальмара
print(qs.stats.calmar(price["pct"]))


# Сохранение drawdown_details в формат .csv для удобства чтения
drawdown_details = qs.stats.drawdown_details(price["pct"])
drawdown_details.to_csv('Your_directory/drawdown_details.csv', index=False)


# Вывод exposure
print(qs.stats.exposure(price["pct"]))


# Вывод максимальной просадки
print(qs.stats.max_drawdown(price["pct"]))


# Сохранение monthly_returns в формат .csv для удобства чтения
monthly_returns = qs.stats.monthly_returns(price["pct"])
monthly_returns.to_csv('Your_directory/monthly_returns.csv', index=False)


# Коэффициент Шарпа
print(qs.stats.sharpe(price["pct"], periods=365))


# Sortino
print(qs.stats.sortino(price["pct"]))


# График drawdown
qs.plots.drawdown(price["pct"], show=True)


# График drawdown_periods
qs.plots.drawdowns_periods(price["pct"], show=True)


# Пример отчета о компании Apple
returns = qs.utils.download_returns('AAPL')
qs.reports.html(returns, title="Apple report", output='Output/Apple_report.html')



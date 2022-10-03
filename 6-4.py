# Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы остались только строки, использование дополнительного списка незаконно
some_list = [2, 3, 4, 'dfs', "adsasaw", 4, True, False, 'weit']
some_list = list(filter(lambda x:isinstance(x, str), some_list))
print(some_list)
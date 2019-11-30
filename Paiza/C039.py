E = input().split('+')
print(sum([s.count('<')*10 + s.count('/') for s in E]))

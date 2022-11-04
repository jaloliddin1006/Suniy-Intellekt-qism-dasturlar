from sklearn import tree

clf = tree.DecisionTreeClassifier()


x = [
    [220,110,35],
    [226,75,30],
    [290,60,15],
    [210,140,15],
    [200,140,25],
    [180,180,5],
    [180,135,50],
    [205,120,35],
    [110,180,75],
    [95,197,73]
]

y=[
    'yaxshi',
    'yomon',
    'o`rtacha',
    'yaxshi',
    'o`rtacha',
    'yomon',
    'yaxshi',
    'o`rtacha',
    'yomon',
    'yomon'
]
clf = clf.fit(x,y)
taxmin = clf.predict([[231, 105, 29]])

print(taxmin)
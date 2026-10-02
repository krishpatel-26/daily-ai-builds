from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

X = [
    [20, 0, 0], [40, 0, 1], [80, 1, 1], [120, 1, 1],
    [250, 1, 1], [15, 0, 0], [60, 1, 0], [300, 1, 1],
    [35, 0, 0], [180, 1, 1], [90, 1, 0], [12, 0, 1],
]
y = [0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0]

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

predictions = model.predict(X)
print(classification_report(y, predictions, zero_division=0))

new_lead = [[150, 1, 1]]
print("Predicted sales-priority class:", int(model.predict(new_lead)[0]))

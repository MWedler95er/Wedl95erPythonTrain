import numpy as np
from sklearn.linear_model import LinearRegression

# Beispiel-Daten:
# x = Stunden gelernt
# y = Punkte im Test

x = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)  # Feature(s) -> 2D-Array
y = np.array([50, 55, 65, 70, 75, 85])  # Zielvariable -> 1D-Array

# Modell erstellen
model = LinearRegression()

# Modell trainieren (Fit)
model.fit(x, y)

# Modellparameter
slope = model.coef_[0]  # Steigung
intercept = model.intercept_  # Achsenabschnitt

print(f"Gelerntes Modell: y = {slope:.2f} * x + {intercept:.2f}")

# Vorhersage: Wie viele Punkte bei 7 Lernstunden?
x_new = np.array([[]])
y_pred = model.predict(x_new)

print(f"Vorhersage für 7 Stunden Lernen: {y_pred[0]:.2f} Punkte")

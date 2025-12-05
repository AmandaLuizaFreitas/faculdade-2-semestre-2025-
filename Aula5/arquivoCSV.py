import csv
cars = [
     {'marca': 'Ford', 'modelo': 'Fusion', 'ano': 2020},
     {'marca': 'Chevrolet', 'modelo': 'Malibu', 'ano': 2019},
     {'marca': 'Toyota', 'modelo': 'Camry', 'ano': 2021}
 ]  
with open('cars.csv', mode='w', newline='') as file:
    fieldnames = ['marca', 'modelo', 'ano']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    for car in cars:
        writer.writerow(car)
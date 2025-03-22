from smartphone import Smartphone

catalog = [
    Smartphone("Honor", "GT", "+79128553452"),
    Smartphone("Motorola", "Moto E15", "+735135478961"),
    Smartphone("Nokia", "C210", "+79884438558"),
    Smartphone("Oppo", "Reno 13", "+79000653442"),
    Smartphone("Samsung", "Galaxy S25", "+79816628714")
]

for smartphone in catalog:
    print(f"{smartphone.brend} - {smartphone.model}. {smartphone.number}")

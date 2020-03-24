import json
with open("Car_Model_List.json") as json_file:
    dict1 = json.load(json_file) 

def listCarByBrends():
    newListBrends = []
    for i in dict1:
        if i["Make"] not in newListBrends:	
            newListBrends.append(i["Make"])	
            print(i["Make"])
    command = int(input("для продовження, натисніть - 1\nдля виходу з програми натисність - 0"))
    if command == 1:
        index()
    elif command == 0:
        quit()

def listCarByModels(Make):
    newListModels = []
    for i in dict1:
        if Make == i["Make"]:
            if i["Model"] not in newListModels:
                newListModels.append(i["Model"])
    print(newListModels)
    command = int(input("для продовження, натисніть - 1\nдля виходу з програми натисність - 0"))
    if command == 1:
        index()
    elif command == 0:
        quit()

def listCarByMakeModelYear(Model):
    newListMakeModelYear = []
    for i in dict1:
        if Model == i["Model"]:
            print(i["Make"], i["Year"], i["Model"], sep=", ")
    command = int(input("для продовження, натисніть - 1\nдля виходу з програми натисність - 0"))
    if command == 1:
        index()
    elif command == 0:
        quit()

def listCarByYear(Make, YearFrom, YearTo):
    newListModelYear = []
    for i in dict1:
        if Make == i["Make"] and i["Year"] in (YearFrom, YearTo):
            print(i["Model"])
    command = int(input("для продовження, натисніть - 1\nдля виходу з програми натисність - 0"))
    if command == 1:
        index()
    elif command == 0:
        quit()


def index():
    print("Список брендів - 1")
    print("Список моделей певного бренду - 2")
    print("Знайти модель - 3")
    print("Список моделей певного бренду, за визначений проміжок часу - 4")
    command = int(input("Виберіть потрібну команду зі списка: "))
    if command == 1:
        listCarByBrends()
    if command == 2:
        Make = input("Введіть брен: ")
        listCarByModels(Make)
    if command == 3:
        Model = input("Введіть модель: ")
        listCarByMakeModelYear(Model)
    if command == 4:
        Make = input("Введіть бренд: ")
        YearFrom = int(input ("Введіть початковий рік для діапазона: "))
        YearTo = int(input ("Введіть кінець діапазона: "))
        listCarByYear(Make, YearFrom, YearTo)

index()

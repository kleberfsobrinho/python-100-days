import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

data_fur_color = data["Primary Fur Color"]

data_fur_color_gray = len(data[data_fur_color == "Gray"])
data_fur_color_black = len(data[data_fur_color == "Black"])
data_fur_color_cinnamon = len(data[data_fur_color == "Cinnamon"])

print(data_fur_color_gray)
print(data_fur_color_black)
print(data_fur_color_cinnamon)

data_dict = {
    "Fur Color": ["gray", "black", "cinnamon"],
    "Count": [data_fur_color_gray, data_fur_color_black, data_fur_color_cinnamon] }
dataframe = pandas.DataFrame(data_dict)
dataframe.to_csv("squirrel_count.csv")

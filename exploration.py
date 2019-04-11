# Packages
from sys import argv
import csv
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math


def read_csv(file):
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        data = []
        for row in csv_reader:
            data.append(row)
    return data


def write_csv(data, filename):
    with open('%s.csv' % (filename), 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in data:
            csv_writer.writerow(row)
    print('%s.csv saved' % (filename))


def get_column(column_number, x):
    column = []
    for i in range(1, len(x)):
        column.append(x[i][column_number])
    return column


def get_deck(cabin_column_number, x):
    deck = []
    deck.append('Deck')
    for i in range(1, len(x)):
        if x[i][cabin_column_number] == '':
            deck.append('Unknown')
        else:
            current_deck = x[i][cabin_column_number][0]
            deck.append(current_deck)
    return deck


def get_title(name_column_number, x):
    titles = []
    titles.append('Title')
    for i in range(1, len(x)):
        name = x[i][name_column_number]
        end_index = 0
        for j in range(len(name)):
            if name[j] == ',':
                start_index = j + 2
            elif name[j] == '.' and end_index == 0:
                end_index = j + 1
                title = name[start_index:end_index]
                titles.append(title)
            else:
                pass
    return titles


def add_new_column(new_column, x):
    new_data = []
    for i in range(len(x)):
        new_row = []
        for j in range(len(x[i])):
            new_row.append(x[i][j])
        new_row.append(new_column[i])
        new_data.append(new_row)
    return new_data


def make_histogram(x):
    x.value_counts().plot(kind='bar')

    n, bins, patches = plt.hist(x, bins=[], align = 'mid', rwidth=0.5)
    plt.xlabel('Deck')
    plt.ylabel('Number of passengers')
    plt.axis(['A', 'Unknown' , 0, 700])
    plt.show()


def get_age_categories(age_column_number, x):
    age_categories = []
    age_categories.append('Age_categorie')
    for i in range(1, len(x)):
        age = x[i][age_column_number]
        if age == '':
            age_categories.append('Unknown')
        else:
            try:
                age = int(age)
            except:
                age = float(age)
            if age <= 2:
                age_categories.append('Infant')
            elif age <= 6:
                age_categories.append('Young Child')
            elif age <= 12:
                age_categories.append('Child')
            elif age <= 18:
                age_categories.append('Adolescent')
            elif age < 60:
                age_categories.append('Adult')
            else:
                age_categories.append('Elderly')
    return age_categories


def get_persons(age_column_number, sex_column_number, x):
    who = []
    who.append('Who')
    for i in range(1, len(x)):
        age = x[i][age_column_number]
        if age == "":
            who.append('unknown')
        else:
            try:
                age = int(age)
            except:
                age = float(age)
            if age < 18:
                who.append('child')
            else:
                sex = x[i][sex_column_number]
                who.append(sex)
    return who


def count_if(column, condition):
    return sum(1 for x in column if x == condition)


def average_age(pclass, sex, family_size, x):
    pclass_column_number = 2
    sex_column_number = 4
    family_size_column_number = 12
    age_column_number = 5

    number_of_people = 0
    sum_of_ages = 0
    for i in range(1, len(x)):
        if x[i][pclass_column_number] == pclass and x[i][sex_column_number] == sex and x[i][family_size_column_number] == family_size:
            age = x[i][age_column_number]
            if age == "":
                pass
            else:
                try:
                    age = int(age)
                except:
                    age = float(age)
                number_of_people += 1
                sum_of_ages += age
    if number_of_people == 0:
        for i in range(1, len(x)):
            if x[i][pclass_column_number] == pclass and x[i][sex_column_number] == sex:
                age = x[i][age_column_number]
                if age == "":
                    pass
                else:
                    try:
                        age = int(age)
                    except:
                        age = float(age)
                        number_of_people += 1
                        sum_of_ages += age

    average = sum_of_ages / number_of_people
    return average


def fill_missing_ages(x):
    age_column_number = 5
    pclass_column_number = 2
    sex_column_number = 4
    family_size_column_number = 12

    ages = []
    ages.append('Age_transfromed')

    for i in range(1, len(x)):
        if x[i][age_column_number] == "":
            pclass = x[i][pclass_column_number]
            sex = x[i][sex_column_number]
            family_size = x[i][family_size_column_number]
            age = average_age(pclass, sex, family_size, x)
        else:
            age = x[i][age_column_number]
        ages.append(age)

    return ages


def main():
    # input data files
    train_data = argv[1]
    train_data = read_csv(train_data)
    #fare = get_column(9, train_data)
    #make_histogram(fare))
    get_age_categories(15, train_data)
    


    #sns.set(style="darkgrid")
    #titanic = pd.read_csv(train_data)
    #titanic = titanic.sort_values(by="Title")
    #ax = sns.countplot(x="Title", hue="Survived", data=titanic)
    #g = sns.catplot(x="", hue="Who", col="Survived", data=titanic, kind="count", height=4, aspect=.7);
    #plt.show()


if __name__ == '__main__':
    main()

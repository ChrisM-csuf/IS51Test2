
def main():
    calculate_percent_above_average(get_grades())


def get_grades():
    infile = open('Final.txt', 'r')
    lines = infile.readlines()
    grades = [int(i) for i in lines]
    return grades


def calculate_percent_above_average(grades):
    sum = 0
    for i in grades:
        sum = sum + i
    average = sum / len(grades)


    num_above_average = 0
    for i in grades:
        if i > average:
            num_above_average = num_above_average + 1

    percent_above = round((num_above_average / average) * 100, 2)
    print(f"{percent_above}% of values are higher than the average")


main()
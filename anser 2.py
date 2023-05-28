from datetime import date
def test(month, year):
    return str(date(year,month,9).strftime("%A")=='Monday')



month = 5;
year = 2023;
print("\nMonth No.: ", month, " Year: ", year);
print("Check  month and year  Monday  on 9th.: " + test(month, year));


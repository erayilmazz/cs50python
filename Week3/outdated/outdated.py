import string


months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    date = input("Date: ")
    if ',' in date:
        list1 = date.split()
        if list1[0] in months:
            year = int(list1[2])
            month = int(months.index(list1[0]) + 1)
            day = list1[1].replace(",","")
            if year <= 9999 and month <= 12 and int(day) <= 31:
                print(f"{year}-{month:02}-{int(day):02}")
                break

    elif '/' in date:
        list2 = date.split('/')
        if list2[0] in months:
            continue
        year = int(list2[2])
        month = int(list2[0])
        day = int(list2[1])
        if year <= 9999 and month <= 12 and day <= 31:
            print(f"{year:04}-{month:02}-{day:02}")
            break



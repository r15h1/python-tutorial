#key-value pairs
#use curly brackets {}
#keys must be unique
months = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

#January
print(months["Jan"])
print(months.get("Jan"))

#error - key not found
#print(months["jnnn"])

#no error - get None
print(months.get("jnn"))
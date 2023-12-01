def date_converter(us):
    mm = us[0:2]
    dd = us[3:5]
    yy = us[6:8]
    return "20"+yy+"-"+mm+"-"+dd


# Main program starts
us = "10/07/22"
sw = date_converter(us)
print(us, "==>", sw)

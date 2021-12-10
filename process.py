log_file = open("um-server-01.txt")#this line connects the um-server file, simliar to linking files in html, css, and JavaScript


def sales_reports(log_file):#this is the beginning of a function
    for line in log_file:#looping through the data from um-server file
        line = line.rstrip()#this line makes a new varialbe of the data with no excess whitespace
        day = line[0:3]#converts numbers to a string if there are any
        if day == "Mon":#boolean saying if there is a line with Mon then print that line
            print(line)


sales_reports(log_file)#invoking the function

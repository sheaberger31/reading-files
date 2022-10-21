def read_all():
    file = open('days.txt', 'r')
    all_lines = file.read()
    print(all_lines)
    file.close()
    
def list_file():
    file = open('days.txt', 'r')
    days_list = file.readlines()
    print(days_list)
    weekday = (days_list[3])
    print("The fourth day of the week is", weekday)
    file.close()
    
def read_linebyline():
    file = open('days.txt', 'r')
    line = file.readline()
    print(line)
    
    
    line2 = file.readline()
    print(line2)
    
    file.close()
    
def main():
    read_all()
    list_file()
    read_linebyline()
    
main()
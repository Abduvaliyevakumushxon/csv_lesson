import csv
def get_country_column(file_name):
    """
    This function takes a filename as input and returns a list of countries
    Args:
        file_name: string
    Returns:
        list
    """
    f=open('data.csv')
    file_name=csv.reader(f,delimiter='.')
    l=[]
    for i in file_name:
        l.append(i)
    return l
print(get_country_column('data.csv'))

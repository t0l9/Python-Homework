
name = input('Enter name: ').capitalize()
surname = input('Enter surname: ').capitalize()
year = int(input('Enter year: '))
city = input('Enter city: ').capitalize()
email = input('Enter email: ')
telephone = int(input('Enput telephone: '))

def get_parametrs(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])

print(get_parametrs(surname, name, year, city, email, telephone)) 

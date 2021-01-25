def main():
    z1()

def z1():
    worker = ['Olya', 'Silyutina', 350000, 6]
    user_name = worker[0]
    user_family = worker[1]
    position = ' 123'
    if worker[3] < 2 :
        position = 'junior'
    elif (worker[3] >= 2 and worker[3] <= 5) :
        position = 'middle'
    elif worker[3] > 5 :
        position = 'senior'
        status = user_name +" "+ user_family + " is " + position
        print(status)

main()

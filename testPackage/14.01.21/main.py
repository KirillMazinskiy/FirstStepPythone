def main():
    z2()

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

def z2():
    workers = [['Ivan', 'Ivanov', 100000, 7], ['Petr', 'Petrov', 150000, 2], ['Sidor', 'Sidorov', 200000, 3]]
    for i in range(len(workers)):
            status = '123'
            user_name = workers[i][0]
            user_family = workers[i][1]
            position = '123'
            if workers[i][3] < 2:
                position = 'junior'
            elif (workers[i][3] >= 2 and workers[i][3] <= 5) :
                position = 'middle'
            elif workers[i][3] > 5 :
                position = 'senior'
            status = user_name +" "+ user_family + " is " + position
            print(status)

main()


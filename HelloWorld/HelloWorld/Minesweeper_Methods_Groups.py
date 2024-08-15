import random
import csv

class Field:
    def __init__(self,x,y,BOMB,TURNED,NEIGBOR):
        self.x = x
        self.y = y
        self.bomb = BOMB
        self.turned = TURNED
        self.neighbor = NEIGBOR

    def turn(self,k, fields,b):
        # print(f'{self} Turned')
        if self.bomb:
            print('Game Lost')
            self.neighbor = 'X'
            self.turned = True
            return True

        elif not self.turned:
           # print(f'Anzahl der Nachbarn = {self.neighbor}')
            self.turned = True
            if self.neighbor == 0:
                objs = fields
                if not objs[b].x == k[1] - 1:
                    objs[b + 1].turn(k,fields,b + 1)
                    if not objs[b].y == k[0] - 1:
                        objs[b + k[1] + 1].turn(k,fields,b + k[1] + 1)
                    if not objs[b].y == 0:
                        objs[b - k[1] + 1].turn(k,fields,b - k[1] + 1)
                if not objs[b].x == 0:
                    objs[b - 1].turn(k,fields,b - 1)
                    if not objs[b].y == k[0] - 1:
                        objs[b + k[1] - 1].turn(k,fields,b + k[1] - 1)
                    if not objs[b].y == 0:
                        objs[b - k[1] - 1].turn(k,fields,b - k[1] - 1)
                if not objs[b].y == 0:
                    objs[b - k[1]].turn(k,fields,b - k[1])
                if not objs[b].y == k[0]-1:
                    objs[b + k[1]].turn(k,fields,b + k[1])


def create_field(k):
    objs = [Field(0,0,False,False,0) for i in range(k[1]*k[0])]
    for i in range(k[0]):
        for j in range(k[1]):
            objs[i*k[1]+j].x=j
            objs[i*k[1]+j].y=i
    for i in range(k[2]):
        while True:
            b = random.randint(0,k[1] * k[0] - 1)
            if not objs[b].bomb:
                objs[b].bomb = True
                if not objs[b].x == k[1] - 1:
                    objs[b + 1].neighbor += 1
                    if not objs[b].y == k[0] - 1:
                        objs[b + k[1] + 1].neighbor += 1
                    if not objs[b].y == 0:
                        objs[b - k[1] + 1].neighbor += 1
                if not objs[b].x == 0:
                    objs[b - 1].neighbor += 1
                    if not objs[b].y == k[0] - 1:
                        objs[b + k[1] - 1].neighbor += 1
                    if not objs[b].y == 0:
                        objs[b - k[1] - 1].neighbor += 1
                if not objs[b].y == 0:
                    objs[b - k[1]].neighbor += 1
                if not objs[b].y == k[0]-1:
                    objs[b + k[1]].neighbor += 1
                # print(f'Mine {b} set to true')
                break
    return objs


def print_field(k, fields):
    height = k[0]
    width = k[1]
    Output_1 = '   '
    for i in range(width):
        if i < 11:
            Output_1 += ' ' + str(i) + ' '
        else:
            Output_1 += '' + str(i) + ' '
    print(Output_1)
    print('')
    for i in range(height):
        if i*width < 10:
            Output = str(i*width) + '  '
        else:
            Output = str(i * width) + ' '
        for j in range(width):
            if fields[i*width+j].turned:
                Output += ' ' + str(fields[i*width+j].neighbor) + ' '
            else:
                Output += ' H '
        Output += '  ' + str(i*width+j)
        print(Output)
    print('')
    print(Output_1)

def select_field_constraints():
    try:
        h = int(input('select height: '))
        w = int(input('select width: '))
        mines = int(input('select mines: '))
    except ValueError:
        print('sorry - numbers have to be used to define height')
        yes_no = input('you want to retry (Y)es/(N)o? ')
        if yes_no.lower() == 'y':
            answer = select_field_constraints()
            h = answer[0]
            w = answer[1]
            mines = answer[2]
        else:
            h = 10
            w = 10
            mines = 5
    return h, w, mines

def safe_field(fields):
    with open("groups.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(['x', 'y', 'bomb', 'turned', 'neighbor'])
        for field in fields:
            writer.writerow([field.x, field.y, str(field.bomb), str(field.turned), field.neighbor])
def load_field():
    imported_field = []
    k = [0, 0, 0]
    with open('groups.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            x = int(row["x"])
            y = int(row["y"])
            bomb = False
            if row['bomb'] == 'True':
                bomb = True
            turned = False
            if row['turned'] == 'True':
                turned = True
            neighbor = int(row['neighbor'])
            imported_field.append(Field(x, y, bomb, turned, neighbor))
            if bomb:
                k[2] += 1
            if y >= k[0]:
                k[0] += 1
            if x >= k[1]:
                k[1] += 1
    return imported_field, k
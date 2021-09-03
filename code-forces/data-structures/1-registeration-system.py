names = {}

def register(name):
    try:
        names[name] += 1
        return name + str(names[name])
    except:
        names[name] = 0
        return 'OK'
    

test = [
    'abacaba',
    'acaba',
    'abacaba',
    'acab'
]

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        print(register(name))
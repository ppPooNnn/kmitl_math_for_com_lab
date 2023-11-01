Profs = ['อ.วิชญะ', 'อ.ธีระ', 'อ.สันธนะ']
Cars = ['Mini', 'Honda', 'Toyota']

Profs_Pref =    { 
                    'อ.วิชญะ' : ['Honda', 'Mini', 'Toyota'],
                    'อ.ธีระ' : ['Mini', 'Toyota', 'Honda'],
                    'อ.สันธนะ' : ['Mini', 'Honda', 'Toyota']
                }

Cars_Pref =  {  
                'Mini' : ['อ.วิชญะ', 'อ.ธีระ', 'อ.สันธนะ'],
                'Honda' : ['อ.สันธนะ', 'อ.ธีระ', 'อ.วิชญะ'],
                'Toyota' : ['อ.วิชญะ', 'อ.ธีระ', 'อ.สันธนะ']
             }

def main() :
    Profs_free = list(Profs)
    
    Matches = { 'อ.วิชญะ' : '',
                'อ.ธีระ' : '',
                'อ.สันธนะ' : ''       
              }
    
    key_list = list(Matches.keys())
    
    while len(Profs_free) > 0:
        for prof in Profs_free:
            for car in Profs_Pref[prof]:
                if car not in list(Matches.values()):
                    Matches[prof] = car
                    print(prof, 'this is prof', Profs_free, 'this is prof free')
                    print('------------------------------------------------------------')
                    Profs_free.remove(prof)
                    break
                elif car in list(Matches.values()) :
                    current_pair = list(Matches.keys())[list(Matches.values()).index(car)]
                    car_list = Cars_Pref.get(car)
                    if car_list.index(prof) < car_list.index(current_pair) :
                        Matches[prof] = car
                        print('from under condition')
                        print(prof, 'this is prof', Profs_free, 'this is prof free')
                        Profs_free.remove(prof)
                        Matches[current_pair] = ''
                        Profs_free.append(current_pair)
    
    for prof in Matches.keys() :
        print(prof, ' buy ', Matches[prof])

if __name__ == "__main__" :
    main()
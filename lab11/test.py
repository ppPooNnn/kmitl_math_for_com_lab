Men = ['M1', 'M2', 'M3', 'M4']
Women = ['W1', 'W2', 'W3', 'W4']

Men_Pref =  { 'M1' : ['W1', 'W3', 'W4', 'W2'],
              'M2' : ['W2', 'W1', 'W3', 'W4'],
              'M3' : ['W2', 'W4', 'W3', 'W1'],
              'M4' : ['W3', 'W1', 'W2', 'W4']
            }

Women_Pref =  { 'W1' : ['M1', 'M4', 'M2', 'M3'],
                'W2' : ['M3', 'M1', 'M2', 'M4'],
                'W3' : ['M2', 'M4', 'M1', 'M3'],
                'W4' : ['M1', 'M4', 'M3', 'M2']
              }

def main() :
    Men_Free = list(Men)
    
    Matches = { 'M1' : '',
                'M2' : '',
                'M3' : '',
                'M4' : ''       
              }
    
    while len(Men_Free) > 0:
        for man in Men_Free:
            for woman in Men_Pref[man]:
                if woman not in list(Matches.values()):
                    Matches[man] = woman
                    print(Men_Free, 'this is men free', man, 'this is man')
                    Men_Free.remove(man)
                    # print(man, ' is temporary engage to ', woman)
                    break
                elif woman in list(Matches.values()) :
                    current_pair = list(Matches.keys())[list(Matches.values()).index(woman)]
                    w_list = Women_Pref.get(woman)
                    if w_list.index(man) < w_list.index(current_pair) :
                        Matches[man] = woman
                        Men_Free.remove(man)
                        Matches[current_pair] = ''
                        Men_Free.append(current_pair)
                        # print(woman, ' was engaged with ', current_pair, 'but now engage with ', man)
    
    for man in Matches.keys() :
        print(man, ' is engage to ', Matches[man])

if __name__ == "__main__" :
    main()
inventar = {                  
             'ложка': 22,           
             'нож':21,          
             'вилка':(20),          
             'топор':(200),           
             'котел':(90),            
             'спички':(5),           
             'соль':(1),      
             'веревка':(80),     
            }

while True:
    print(f"Инвентрь в сундуке =  {inventar}")
    a = input("Введите название нового предмета (или Enter - для продолжения): ")
    if not a:
        break
    ves = input("Введите вес предмета: ")
   
    r = inventar.get(a, None)
    if r is None:
        inventar[a] = ves  

while True:
    print(f"Инвентрь в сундуке =  {inventar}")
    a = input("Введите название предмета для его удаления (или Enter - выход): ")
    if not a:
        break
    r = inventar.pop(a, None)
    if r is None:
        inventar[a] = ves 
print(f"Инвентря в сундуке стало =  {inventar}")
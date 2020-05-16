
class Route:

    destinos = []
    
    size = 0
    town_start = None
    town_end = None

    def __init__(self, town_start, town_end, size):
        self.town_start = town_start
        self.town_end = town_end
        self.size = size

class TrainStation:
    
    name = ''

    def __init__(self, name,  *args, **kwargs):
        self.name = name

    def __repr__(self):
        return self.name
    
class Itinerary:
    routes = []
    def addRoute(self, route):
       self.routes.append(route)

    def getDistance(self, args, i=0):
        if (i > (len(args) - 2)):
            return 0
        else:
            size = 0
            town_start = args[i]
            town_end = args[i+1]
            for route in self.routes:
                isStart = route.town_start.name == town_start
                isEnd = route.town_end.name == town_end 
                if (isStart and isEnd):
                    counter = self.getDistance(args, i +1)
                    if (counter == -1):                        
                        return 0
                    else:
                        return route.size + counter
            return -1
    
    def routesQuantity(self, point_start, point_stop, max_steps, steps = 0, exactly = False):
        if (max_steps < 0):
            return 0
        else:
            for i in range(len(self.routes)):
                route = self.routes[i]
                print(f'{point_start}{i} - Origem: {route.town_start.name} | Destino: {route.town_end.name}')
                if (route.town_start.name == point_start and route.town_end.name != point_stop):
                    print(f'Into - Origem: {route.town_start.name} | Destino: {route.town_end.name}')
                    steps = self.routesQuantity(route.town_end.name, point_stop, max_steps - 1, steps)                                        
                elif (route.town_start.name == point_start and route.town_end.name == point_stop):
                    if (not exactly and max_steps == 0):
                        return 0
                    elif ((exactly and max_steps == 0) or not exactly):
                        steps += 1
                        print(f'Steps: : {steps}')
                        print(f'Encontrei - Origem: {route.town_start.name} | Destino: {route.town_end.name}')
                        # return steps
            return steps
                

                    
                

                
'''
Comentários

entrar C
entrar em todos os roteiro de C até max_steps
verificar se o nó de destino é igual a c

C => C



'''
        

a = TrainStation("A")
b = TrainStation("B")
c = TrainStation("C")
d = TrainStation("D")
e = TrainStation("E")

itinerary = Itinerary()
itinerary.addRoute(Route(a, b, 5))
itinerary.addRoute(Route(b, c, 4))
itinerary.addRoute(Route(c, d, 8))
itinerary.addRoute(Route(d, c, 8))  
itinerary.addRoute(Route(d, e, 6))
itinerary.addRoute(Route(a, d, 5))
itinerary.addRoute(Route(c, e, 2))
itinerary.addRoute(Route(e, b, 3))
itinerary.addRoute(Route(a, e, 7))

routes = [
    ['A', 'B', 'C'],
    ['A', 'D'],
    ['A', 'D','C'],
    ['A', 'E', 'B', 'C', 'D'],
    ['A', 'E', 'D']
]
for i, route in enumerate(routes):
    distance = itinerary.getDistance(route)
    if (distance == 0):
        print('NO SUCH ROUTE')
    else: 
        print(f'{i + 1} # {distance}')

'''
print('Teste ---- C para C ')
print(itinerary.routesQuantity('C', 'C', 3))

print('\n\nTeste ---- A para C ')
print(itinerary.routesQuantity('A', 'C', 4, 0, True))
'''
print('\n\nTeste ---- C para C ')
print(itinerary.routesQuantity('C', 'C', 30))


class Route:
    
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

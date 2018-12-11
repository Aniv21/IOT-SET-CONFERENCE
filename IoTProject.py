import googlemaps
import json
import gmplot
import re
import operator

File = open('workfile3.txt', 'r')
shortest_path = []

def dijkstra(matrix, m, n, source):
    #k=int(input("Enter the source vertex"))
    k = source
    cost = [[0 for x in range(m)] for x in range(1)]
    offsets = []
    offsets.append(k)
    elepos = 0
    for j in range(m):
        cost[0][j] = matrix[k][j]
    mini = 999
    for x in range(m-1):
        mini = 999
        for j in range(m):
            if cost[0][j] <= mini and j not in offsets:
                mini = cost[0][j]
                elepos = j
        offsets.append(elepos)
        for j in range(m):
            if cost[0][j] > cost[0][elepos] + matrix[elepos][j]:
                cost[0][j] = cost[0][elepos] + matrix[elepos][j]
    #print("The shortest path",offsets)
    print("The cost to various vertices in order", cost)
    #sorted_x = zip(offsets,cost[0])
    for i in range(len(offsets)):
        shortest_path.append(offsets[i])
    offsets_path = dict(zip([0, 1, 2, 3, 4, 5, 6], cost[0]))
    sorted_x = sorted(offsets_path.items(), key=operator.itemgetter(1))
    return sorted_x

gmaps = googlemaps.Client(key='AIzaSyCgjB9JkVime1PiPUjlTUpJKT2XOJlTejs')
gmapsdis = googlemaps.Client(key='AIzaSyCyTYekrIGTTiLONwGwwbUSY6Chth8w2r4')
gmapdir = googlemaps.Client(key='AIzaSyB1C0zBRz7o5nwHcFP2N6Z6NyKfHKQYuXU')
gmaproad = googlemaps.Client(key='AIzaSyCoOXG5BGT7a_wDM9v4w_U50ufd6VpbtLs')

#directions = gmaps.directions(address, destination)
distanceMat = json.loads(File.read())

print type(distanceMat)

jsondis = ""

jsondis = json.dumps(distanceMat)

Sources = []
Destinations = []

Sources = distanceMat["origin_addresses"]
Destinations = distanceMat["destination_addresses"]




'''
Sources.append("D Annexe VIT University Vellore, Tamil Nadu 632014 India")
Sources.append("Nelson Mandela Block VIT University Vellore, Tamil Nadu 632014 India")
Sources.append("VIT G Block Men's Hostel VIT University Vellore, Tamil Nadu 632014 India")
Sources.append("Choti Pepsi Dukan VIT University Vellore, Tamil Nadu 632014 India")
Sources.append("L Block Mens Hostel VIT University Vellore, Tamil Nadu 632014,India")
Sources.append("Quaid E Millat Muhammad Ismail Block Tamil Nadu 632014 India")
Sources.append("Sardar Vallabhbhai Patel Block VIT University, Near Katpadi Rd Vellore, Tamil Nadu 632014 India")
Sources.append("Charles Darwin Block N Block , VIT University Vellore, Tamil Nadu 632014 India")
'''


for i in range(len(Sources)):
    print Sources[i]

print len(distanceMat["rows"])
DistanceMatrix = []
for i in range(len(distanceMat["rows"])):
    Rows = []
    for j in range(len(distanceMat["rows"][i]["elements"])):
        Rows.append(distanceMat["rows"][i]["elements"][j]["distance"]["text"])
    DistanceMatrix.append(Rows)
'''
for i in range (len(distanceMat["rows"])) :
      
      for j in range (len(distanceMat["rows"][i]["elements"])):
          print (DistanceMatrix[i][j]),
      print "\n"
'''
for i in range(len(distanceMat["rows"])) :
    for j in range(len(distanceMat["rows"][i]["elements"])):
        if(DistanceMatrix[i][j] == '1 m'):
            DistanceMatrix[i][j] = 0
        elif(re.match(r'([0-9]*) km',DistanceMatrix[i][j])!="None"):
              DistanceMatrix[i][j] = float(DistanceMatrix[i][j][0:3])
      
for i in range (len(distanceMat["rows"])) :
      
      for j in range (len(distanceMat["rows"][i]["elements"])):
          print (DistanceMatrix[i][j]),
      print "\n"

Longitudes = []
Latitudes = []
LongandLan = []


for i in range (len(Sources)):
    LNL =[]
    geocode_result = gmaps.geocode(Sources[i])
    #geocode_result = json.loads(geocode_result)
    Latitudes.append(geocode_result[0]["geometry"]["location"]["lat"])
    Longitudes.append(geocode_result[0]["geometry"]["location"]["lng"])
    LNL.append(geocode_result[0]["geometry"]["location"]["lat"])
    LNL.append(geocode_result[0]["geometry"]["location"]["lng"])
    LongandLan.append(LNL)


#print LongandLan

Graph = dijkstra(DistanceMatrix,len(Sources)-8,len(Sources)-8,0);

print shortest_path

for i in range (len(shortest_path)):
    print Sources[shortest_path[i]]
    geocode_result = gmaps.geocode(Sources[shortest_path[i]])
    #geocode_result = json.loads(geocode_result)
    Latitudes.append(geocode_result[0]["geometry"]["location"]["lat"])
    Longitudes.append(geocode_result[0]["geometry"]["location"]["lng"])

directions = gmaproad.snap_to_roads(LongandLan,True)


DirectionLatitudes =[]
DirectionLongitudes =[]

for i in range (len(directions)):
    
    DirectionLatitudes.append(directions[i]["location"]["latitude"])
    DirectionLongitudes.append(directions[i]["location"]["longitude"])

#print DirectionLatitudes
#print DirectionLongitudes

#print Latitudes
#print Longitudes

#print gmapdir.directions("VIT outdoor stadium to N block shortcut, Tamil Nadu 632014","Main Building, VIT University, Vellore, Tamil Nadu" )

gmap =  gmplot.GoogleMapPlotter.from_geocode("VIT University",50)
gmap2 = gmplot.GoogleMapPlotter.from_geocode("VIT University",20)
gmap3 = gmplot.GoogleMapPlotter.from_geocode("VIT University",20)
gmap4 = gmplot.GoogleMapPlotter.from_geocode("VIT University",100)


gmap.plot(Latitudes, Longitudes, 'cornflowerblue', edge_width=10)
gmap2.scatter(Latitudes, Longitudes, '#3B0B39', size=40, marker=False)
gmap3.plot(Latitudes, Longitudes)




gmap4.plot(DirectionLatitudes, DirectionLongitudes, 'cornflowerblue', edge_width=8)

gmap.draw("mymap.html")
gmap2.draw("mymap2.html")
gmap3.draw("mymap3.html")

gmap4.draw("shortest_path.html")


Graph = dijkstra(DistanceMatrix,len(Sources)-8,len(Sources)-8,0)

#print Graph

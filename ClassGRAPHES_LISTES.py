from files_de_priorite import*

class Arc:
    def __init__(self, dest, poids):
        self.dest = dest
        self.poids = poids

    
class graphe:
    def __init__(self, n, type):
        self.nbsommets = n
        self.typeG = type
        self.listadj = [[] for i in range(n)]

    def affiche(self):
        for i in range(self.nbsommets):
            print(f"Les adjacents du sommet {i} sont:")
            if len(self.listadj[i]) == 0:
                   print("Aucun")
            else: 
                for arc in self.listadj[i]:
                    print((arc.dest, arc.poids), end = "")
                print(end ="\n")
               
                
    def addarc(self,source, dest, poids):
        if (0 <= source < self.nbsommets)  and (0 <= dest < self.nbsommets):
            self.listadj[source].append(Arc(dest,poids))
            if self.typeG =='NON_ORIENTED':
                self.listadj[dest].append(Arc(source,poids))
            return 'OK'
        else:
            return 'ERROR'
        
   
    
    def _min_distance(self, distances, visited):
        min_distance = float('inf')
        min_vertex = None
        for v in range(self.nbsommets):
            if distances[v] < min_distance and v not in visited:
                min_distance = distances[v]
                min_vertex = v
        return min_vertex

    def dijkstra(self, start):
        distances = [float('inf')] * self.nbsommets
        distances[start] = 0
        visited = []  # Pour stocker les sommets traversés
        paths = [[] for _ in range(self.nbsommets)]  # Pour stocker le chemin optimal à chaque mise à jour

        while len(visited) < self.nbsommets:
            current_vertex = self._min_distance(distances, visited)
            if current_vertex is None:
                break  # Tous les sommets ont été visités
            visited.append(current_vertex)

            if self.listadj[current_vertex]:
                for arc in self.listadj[current_vertex]:
                    neighbor = arc.dest
                    weight = arc.poids
                    new_distance = distances[current_vertex] + weight

                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        paths[neighbor] = paths[current_vertex] + [current_vertex]

        self._print_path(start, distances, paths)
        #print("Sommets traversés:", visited)

        return distances, paths

    def _print_path(self, start, distances, paths):
        for i, distance in enumerate(distances):
            path = paths[i] + [i]
            print(f"Chemin le plus court de {start} à {i}: {path}, Distance: {distance}")

    
        
        
    
            

#Exemple utilisation:
        
Graphe1 = graphe(7,'NON_ORIENTED')
#> crée un graphe non-orienté avec 7 sommets

Graphe1.addarc(0,1, 40)
#> ajoute un arc de 0 à 1 de poids 40

Graphe1.addarc(0,4, 50)

Graphe1.addarc(4,5, 30)

Graphe1.addarc(4,6, 100)

status = Graphe1.addarc(3,6, 50)
print(status)
#> affiche OK

status = Graphe1.addarc(10,4, 50)
print(status)
#> affiche ERROR

Graphe1.affiche()
#> affiche les listes d'adjacence de Graphe1

start_vertex = 0
shortest_distances, shortest_paths = Graphe1.dijkstra(start_vertex)

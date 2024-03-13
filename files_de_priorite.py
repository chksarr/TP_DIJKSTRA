# Définition de la classe Data ###############################################################################
class Data:
    def __init__(self, key, priority):
        self.key = key  
        self.priority = priority  

# Définition de la classe File pour la file de priorité pour un tas de type MIN######################################
class File:
    def __init__(self):
        # Initialisation de la file de priorité comme une liste vide.
        self.heap = []

    # Fonction auxiliaire pour obtenir l'indice du parent d'un élément###############################################
    def parent(self, i):
        return (i - 1) // 2

    # Fonction auxiliaire pour obtenir l'indice du fils gauche d'un élément###########################################
    def left_child(self, i):
        return 2 * i + 1

    # Fonction auxiliaire pour obtenir l'indice du fils droit d'un élément###############################################
    def right_child(self, i):
        return 2 * i + 2

    # Méthode pour insérer un objet de type Data dans la file de priorité##############################################
    def insert(self, data):
        self.heap.append(data)  # Ajoute l'élément à la fin de la liste (fin de la file )
        self.heapify_up(len(self.heap) - 1) # Rétablit la propriété du tas en remontant l'élément ajouté nbr de noeur -1 car on commence par l indice 0

    # Méthode pour rétablir la propriété du tas à partir d'une position donnée ######################################################
    def heapify_up(self, i):
        while i > 0 and self.heap[self.parent(i)].priority > self.heap[i].priority:
            # Échange les éléments si la priorité du parent est plus grande que celle de l'élément actuel.
            temp = self.heap[i]  # Sauvegarde la valeur de l'élément à l'indice i
            self.heap[i] = self.heap[self.parent(i)]  # Remplace la valeur de l'élément à l'indice i par celle de son parent
            self.heap[self.parent(i)] = temp  # Remplace la valeur du parent par la valeur sauvegardée temporairement
            i = self.parent(i)  # le i pointe sur le parent mnt  on continue jusqua ce que c bon

    # Méthode pour afficher le contenu de la file de priorité#########################################################
    def affiche(self):
        for data in self.heap:
            print(f"Key: {data.key}, Priority: {data.priority}")

    # Méthode pour extraire et supprimer l'élément de priorité minimale##############################################
    def extract_min(self):
        if not self.empty():
            if len(self.heap) == 1:
                return self.heap.pop() # si on a un seule elemnt on le retourne directement
            root = self.heap[0] # on stocke dans root la racine
            self.heap[0] = self.heap.pop()
            # Rétablit la propriété du tas en descendant l'élément.
            self.heapify_down(0)
            return root  # retourner le minimum  qui est a la racine car c un tas MIN

    # Méthode pour rétablir la propriété du tas à partir de la racine.
    def heapify_down(self, i):
        left = self.left_child(i)
        right = self.right_child(i)
        smallest = i

        if left < len(self.heap) and self.heap[left].priority < self.heap[i].priority:
            smallest = left

        if right < len(self.heap) and self.heap[right].priority < self.heap[smallest].priority:
            smallest = right

        if smallest != i:
            # Échange les éléments si nécessaire pour maintenir la propriété du tas.
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            # Rétablit la propriété du tas en descendant.
            self.heapify_down(smallest)

    # Méthode pour tester si la file de priorité est vide.
    def empty(self):
        return len(self.heap) == 0
    
    # Méthode pour la MAJ
    def update(self, key, new_priority):
        # Recherche de l'élément correspondant à la clé dans la file
        for data in self.heap:
            if data.key == key:
                # Mise à jour de la priorité si la nouvelle priorité est meilleure
                if new_priority < data.priority:
                    data.priority = new_priority
                    # Rétablit la propriété du tas en remontant l'élément mis à jour
                    index = self.heap.index(data)
                    self.heapify_up(index)
                return

"""
# Exemple d'utilisation
file_de_priorite = File()
file_de_priorite.insert(Data("A", 3))
file_de_priorite.insert(Data("B", 2))
file_de_priorite.insert(Data("C", 4))
file_de_priorite.insert(Data("D", 1))

print("Contenu de la file de priorité:")
file_de_priorite.affiche()

min_element = file_de_priorite.extract_min()
print(f"Élément de priorité minimale extrait: Key: {min_element.key}, Priority: {min_element.priority}")

print("Contenu de la file de priorité après extraction:")
file_de_priorite.affiche()"""

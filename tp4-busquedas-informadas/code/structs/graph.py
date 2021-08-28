class Graph:
    class Node:
        def __init__(self, name, value, key = None, parent = None):
            self.value = value;
            self.name = name;
            self.key = key;
            self.parent = parent;

        def getValue(self):
            return self.value;

        def getName(self):
            return self.name;

        def getParent(self):
            return self.parent;

        def getKey(self):
            return self.key;

    def __init__(self):
        #Guarda los vertices
        """
        V = {
            'name': name,
            'value': value
        }
        """
        self.V = {};
        #Guarda las aristas
        """
        E = {
            'vertexA': {
                'vertexB': weight,
                'vertexC': weight
            },
            'vertexB': {
                'vertexC': weight
            }
        }
        """
        self.E = {};

    def addVertex (self, name, value, key = None, childrens = {}):
        #Si no hay vertice con ese nombre, se crea
        if(not self.getVertex(name)):
            self.V[name] = self.Node(name, value, key);
            self.E[name] = {};
            self.addChildrens(name, childrens);

    def addConection(self, V1, V2, weight = 0):
        try:
            #Si ambos vértices existen en el grafo
            self.V[V1];
            self.V[V2];
            try:
                #Si existe la conexion, reasigna el peso
                self.E[V2][V1];
                self.E[V2][V1] = weight;
            except (Exception):
                #Agrega la arista al revez por si se quiere agregar la misma pero invertida 
                self.E[V1][V2] = weight;
                self.V[V2].parent = self.V[V1];
        except (Exception):
            pass

    def addChildrens (self, parent, childrens = {}):
        for c in childrens:
            try:
                #Si no existe el vértice en el grafo, lo crea
                self.V[c]
            except (Exception):
                try:
                    childrens[c]["key"];
                    self.addVertex(c, childrens[c]["value"], childrens[c]["key"]);
                except (Exception):
                    try:
                        childrens[c]["value"];
                        self.addVertex(c, childrens[c]["value"]);
                    except (Exception):
                        self.addVertex(c, childrens[c]);
                        
            #Agrega la conexion entre los vértices
            self.addConection(parent, c);

    def getVertex (self, name):
        try:
            return self.V[name];
        except:
            pass

    def getAllVertex(self):
        return self.V

    def getConections (self, V):
        return self.E[V];

    def getCountVertex (self):
        return len(self.V.keys());

    def show (self):
        for e in self.E:
            print(self.V[e].getName(), "|", self.V[e].getValue(), ": ",end="");
            print(
                list(
                    map(
                        lambda x: x,
                        self.E[e]
                    )
                )
            );

import numpy as np

# components of distribution
poisonous_components = 6
edible_components = 5


def get_data():
    reading_data = []
    f = open('agaricus-lepiota.data.txt')
    line = f.readline()
    while line:
        reading_data.append(line.split(',')[:-1])
        line = f.readline()
    f.close()
    return reading_data


def prior_probability():
    sum_of_poisonous = 0
    for line in Data:
        if line[0] == 'p': sum_of_poisonous +=1
    poisonous_probability = float(sum_of_poisonous)/Data.__len__()
    return 1-poisonous_probability, poisonous_probability


def HEOM_distance(x, y):
    distance = 0
    for i in range(len(x))[1:]:
        if x[i] != y[i] or x[i] == '?':
            distance += 1
    return distance


def overlap(x, y):
    return 1 if x != y or x == '?' else 0


class layer1_neuron:

    def __init__(self):
        self.expectation = Data[0][1:]
        self.dispersion = [1 for i in self.expectation]

    def radial_function(self, x):
        return np.exp(-0.5* reduce(lambda x, y: x+y, map(lambda i: (float(overlap(x[i],self.expectation[i]))/self.dispersion[i])**2, range(len(self.expectation)))))


class layer2_neuron:

    def __init__(self, number_of_inputs):
        self.weights = [1.0/number_of_inputs for i in range(number_of_inputs)]
        self.values = []

    def probability(self):
        ret = np.dot(np.array(self.weights), np.array(self.values))
        self.values = []
        return ret

    def add(self, value):
        self.values.append(value)


def create_network():
    # returns array, the first two elements are arrays of layer 1 neurons, responsible for edible and poisonous class respectively,
    # the last two elements are two layer 2 neurons with similar responsibilities
    l1_poisonous = [layer1_neuron() for i in range(poisonous_components)]
    l1_edible = [layer1_neuron() for i in range(edible_components)]
    return [l1_edible, l1_poisonous, layer2_neuron(edible_components), layer2_neuron(poisonous_components)]


def run_network(x):

    for neuron in network[0]:
        network[2].add(neuron.radial_function(x))
    for neuron in network[1]:
        network[3].add(neuron.radial_function(x))

    edible_probability = network[2].probability()
    poisonous_probability = network[3].probability()
    return 'e' if edible_probability > poisonous_probability else 'p'



Data = get_data()
P_edible, P_poisonous = prior_probability()
network = create_network()
for i in range(30):
    print run_network(Data[i])
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# N defines maximum number of nearest neighbours for evaluation
N = 15

def get_data():
    # this function reads and returns features and classes from file with data
    X_ret= []
    Y_ret= []
    f = open('wine.data.txt')
    line = f.readline()
    while line:
        X_ret.append(line.split(',')[1:-1])
        Y_ret.append(line.split(',')[0])
        line = f.readline()
    f.close()
    return X_ret, Y_ret


def accuracy_range(metric):
    # this function returns accuracy for each value of nearest neighbours from 2 to N in passed metrics
    accuracy = []
    for i in range(N+1)[2:]:
        model = KNeighborsClassifier(n_neighbors=i, metric = metric)
        model.fit(features, classes)
        predicted_classes = model.predict(features)
        accuracy.append(accuracy_score(classes, predicted_classes))
    return accuracy


features, classes = get_data()
euclidian_acc = accuracy_range('euclidean')
manhattan_acc = accuracy_range('manhattan')
chebyshev_acc = accuracy_range('chebyshev')


plt.plot(range(N+1)[2:], euclidian_acc, 'r', label='euclidian', linewidth = 2)
plt.plot(range(N+1)[2:], manhattan_acc, 'g', label='manhattan', linewidth = 2)
plt.plot(range(N+1)[2:], chebyshev_acc, 'b', label='chebyshev', linewidth = 2)
plt.legend()
plt.xlabel('Number of neighbours', fontsize = 18)
plt.ylabel('Accuracy', fontsize = 18)
plt.show()
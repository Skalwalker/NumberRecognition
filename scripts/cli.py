import argparse
from adapter import Adapter

DEFAULT_ALGORITHM = 'lda'
DEFAULT_K_VALUE = 3
DEFAULT_PROCESSING = 'None'
DEFAULT_TRAIN = True

def getAdapter():
    parser = argparse.ArgumentParser(description='A KNN and LDA approach for recognising handwriting numbers using the MNIST Dataset.')

    parser.add_argument('--algorithm', dest='algorithm', choices=['knn', 'lda', 'both'], type=str, default=DEFAULT_ALGORITHM, help='Select Learning Algorithm')

    parser.add_argument('-k', dest='k', type=int, default=DEFAULT_K_VALUE,help='K value for the KNN Algorithm')

    parser.add_argument('--train', dest='train', default=DEFAULT_TRAIN, type=bool, help='Enable or disable the training of the model')

    parser.add_argument('--proc', dest='proc', default=DEFAULT_PROCESSING, choices=['normalLines', 'None'], type=str, help='Type of image processing before training')

    args = parser.parse_args()

    adapter = Adapter(args.algorithm,
                      args.k,
                      args.train,
                      args.proc)

    return adapter

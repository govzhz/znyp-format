from PIL import Image
import os
import pickle
import numpy as np
import matplotlib.pyplot as plt

def load_dataset(file_root):
    """Load znyp Dataset

    input:
        file_root: the root location of "pickled" object (e.g., './')

	return:
		X: images (N, H, W, C)
		Y: labels (N, )
	"""
    train_filename = os.path.join(file_root, 'train_data')
    test_filename = os.path.join(file_root, 'test_data')
    x_train, y_train = _unpickle_dataset(train_filename, 'train')
    x_test, y_test = _unpickle_dataset(test_filename, 'test')

    return x_train, y_train, x_test, y_test


def _unpickle_dataset(filename, category):
    """ Unpickle Dataset

    input:
        filename: the save location of "pickled" object
        category: dataset category

	return:
		X: images (N, H, W, C)
		Y: labels (N, )
	"""
    with open(filename, 'rb') as f:
        datadict = pickle.load(f)
        X = datadict['data']
        Y = datadict['labels']
        H = datadict['height']
        W = datadict['width']
        C = datadict['channel']
        num_images = datadict['num_images']
        X = X.reshape(num_images, C, H, W).transpose(0, 2, 3, 1).astype("float32")
        Y = np.array(Y)
        print('X_%s: %s' % (category, X.shape))
        print('Y_%s: %s' % (category, Y.shape))
        return X, Y

def visualize_image(X_train, y_train):
    """Visual Dataset

    input:
        X_train: images (N, H, W, C)
        y_train: labels (N, )
    """
    W, H, C = X_train[0].shape
    plt.rcParams['figure.figsize'] = (10.0, 8.0)  # set default size of plots
    plt.rcParams['image.interpolation'] = 'nearest'
    plt.rcParams['image.cmap'] = 'gray'
    classes = ['A', 'B', 'C']   # a list of class name, you can control the number of output class here
    num_classes = len(classes)
    samples_per_class = 4
    for y, cls in enumerate(classes):
        # Get the subscript index of training samples whose label belong to the same class
        idxs = np.flatnonzero(y_train == y)
        # several images were randomly selected from the training samples whose label belong to the same class
        idxs = np.random.choice(idxs, samples_per_class, replace=False)
        # several images of each classification are displayed
        for i, idx in enumerate(idxs):
            plt_idx = i * num_classes + y + 1
            # create a subplot
            plt.subplot(samples_per_class, num_classes, plt_idx)
            # If it is gray-scale map, which is transformed from the three-dimensional to two-dimensional, otherwise unchanged
            if C == 1:
                X_show = X_train[idx].reshape((W, H))
            elif C == 3:
                X_show = X_train[idx]
            plt.imshow(X_show.astype('uint8'))
            plt.axis('off')
            # append title
            if i == 0:
                plt.title(cls)
    plt.show()


if __name__ == '__main__':
    # load dataset
    x_train, y_train, x_test, y_test = load_dataset(file_root='./znyp_dataset')
    # visual dataset
    visualize_image(x_train, y_train)
import tensorflow as tf
from tensorflow import keras


class gcn_layer(keras.layers.Layer):
    """
    GCN layer
    """

    def __init__(self, vector_size):
        super(gcn_layer, self).__init__()
        self.h1 = self.add_weight('h1', [vector_size, vector_size])

    def call(self, inputs, training=None):
        out = inputs[2] @ inputs[1]
        out = out @ inputs[2]
        out = out @ inputs[0]
        out = out @ self.h1
        return out


class dense_layer(keras.layers.Layer):
    """
    Linear layer
    """

    def __init__(self, input_dim, out_dim):
        super(dense_layer, self).__init__()
        self.h1 = self.add_weight('h1', [input_dim, out_dim])
        self.b1 = self.add_weight('b1', [out_dim])

    def call(self, inputs, training=None):
        out = inputs @ self.h1 + self.b1
        return out


class GCN(keras.Model):
    """
    GCN model
    """

    def __init__(self, out_size, vector_size):
        super(GCN, self).__init__()
        self.gcn = gcn_layer(vector_size=vector_size)
        self.fc1 = dense_layer(input_dim=vector_size, out_dim=64)
        self.fc2 = dense_layer(input_dim=64, out_dim=32)
        self.fc3 = dense_layer(input_dim=32, out_dim=out_size)

    def call(self, inputs, training=None):
        out = self.gcn(inputs)
        out = tf.reduce_mean(out, 1)
        out = self.fc1(out)
        out = self.fc2(out)
        out = self.fc3(out)
        return out

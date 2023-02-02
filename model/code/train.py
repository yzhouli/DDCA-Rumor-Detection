import tensorflow as tf
from tensorflow.keras import layers, optimizers, datasets, models
import numpy as np

from gcn import GCN


class dfca_train(object):
    """
    DFCA-GCN start
    """

    @staticmethod
    def list_max_index(data_li):
        """
        Gets the index of the maximum value of the list.
        :param data_li: the list.
        :return: the index of the maximum value.
        """
        max_value = max(data_li)
        for index, value in enumerate(data_li):
            if max_value == value:
                return index

    @staticmethod
    def process(att, rel, d, rumor_type):
        """
        Data type standardization.
        :param att: Characteristic matrix.
        :param rel: Relational matrix.
        :param d: Degree matrix of relation matrix.
        :param rumor_type: Real label.
        """
        att = tf.cast(att, tf.float32)
        rel = tf.cast(rel, tf.float32)
        d = tf.cast(d, tf.float32)
        rumor_type = tf.cast(rumor_type, tf.int32)
        return att, rel, d, rumor_type

    @staticmethod
    def train(source_path, batch_size, learning_rate, epochs):
        """
        DFCA-GCN model training
        :param source_path: source path of dataset.
        :param batch_size: batch size.
        :param learning_rate: learning rate.
        :param epochs: training time.
        """
        optimizer = optimizers.Adam(learning_rate)
        train_att_li = np.load(f'{source_path}/train_att.npy')
        train_rel_li = np.load(f'{source_path}/train_rel.npy')
        train_type_li = np.load(f'{source_path}/train_type.npy')
        train_d_li = np.load(f'{source_path}/train_d.npy')
        test_att_li = np.load(f'{source_path}/test_att.npy')
        test_rel_li = np.load(f'{source_path}/test_rel.npy')
        test_type_li = np.load(f'{source_path}/test_type.npy')
        test_d_li = np.load(f'{source_path}/test_d.npy')
        train_db = tf.data.Dataset.from_tensor_slices((train_att_li, train_rel_li, train_d_li, train_type_li))
        train_db = train_db.map(dfca_train.process).shuffle(100000).batch(batch_size)
        test_db = tf.data.Dataset.from_tensor_slices((test_att_li, test_rel_li, test_d_li, test_type_li))
        test_db = test_db.map(dfca_train.process).shuffle(100000).batch(batch_size)
        network = GCN(vector_size=100, out_size=2)
        print('train start')
        with tf.device('/gpu:0'):
            for epoch in range(epochs):
                loss_total = 0
                for step, (att, rel, d, rumor_type) in enumerate(train_db):
                    with tf.GradientTape() as tape:
                        out = network((att, rel, d))
                        loss = tf.losses.categorical_crossentropy(rumor_type, out, from_logits=True)
                        loss = tf.reduce_mean(loss)
                        loss_total += loss
                    grads = tape.gradient(loss, network.trainable_variables)
                    optimizer.apply_gradients(zip(grads, network.trainable_variables))
                print(f'epoch: {epoch}, loss: {loss_total}')
                total_sum, total_true = 0.0, 0.0
                for (att, rel, d, rumor_type) in test_db:
                    out = network((att, rel, d))
                    for index, out_type in enumerate(out):
                        predict_type = dfca_train.list_max_index(out_type)
                        real_type = dfca_train.list_max_index(rumor_type[index])
                        if predict_type == real_type:
                            total_true += 1
                        total_sum += 1
                print(f'epoch: {epoch}, accuracy: {total_true / total_sum}')


if __name__ == '__main__':
    source_path = '../dataset/dataset_time_4'
    dfca_train.train(source_path=source_path, batch_size=128, learning_rate=0.01, epochs=13)

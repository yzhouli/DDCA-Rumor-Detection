import numpy as np


class d_matrix(object):
    @staticmethod
    def matrix_du(matrix_2d):
        """
        Calculate the degree matrix of the relation matrix
        :param matrix_2d: Two-dimensional relation matrix
        :return: the degree matrix
        """
        result = np.zeros([len(matrix_2d), len(matrix_2d)], dtype=np.float32)
        for index, matrix_line in enumerate(matrix_2d):
            line_du = 0.0
            for value in matrix_line:
                if value != 0.0:
                    line_du += 1.0
            result[index][index] = line_du
        return result

    @staticmethod
    def du_sq(du_2d, sq_num):
        """
        Matrix root
        :param du_2d: Two-dimensional diagonal matrix
        :param sq_num: Value of square root
        :return: root Matrix
        """
        for i in range(len(du_2d)):
            du_2d[i][i] **= sq_num
        return du_2d

    @staticmethod
    def du_inverse(du_2d):
        """
        Find the inverse of the diagonal matrix
        :param du_2d: Two-dimensional diagonal matrix
        :return: inverse matrix
        """
        for i in range(len(du_2d)):
            du_2d[i][i] = 1 / du_2d[i][i]
        return du_2d

    @staticmethod
    def build_d_matrix(matrix_li):
        """
        Calculate the degree matrix of the element relation matrix
        :param matrix_li: list of relation matrix
        :return: list of degree matrix
        """
        result = np.zeros([len(matrix_li), len(matrix_li[0]), len(matrix_li[0])], dtype=np.float32)
        for index, matrix in enumerate(matrix_li):
            du_matrix = d_matrix.matrix_du(matrix_2d=matrix)
            sq_matrix = d_matrix.du_sq(du_2d=du_matrix, sq_num=0.5)
            inverse_matrix = d_matrix.du_inverse(du_2d=sq_matrix)
            result[index] = inverse_matrix
        return result

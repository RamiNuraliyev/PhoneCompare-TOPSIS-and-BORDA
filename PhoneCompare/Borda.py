import numpy as np
import time

class Borda:
    m = None  # Number of phones
    n = None  # Number of features
    w = None  # Weight matrix
    rank_matrix = []
    points_matrix = []

    def __init__(self, phone_matrix, j, w):
        self.phone_matrix = np.array(phone_matrix)
        self.m = len(phone_matrix)
        self.n = len(phone_matrix[0])
        self.pos_or_neg = j
        self.w = self.floater(w)

        # Weights normalize
        self.w = self.w / sum(self.w)

    # Return phone_matrix numpy array with float items
    def floater(self, phone_matrix):
        ax = []
        for i in phone_matrix:
            try:
                ix = []
                for j in i:
                    ix.append(float(j))
            except:
                ix = float(i)
                pass
            ax.append(ix)
        return np.array(ax)

    def borda_ranks(self):
        rank_matrix = self.floater(self.phone_matrix)

        for j in range(self.n):
            col_var = []
            col = []
            col_var = (self.phone_matrix[:, j])
            col = np.copy(self.phone_matrix[:, j])
            k = 0

            # If pos_or_neg[i] = 1 the best in column is positive(max)
            # else negative(min)

            while len(col_var) > 0:
                if self.pos_or_neg[j] == 1:
                    best_index = np.argmax(col_var)
                else:
                    best_index = np.argmin(col_var)
                best_var = col_var[best_index]
                num_of_best = len(col_var[col_var == best_var])
                for i in range(len(col)):

                    if col[i] == best_var:
                        if num_of_best > 1:
                            rank = 0.0
                            for l in range(num_of_best):
                                rank += float(k + l + 1)
                            rank_matrix[i][j] = float(rank / num_of_best)
                            if self.pos_or_neg[j] == 1:
                                col_var = np.delete(col_var, np.argmax(col_var))
                            else:
                                col_var = np.delete(col_var, np.argmin(col_var))

                        else:
                            col_var = np.delete(col_var, best_index)
                            rank_matrix[i][j] = k + 1
                            break
                k += num_of_best
        print("\n---------Step1-------\n", rank_matrix)
        self.rank_matrix = np.copy(rank_matrix)

    # Step2 -------------Borda points-------
    # If rank is #1 the points are max #m-1(m alternatives)
    def borda_points_and_result(self):

        self.points_matrix = np.copy(self.rank_matrix)
        self.points_matrix = self.m - self.points_matrix
        print("\n----------Step2 rank to points-------\n", self.points_matrix)
        self.points_matrix = self.points_matrix * self.w
        print("\n----------Step2 points with weights-------\n", self.points_matrix)

        result = np.zeros(self.m)
        for i in range(self.m):
            result[i] = sum(self.points_matrix[i, :])

        print("\n----------Step2 results-------\n", result)

        return np.argmax(result)

    def calc(self):
        start_time = time.time()
        self.borda_ranks()
        result = self.borda_points_and_result()
        print('\nChoice #', result, 'is the best for you!\n')
        print("---Borda Run time = %s seconds ------" % (time.time() - start_time))
        return result


# -------------Test-----------

# matrix = [7, 9, 9, 8], \
#          [8, 7, 8, 7], \
#          [9, 6, 8, 9], \
#          [6, 7, 8, 6]
#
# print("\n---------init-------\n", np.array(matrix))
#
# weight = [0.1, 0.4, 0.3, 0.2]
# j = [1, 1, 0, 0]
# # Each feature have the same weight
# weight = [1, 1, 1, 1]
# alg = Borda(matrix, j, weight)
# alg.calc()

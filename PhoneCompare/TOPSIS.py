import numpy as np
import time

class Topsis:

    phone_matrix = []  # Matrix
    w = []  # Weight matrix
    r = []  # Normalisation matrix
    m = None  # Number of phones
    n = None  # Number of features
    neg_ideal = []  # V` Negative ideal solution
    pos_ideal = []  # V* Positive ideal solution
    dis_from_neg_ideal = None  # S` Distance from negative ideal
    dis_from_pos_ideal = None  # S* Distance from positive ideal
    closeness = None  # C* Closeness to the ideal solution
    result = None

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

    def __init__(self, phone_matrix, w, j):
        self.phone_matrix = self.floater(phone_matrix)
        self.m = len(phone_matrix)
        self.n = len(phone_matrix[0])
        self.w = self.floater(w)
        print("\n---Init---\n", self.phone_matrix, "\n")

        # Weights normalize
        self.w = self.w / sum(self.w)

        # j[i] = 1 if positive feature 0 if negative
        self.j = np.array(j)

    # Step 1 ----------Normalize--------
    def step1(self):
        self.r = self.phone_matrix
        for j in range(self.n):
            feature_sum = sum(self.phone_matrix[:, j] ** 2) ** 0.5
            for i in range(self.n):
                self.r[i, j] = self.phone_matrix[i, j] / feature_sum
        print("\n------Step1-------\n", self.r)

    # Step 2 --------Multiply by weights------
    def step2(self):
        self.v = self.r * self.w
        print("\n------Step2-------\n", self.v)

    # Step 3 ---Determining positive and negative ideal solutions-------
    def step3(self):
        for i in range(self.n):
            if self.j[i] == 1:
                self.neg_ideal.append(min(self.v[:, i]))
                self.pos_ideal.append(max(self.v[:, i]))
            else:
                self.neg_ideal.append(max(self.v[:, i]))
                self.pos_ideal.append(min(self.v[:, i]))

        self.neg_ideal = np.array(self.neg_ideal)
        self.pos_ideal = np.array(self.pos_ideal)
        print("\n------Step3-------\n", "Neg ideal:", self.neg_ideal
              , "\nPos ideal:", self.pos_ideal, "\n")

    # Step 4 ----Measures the distance from the ideal features----
    def step4(self):
        self.dis_from_neg_ideal = (self.neg_ideal - self.v) ** 2
        self.dis_from_pos_ideal = (self.v - self.pos_ideal) ** 2

        print("\n------Step4-------\n", "Neg dis:", self.dis_from_neg_ideal,
              "\nPos dis:", self.dis_from_pos_ideal)

        self.neg_dis_sum = []
        self.pos_dis_sum = []
        for i in range(self.m):
            self.neg_dis_sum.append(sum(self.dis_from_neg_ideal[i, :]) ** 0.5)
            self.pos_dis_sum.append(sum(self.dis_from_pos_ideal[i, :]) ** 0.5)

        self.neg_dis_sum = np.array(self.neg_dis_sum)
        self.pos_dis_sum = np.array(self.pos_dis_sum)

        print("\n------Step4-------\n", "Neg dis_sum:", self.neg_dis_sum, "\n",
              "\nPos dis_sum:", self.pos_dis_sum, "\n")

    # Step 5 ------ Calculate the relative closeness to the ideal solution--
    def step5(self):
        # np.seterr(all='ignore') -----ignore float point error
        self.closeness = self.neg_dis_sum / (self.neg_dis_sum + self.pos_dis_sum)

        print("\n------Step5-------\n", "Closeness:", self.closeness, "\n")

        self.result = 0
        m = 0
        for i in range(self.m):
            print
            self.closeness[i]
            if self.closeness[i] > m or m == None:
                m = self.closeness[i]
                self.result = i
        print('Choice #', self.result + 2, 'is the best for you!\n')

    # TODO: ----------print phone name
    def calc(self):
        start_time = time.time()
        self.step1()
        self.step2()
        self.step3()
        self.step4()
        self.step5()
        print("---Topsis Run time = %s seconds ------" % (time.time() - start_time))

        return self.result + 1


# ------------Test-----------
# matrix = [7, 9, 9, 8], \
#          [8, 7, 8, 7], \
#          [9, 6, 8, 9], \
#          [6, 7, 8, 6]
#
# weight = [0.1, 0.4, 0.3, 0.2]
# j = [1, 1, 0, 0]
# alg = Topsis(matrix, weight, j)
# alg.calc()

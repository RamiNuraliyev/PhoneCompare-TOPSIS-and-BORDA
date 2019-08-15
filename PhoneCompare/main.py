import Borda
import TOPSIS
import xlsxwriter
import numpy as np
import xlrd

#TODO: Change location of xcel data file:

loc = "C:\\Users\\rami\\Desktop\\Phone Compare (1).xlsx"

class Phone:

    def __init__(self, name, brand, year, memory,
                 ram, cores, speed, screen,
                 front_cam, back_cam, weight, battery,
                 x_pixels, y_pixels, price, rate, brand_rate,
                 os_version, water_proof, number_of_colors,
                 expandable_memory, autofocus, fingerprint_sensor):
        self.name = name
        self.brand = brand
        self.year = year
        self.memory = memory
        self.ram = ram
        self.cores = cores
        self.speed = speed
        self.screen = screen
        self.front_cam = front_cam
        self.back_cam = back_cam
        self.weight = weight
        self.battery = battery
        self.x_pixels = x_pixels
        self.y_pixels = y_pixels
        self.price = price
        self.rate = rate
        self.brand_rate = brand_rate
        self.os_version = os_version
        self.water_proof = water_proof
        self.number_of_colors = number_of_colors
        self.expandable_memory = expandable_memory
        self.autofocus = autofocus
        self.fingerprint_sensor = fingerprint_sensor

    def print_phone(self):
        print("\n", self.name, self.brand
              , self.year
              , self.memory
              , self.ram
              , self.cores
              , self.speed
              , self.screen
              , self.front_cam
              , self.back_cam
              , self.weight
              , self.battery
              , self.x_pixels
              , self.y_pixels
              , self.price
              , self.rate
              , self.brand_rate
              , self.os_version
              , self.water_proof
              , self.number_of_colors
              , self.expandable_memory
              , self.autofocus, self.fingerprint_sensor, "\n")

    @classmethod
    # Constructor from string line with only spaces between arguments
    def from_string(cls, string):
        name, brand, year, memory, ram, cores, speed, screen, \
        front_cam, back_cam, weight, battery, x_pixels, y_pixels, price, \
        rate, brand_rate, os_version, water_proof, number_of_colors, \
        expandable_memory, autofocus, fingerprint_sensor = string.split(" ")

        return cls(name, brand, year, memory,
                   ram, cores, speed, screen, front_cam, back_cam,
                   weight, battery, x_pixels, y_pixels, price,
                   rate, brand_rate, os_version, water_proof,
                   number_of_colors, expandable_memory, autofocus, fingerprint_sensor)


# Read xcel file with data

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

# Save data in phones array
phones = []
for i in range(31):
    phone = Phone(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    j = 0
    phone.name = sheet.cell_value(i, j)
    j += 1
    phone.brand = sheet.cell_value(i, j)
    j += 1
    phone.year = sheet.cell_value(i, j)
    j += 1
    phone.memory = sheet.cell_value(i, j)
    j += 1
    phone.ram = sheet.cell_value(i, j)
    j += 1
    phone.cores = sheet.cell_value(i, j)
    j += 1
    phone.speed = sheet.cell_value(i, j)
    j += 1
    phone.screen = sheet.cell_value(i, j)
    j += 1
    phone.front_cam = sheet.cell_value(i, j)
    j += 1
    phone.back_cam = sheet.cell_value(i, j)
    j += 1
    phone.weight = sheet.cell_value(i, j)
    j += 1
    phone.battery = sheet.cell_value(i, j)
    j += 1
    phone.x_pixels = sheet.cell_value(i, j)
    j += 1
    phone.y_pixels = sheet.cell_value(i, j)
    j += 1
    phone.price = sheet.cell_value(i, j)
    j += 1
    phone.rate = sheet.cell_value(i, j)
    j += 1
    phone.brand_rate = sheet.cell_value(i, j)
    j += 1
    phone.os_version = sheet.cell_value(i, j)
    j += 1
    phone.water_proof = sheet.cell_value(i, j)
    j += 1
    phone.number_of_colors = sheet.cell_value(i, j)
    j += 1
    phone.expandable_memory = sheet.cell_value(i, j)
    j += 1
    phone.autofocus = sheet.cell_value(i, j)
    j += 1
    phone.fingerprint_sensor = sheet.cell_value(i, j)

    phones.append(phone)

# Create phones matrix with the relevant data
phones_matrix = np.zeros((31, 21))
phones = np.array(phones)

for i in range(30):
    i += 1
    j = 0
    phones_matrix[i][j] = phones[i].year
    j += 1
    phones_matrix[i][j] = phones[i].memory
    j += 1
    phones_matrix[i][j] = phones[i].ram
    j += 1
    phones_matrix[i][j] = phones[i].cores
    j += 1
    phones_matrix[i][j] = phones[i].speed
    j += 1
    phones_matrix[i][j] = phones[i].screen
    j += 1
    phones_matrix[i][j] = phones[i].front_cam
    j += 1
    phones_matrix[i][j] = phones[i].back_cam
    j += 1
    phones_matrix[i][j] = phones[i].weight
    j += 1
    phones_matrix[i][j] = phones[i].battery
    j += 1
    phones_matrix[i][j] = phones[i].x_pixels
    j += 1
    phones_matrix[i][j] = phones[i].y_pixels
    j += 1
    phones_matrix[i][j] = phones[i].price
    j += 1
    phones_matrix[i][j] = phones[i].rate
    j += 1
    phones_matrix[i][j] = phones[i].brand_rate
    j += 1
    phones_matrix[i][j] = phones[i].os_version
    j += 1
    phones_matrix[i][j] = phones[i].water_proof
    j += 1
    phones_matrix[i][j] = phones[i].number_of_colors
    j += 1
    phones_matrix[i][j] = phones[i].expandable_memory
    j += 1
    phones_matrix[i][j] = phones[i].autofocus
    j += 1
    phones_matrix[i][j] = phones[i].fingerprint_sensor

phones_matrix = np.array(phones_matrix)
phones_matrix = np.delete(phones_matrix, 0, axis=0)
print("Phone Matrix:\n", phones_matrix)


def matrix_to_xcel(path, matrix):
    workbook = xlsxwriter.Workbook(path)
    worksheet = workbook.add_worksheet()

    # Start from the first cell.
    # Rows and columns are zero indexed.
    # if matrix:
    if (np.size(matrix[0]) > 1):
        for row in range(len(matrix)):
            column = 0
            # iterating through content list
            for item in matrix[row]:
                # write operation perform
                worksheet.write(row, column, item)
                column += 1
    # else array
    else:
        row = 0
        for item in matrix:
            worksheet.write(row, 0, item)
            row += 1
    workbook.close()


# J[i] = 1 => max is ideal, else min is ideal
J = [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1]

# year	memory	ram	cores speed	screen	front_cam back_cam	weight	battery	Xpixels Ypixels	price
# rate_brand  rate	os_version	water_proof	num_of_colors	Expandable_Memory	Autofocus	Fingerprint
no_weights = [1] * 21
kids_weights = [9, 7, 8, 9, 10, 7, 6, 6, 0, 5, 9, 9, 0, 8, 9, 9, 5, 8, 6, 3, 3]
adults_weights = [2, 3, 4, 4, 5, 10, 5, 5, 7, 8, 7, 7, 6, 0, 0, 3, 5, 0, 2, 0, 4]
students_weights = [8, 8, 9, 9, 10, 7, 8, 10, 5, 10, 6, 6, 10, 9, 8, 8, 9, 4, 8, 5, 5]
borda_result = None
topsis_result = None

# Uncomment to see phones list
# for p in phones:
#     print( p.brand, " ", p.name, "\n")

# TODO:Uncomment under the test group you want:------------------------------------------

# --------------No weight---------------
#
# print("\n----------Borda-no_weight-------------\n")
# borda_alg = Borda.Borda(phones_matrix, J, no_weights)
# borda_result = borda_alg.calc()
# print("\n----------Topsis-no_weight--------------\n")
# topsis_alg = TOPSIS.Topsis(phones_matrix, no_weights, J)
# topsis_result = topsis_alg.calc()
# print("\n----------No weights results-------------\n")
# print("topsis_result = ", phones[topsis_result].brand, " ", phones[topsis_result].name, "\n")
# print("borda_result = ", phones[borda_result].brand, " ", phones[borda_result].name, "\n")


# -------------------kids weights----------------

# print("\n----------Borda-kids_weights-------------\n")
# borda_alg = Borda.Borda(phones_matrix, J, kids_weights)
# borda_result = borda_alg.calc()
# print("\n----------Topsis-kids_weights--------------\n")
# topsis_alg = TOPSIS.Topsis(phones_matrix, kids_weights, J)
# topsis_result = topsis_alg.calc()
# print("\n-------------kids_results-------------\n")
# print("Topsis_result = ", phones[topsis_result].brand, " ", phones[topsis_result].name, "\n")
# print("borda_result = ", phones[borda_result].brand, " ", phones[borda_result].name, "\n")


# -------------------adults weights----------------

# print("\n----------Borda-adults_weights-------------\n")
# borda_alg = Borda.Borda(phones_matrix, J, adults_weights)
# borda_result = borda_alg.calc()
# print("\n----------Topsis-adults_weights--------------\n")
# topsis_alg = TOPSIS.Topsis(phones_matrix, adults_weights, J)
# topsis_result = topsis_alg.calc()
# print("\n--------------adults_results-------------\n")
# print("Topsis_result = ", phones[topsis_result].brand, " ", phones[topsis_result].name, "\n")
# print("borda_result = ", phones[borda_result].brand, " ", phones[borda_result].name, "\n")

# -------------------students weights----------------

# print("\n----------Borda-students_weights-------------\n")
# borda_alg = Borda.Borda(phones_matrix, J, students_weights)
# borda_result = borda_alg.calc()
# # print("\n----------Topsis-students_weights--------------\n")
# topsis_alg = TOPSIS.Topsis(phones_matrix, students_weights, J)
# topsis_result = topsis_alg.calc()
# print("\n-------------students_results-------------\n")
# print("topsis_result = ", phones[topsis_result].brand, " ", phones[topsis_result].name, "\n")
# print("borda_result = ", phones[borda_result].brand, " ", phones[borda_result].name, "\n")


# write steps to excel file

# print("\n----------Borda-no_weight-------------\n")
# borda_alg = Borda.Borda(phones_matrix, J, no_weights)
# borda_alg.borda_ranks()
# matrix_to_xcel("C:\\Users\\rami\\Desktop\\borda1.xlsx", borda_alg.rank_matrix)
# borda_alg.borda_points_and_result()
# matrix_to_xcel("C:\\Users\\rami\\Desktop\\borda2.xlsx", borda_alg.points_matrix)

# print("\n----------Topsis-no_weight--------------\n")
# topsis_alg = TOPSIS.Topsis(phones_matrix, no_weights, J)
# topsis_alg.step1()
# matrix_to_xcel("C:\\Users\\rami\\Desktop\\topsis1.xlsx", topsis_alg.r)
# topsis_alg.step2()
# matrix_to_xcel("C:\\Users\\rami\\Desktop\\topsis2.xlsx", topsis_alg.v)
# topsis_alg.step3()
# matrix_to_xcel("C:\\Users\\rami\\Desktop\\topsis3pos.xlsx", np.array(topsis_alg.pos_ideal))
# matrix_to_xcel("C:\\Users\\rami\\Desktop\\topsis3neg.xlsx", np.array(topsis_alg.neg_ideal))
# topsis_alg.step4()
# matrix_to_xcel("C:\\Users\\rami\\Desktop\\topsis4neg.xlsx", topsis_alg.dis_from_neg_ideal)
# matrix_to_xcel("C:\\Users\\rami\\Desktop\\topsis4pos.xlsx", topsis_alg.dis_from_pos_ideal)
# matrix_to_xcel("C:\\Users\\rami\\Desktop\\topsis4negsum.xlsx", topsis_alg.neg_dis_sum)
# matrix_to_xcel("C:\\Users\\rami\\Desktop\\topsis4possum.xlsx", topsis_alg.pos_dis_sum)
# topsis_alg.step5()
# matrix_to_xcel("C:\\Users\\rami\\Desktop\\topsis5.xlsx", topsis_alg.closeness)

# print("\n----------Topsis-kids_weights--------------\n")
# topsis_alg = TOPSIS.Topsis(phones_matrix, kids_weights, J)
# topsis_alg.step1()
# matrix_to_xcel("C:\\Users\\rami\\Desktop\\topsiskids1.xlsx", topsis_alg.r)
# topsis_alg.step2()
# matrix_to_xcel("C:\\Users\\rami\\Desktop\\topsiskids2.xlsx", topsis_alg.v)
# topsis_alg.step3()
# matrix_to_xcel("C:\\Users\\rami\\Desktop\\topsiskids3pos.xlsx", topsis_alg.pos_ideal)
# matrix_to_xcel("C:\\Users\\rami\\Desktop\\topsiskids3neg.xlsx", topsis_alg.neg_ideal)
# topsis_alg.step4()
# matrix_to_xcel("C:\\Users\\rami\\Desktop\\topsiskids4neg.xlsx", topsis_alg.dis_from_neg_ideal)
# matrix_to_xcel("C:\\Users\\rami\\Desktop\\topsiskids4pos.xlsx", topsis_alg.dis_from_pos_ideal)
# matrix_to_xcel("C:\\Users\\rami\\Desktop\\topsiskids4negsum.xlsx", topsis_alg.neg_dis_sum)
# matrix_to_xcel("C:\\Users\\rami\\Desktop\\topsiskids4possum.xlsx", topsis_alg.pos_dis_sum)
# topsis_alg.step5()
# matrix_to_xcel("C:\\Users\\rami\\Desktop\\topsiskids5.xlsx", topsis_alg.closeness)

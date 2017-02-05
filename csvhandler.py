import csv
from options import Options

class CsvHandler:

    @classmethod
    def read_from_csv(cls, file_name):
        with open(file_name, "r") as file:
            lines = file.readlines()
        table = [element.replace("\t", ",").replace("\n", "").split(",") for element in lines]

        return table

    @staticmethod
    def string_lenght(element):
        return len(str(element))


    @classmethod
    def print_table(cls, table, headers):


        # width_of_columns = []
        #
        #
        # column_count = len(table[0])
        #
        #
        # for column in range(column_count):
        #     max_len_for_col = 0
        #
        #     for row in range(len(table)):
        #
        #         if max_len_for_col < len(str(table[row][column])):
        #             max_len_for_col = len(str(table[row][column]))
        #
        #     width_of_columns.append(max_len_for_col)
        #
        #
        # width_of_frame = (sum(width_of_columns) + 2*column_count) - 2
        #
        # print("/", end="")
        # print("="*width_of_frame, end="")
        # print("\\")

        for head in headers:
            print("{:^}".format(head))

        for row in range(len(table)):
            print("{}".format(table[row]))

        # #prints upper frame of table
        # print("╔", end="")
        # for index, head in enumerate(headers):
        #     for index, column_width in enumerate(width_of_columns):
        #         if index < len(headers) - 1:
        #             print("═" * (column_width + 2) + "╦", end="")
        #         else:
        #             print("═" * (column_width + 2), end="")
        #     print("╗")
        #
        # #prints headers
        # print("║", end="")
        # for head in headers:
        #     if len(head) == 1:
        #         print(" {:{width}} ║".format(head, width=width_of_columns))
        #     else:
        #         print(" {} {}".format(head, "║"), end="")
        #
        # for nested_list in table:
        #     print(nested_list)



# headers = ['Małopolska']
# a = CsvHandler.read_from_csv('malopolska.csv')
# b = Options.list_statistics(a)
# CsvHandler.print_table(b, headers)

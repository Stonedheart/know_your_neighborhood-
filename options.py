class Options:

    @classmethod
    def list_statistics(cls, table):

        statistics = {}

        for nested_list in table:

            if nested_list[5] == 'powiat':
                if nested_list[5] in statistics:
                    statistics[nested_list[5]] += 1
                else:
                    statistics[nested_list[5]] = 1

            elif nested_list[5] == 'gmina miejska':
                if nested_list[5] in statistics:
                    statistics[nested_list[5]] += 1
                else:
                    statistics[nested_list[5]] = 1

            elif nested_list[5] == 'gmina wiejska':
                if nested_list[5] in statistics:
                    statistics[nested_list[5]] += 1
                else:
                    statistics[nested_list[5]] = 1

            elif nested_list[5] == 'gmina miejsko-wiejska':
                if nested_list[5] in statistics:
                    statistics[nested_list[5]] += 1
                else:
                    statistics[nested_list[5]] = 1

            elif nested_list[5] == 'obszar wiejski':
                if nested_list[5] in statistics:
                    statistics[nested_list[5]] += 1
                else:
                    statistics[nested_list[5]] = 1

            elif nested_list[5] == 'miasto na prawach powiatu':
                if nested_list[5] in statistics:
                    statistics[nested_list[5]] += 1
                else:
                    statistics[nested_list[5]] = 1

            elif nested_list[5] == "miasto":
                if nested_list[5] in statistics:
                    statistics[nested_list[5]] += 1
                else:
                    statistics[nested_list[5]] = 1

            elif nested_list[5] == "delegatura":
                if nested_list[5] in statistics:
                    statistics[nested_list[5]] += 1
                else:
                    statistics[nested_list[5]] = 1

        statistics['powiat'] += statistics['miasto na prawach powiatu']

        statistics_to_print = []

        for key, value in statistics.items():
            statistics_to_print.append([key, value])

        return statistics_to_print


    @classmethod
    def three_cities_with_longest_name(cls, table):

        list_of_cities = []

        for index, nested_list in enumerate(table):
            if index > 2:
                if list_of_cities == [] or len(nested_list[4]) > len(max(list_of_cities, key=len)):
                    list_of_cities.append(nested_list[4])

        for element in sorted(list_of_cities, key=len):
            if len(list_of_cities) > 3:
                if len(element) < len(max(list_of_cities, key=len)):
                    list_of_cities.remove(element)

        return sorted(list_of_cities)


    @classmethod
    def county_with_largest_num_of_communities(cls, table):

        communities_num = {}

        for index, nested_list in enumerate(table):
            if index > 2:
                if nested_list[3] != '':
                    if nested_list[1] in communities_num:
                        communities_num[nested_list[1]] += 1
                    else:
                        communities_num[nested_list[1]] = 1


        county = max(communities_num, key=communities_num.get)

        for nested_list in table:
            if nested_list[2] == '':
                if nested_list[1] == county:
                    return "{} {}".format(nested_list[5], nested_list[4])


    @classmethod
    def locations_with_more_than_one_category(cls, table):

        locations = []

        for nested_list in table:
            if "-" in nested_list[5]:
                locations.append(nested_list[4])

        return sorted(locations)


    @classmethod
    def advanced_searching(cls, table, to_find):

        communities = []

        for nested_list in table:
            if to_find in nested_list[4]:
                communities.append([nested_list[4], nested_list[5]])

        return sorted(communities)
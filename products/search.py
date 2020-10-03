def searchingContent(tables):
    names_map = list()

    for table in tables:
        temp = list(table.objects.all())

        for item in temp:
            names_map.append([item.name, item.id])

    return names_map


def gettingTables():
    pass

import csv


def open_csv_at_given_line(csvPath, delimiter, firstLine):
    reader = csv.reader(open(csvPath + '.csv', mode='r'), delimiter=delimiter)
    for i in range(firstLine):
        reader.__next__()
    header = reader.__next__()
    return header, reader


class RawData:
    def __init__(self, csvPath, delimiter, firstLine,
                 xQualLabels, xQuantLabels, yLabels):
        self.xQuali = {k: [] for k in xQualLabels}
        self.xQuanti = {k: [] for k in xQuantLabels}
        self.y = {k: [] for k in yLabels}
        header, reader = open_csv_at_given_line(csvPath, delimiter, firstLine)
        for line in reader:
            for (labels, attribute) in [(xQuantLabels, self.xQuanti), (yLabels, self.y)]:
                for label in labels:
                    attribute[label].append(float(line[header.index(label)].replace(',', '.')))
            for label in xQualLabels:
                self.xQuali[label].append(line[header.index(label)])
        self.possibleValues = dict()
        self.digitalize()

    def digitalize(self):
        self.enumeratePossibleValues()
        for label in self.xQuali.keys():
            self.xQuali[label] = [self.possibleValues[label].index(value) for value in self.xQuali[label]]

    def enumeratePossibleValues(self):
        for label, column in self.xQuali.items():
            self.possibleValues[label] = []
            for value in column:
                if value not in self.possibleValues[label]:
                    self.possibleValues[label].append(value)

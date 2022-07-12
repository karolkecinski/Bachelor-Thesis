"""
    Data model class for easy data extraction
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import os

from main import DATAFOLDER 
UPDIR = '..'

class SubjectData():
    def __init__(self, uniparkFile, nazcaFile, epocxFile):
        self.load_unipark(uniparkFile)
        self.load_nazca(nazcaFile)
        self.load_epocx(epocxFile)

    def tag(self, raw_data):
        self.data       = raw_data
        self.ID         = raw_data[7]
        self.Gender     = raw_data[8]
        self.Age        = raw_data[9]
        self.Edulevel   = raw_data[10]

    def load_unipark(self, uniparkFilename):
        print('############## Unipark ##############')
        print("========> Loading unipark")
        raw_data = pd.read_excel(os.path.join(UPDIR, DATAFOLDER, uniparkFilename)).to_numpy()

        self.unipark_data   = raw_data[0]
        self.ID             = raw_data[0][7]
        self.Gender         = raw_data[0][8]
        self.Age            = raw_data[0][9]
        self.Edulevel       = raw_data[0][10]

        print("<======== Done.\n")

    def load_nazca(self, nazcaFilename):
        print('############## Nazca ##############')
        print("========> Loading nazca")
        raw_data = pd.read_csv(os.path.join(UPDIR, DATAFOLDER, nazcaFilename), delimiter=';').to_numpy()
        self.nazca_data = raw_data
        print("<======== Done.\n")

    def load_epocx(self, epocxFile):
        print('############## EPOCX ##############')
        print("========> Loading EPOCX")
        raw_data = pd.read_csv(os.path.join(UPDIR, DATAFOLDER, epocxFile), delimiter=',').to_numpy()
        print(raw_data)
        self.epocx_data = raw_data
        print("<======== Done.\n")

class ExportData():
    def __init__(self):
        pass

    @staticmethod
    def load_export(exportFilename : str) -> list:
        """
        Parameters
        ----------
        exportFilename : str
            Name of the file containing combined experiments data.

        Returns
        -------
        data : list
            List of SubjectData objects that represent experiments.
    
        """

        raw_data = pd.read_excel(os.path.join(UPDIR, DATAFOLDER, exportFilename)).to_numpy()
        print('############## Loaded ##############')
        data = []
        for entry in raw_data:
            subject_data = SubjectData()
            subject_data.tag(entry)
            data.append(subject_data)
        return data

if __name__ == "__main__":
    #SubjectData().load_unipark('s1-20220602\s1_unipark_2022.06.03T15.37.21.xlsx')
    #data = ExportData.load_export('export.xlsx')
    #print(data[1].ID)

    sd = SubjectData(
        's1-20220602\s1_unipark_2022.06.03T15.37.21.xlsx',
        's1-20220602\s1_nazca_2022.06.02.csv',
        's1-20220602\s1_EPOCX_160041_2022.06.02T15.37.21+02.00.md.csv'
    )

    print(sd.unipark_data)
    print("\n\n")
    print(sd.nazca_data)
    print("\n\n")
    print(sd.epocx_data[0])
    print("\n\n")
    print(sd)

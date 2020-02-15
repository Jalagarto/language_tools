#!/usr/bin/python3

import os
from translate import Translator
import pandas as pd
from os.path import join

print("This script creates a csv table with translations \nfrom a list of items (words or sentences) separated by commas\n")

# https://pypi.org/project/translate/
cwd = os.getcwd()
files = os.listdir(cwd)

print("Files found in the directory:")
print(files, "\n")

tr = Translator(to_lang="es")

try:
	for f in files:
		if f.endswith(".txt"):
			print("\nTranslating items from file: '{}'".format(f))
			data = [word.split(',') for word in open(f, 'r').readlines()]
			data = [word.replace("\n", "") for word in data[0]]
			trans = [tr.translate(w) for w in data]
			dicto = dict(zip(data,trans))
			#print("Items to be translated:")
			#print(dicto)
			df = pd.DataFrame(dicto.items(), columns = ['English','Spanish'])
			print("\n", df)
			print("\nThe translated file can be found here: ", join(cwd, f.rsplit(".",1)[0]+".csv"))
			df.to_csv(join(cwd, f.rsplit(".",1)[0]+".csv"), index=False)
			print("\n             ___________________________________________\n")
except Exception as error:
	print('Caught this error: ' + repr(error))
	print("\n...something went wrong... \nItems need to be in a txt file and to be separated by commas")





  


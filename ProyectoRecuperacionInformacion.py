import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer 
from collections import Counter
ps = PorterStemmer()
cont = 0
filename = "TodosLibros.txt"
file = open(filename,encoding="utf8")
text = file.readlines()
file.close()
longitud=len(text)
#print(longitud) #108747  longitud del TXT en lineas
Textoprocesado=[]
TODOOELLIBRO=[]
TODOOELLIBROVALORES = []
with open("ResultadosdeEjecuacucion.txt", "w") as Res, open("Diccionario.txt", "w") as Dic, open("Vectores.txt", "w") as Vec:
	for x in range(0,longitud):
		TituloLibro= []
		TextoDelLibro2 = []
		if ".I" in text[x] :
			lineastring = text[x]
			if lineastring[1] == "I":
				if lineastring[0] == ".":
					lineastring = lineastring.replace('I', '')
					lineastring = lineastring.replace('.', '')
					lineastring =lineastring.replace(' ', '')
					lineastring =lineastring.replace('\n', '')
					Res.write(lineastring + " | ")
	
		if ".T" in text[x] :
			lineastring = text[x]
			if lineastring[1] == "T":
				if lineastring[0] == ".":
					lineastring1 = text[x+1] 
					lineastring2 = text[x+2] 
					if ".A" not in lineastring1 and ".A" not in lineastring2:
						TituloLibro = " ".join([lineastring1.rstrip('\n'),lineastring2.rstrip('\n')])
						Res.write(TituloLibro+" | ")
					if ".A" not in lineastring1 and ".A" in lineastring2:
						TituloLibro = lineastring1.rstrip('\n')
						Res.write(TituloLibro+" | ")

		if text[x] == ".W"+"\n":
			TextoDelLibro = " "
			y = x+1
			words=[]
			while text[y] != ".X"+"\n":
				#print(text[y])
				words = text[y].split()
				#print(words)
				words= re.split(r'\W+', text[y])
				#print(words)
				words = [word.lower() for word in words]
				#print(words)
				nltk_stopwords = set(stopwords.words('english'))
				text_without_stopword = [word for word in words if not word in nltk_stopwords]
				#print(text_without_stopword)

				todoo=[]
				for x in range(len(text_without_stopword)):
					ww= text_without_stopword[x]
					todoo.append(ps.stem(ww))
				
				#print(todoo)
				
				all = " ".join(todoo)
				TextoDelLibro += all
			
			
				y+=1

			Res.write(TextoDelLibro)
			Res.write("\n")
			arrayTemp2 = []
			arrayTemp = TextoDelLibro.split() 
			a = dict(Counter(arrayTemp))
			valorespalabras =list(a.values())
			TODOOELLIBRO.append(arrayTemp)
			TODOOELLIBROVALORES.append(valorespalabras)

			for x in range(0,len(arrayTemp)):
				if arrayTemp[x] not in arrayTemp2 and "7" not in arrayTemp[x] and "1" not in arrayTemp[x] and "5" not in arrayTemp[x] and "2" not in arrayTemp[x] and "6" not in arrayTemp[x] and "3" not in arrayTemp[x] and "4" not in arrayTemp[x] and "9" not in arrayTemp[x] and "8" not in arrayTemp[x]:	

					arrayTemp2.append(arrayTemp[x])
 
			Texto = " ".join(arrayTemp2)
			Dic.write(Texto)
			Dic.write("\n")
			#for x in range(0,len(arrayTemp2)):
			#	print(arrayTemp2[x],end='')
			#	print("  ",end ='')
			#	print(valorespalabras[x])
		
#Fin del While	

print(TODOOELLIBROVALORES)
print(TODOOELLIBRO)
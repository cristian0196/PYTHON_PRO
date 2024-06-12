meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "una respuesta a una broma",
            "SHEESH": " ligera desaprobación",
            "AGGRO": "aterrador, siniestro"
            }
            
palabra = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if palabra in meme_dict.keys():
   print(meme_dict[palabra])
else:
    print("la palabra no se encuentra o no esta escrita con mayusculas")

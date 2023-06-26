import os

def recupfichieravectableaux():
    count = 0 
    folder_path = r"C:\Users\karla-ded\Documents\Aide_en_ligne_github\aide-en-ligne\docs"
    for path, dirs, files in os.walk(folder_path):
        for filename in files:
            if ".md" in filename:
                file = path.replace(os.sep, '/')+'/'+ filename
                i = 0 
                with open(file, 'r') as f1:
                    for ligne in f1:
                        if '|' in ligne:
                            i += 1
                if i > 5 : 
                    with open(r"C:\Users\karla-ded\Documents\ousontlestableaux.txt", 'a') as f2:
                        f2.write(file+'\n')
                        count += 1
    print(count)

recupfichieravectableaux()
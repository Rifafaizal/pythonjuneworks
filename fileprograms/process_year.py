f_read=open("C:\\Users\\ser\\Desktop\\PythonJuneWorks\\fileprograms\\years.txt","r")
f_century=open("C:\\Users\\ser\\Desktop\\PythonJuneWorks\\fileprograms\\century.txt","w")
f_noncentury=open("C:\\Users\\ser\\Desktop\\PythonJuneWorks\\fileprograms\\noncentury.txt","w")
for year in f_read:
    year=int(year.rstrip("\n"))
    if year%100==0:
        f_century.write(str(year)+"\n")
    else:
        f_noncentury.write(str(year)+"\n")

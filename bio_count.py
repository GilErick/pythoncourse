#Prueba de lectura de secuencias (Erick Ivan Gil Reyes)
#Trying


from Bio.Seq import Seq
my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")
print (len(my_seq))
print (my_seq.count("G"))
print (my_seq.count("C"))

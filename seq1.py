#Actividad para la impresión de secuencias (Erick Ivan Gil Reyes)
from Bio.Seq import Seq
my_seq = Seq("AGTACACTGGT")
print (my_seq)
print (my_seq.complement())
print (my_seq.reverse_complement())

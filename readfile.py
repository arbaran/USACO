fin = open("test_file_io", 'r') 
fout = open("mytestfile.out", 'w') 

lineone = fin.readline()
linetwo = fin.readline()

print(lineone)
print(linetwo)

fin.close()
fout.close()


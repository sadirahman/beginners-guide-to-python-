fw = open ('simple.txt','w')
fw.write('i love my country\n')
fw.write('i love my desh\n')
fw.close()

fr = open('simple.txt', 'r')
text = fr.read()
print(text)
fr.close()





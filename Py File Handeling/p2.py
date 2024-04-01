n1=input('Friend 1 :')
n2=input('Friend 2 :')
n3=input('Friend 3 :')

fi=open('p2.txt','w')
# fi.write(n1+'\n'+n2+'\n'+n3+'\n')

fi.write(n1+'\n')
fi.write(n2+'\n')
fi.write(n3+'\n')
fi.close()
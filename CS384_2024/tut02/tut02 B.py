x=input()
p="";
s=0;
for i in range (0,len(x)-1):
    if(x[i]==x[i+1]) :
      s=s+1;
    else :
      p+=x[i];
      p+=str(s+1);
      s=0;
p+=x[len(x)-1];
p+=str(s+1);

print(p);
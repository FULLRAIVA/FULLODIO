
from copy import deepcopy
class calculadora(object):

    def __init__(self,entrada):
        self._entrada = entrada
        self._lista = []
        self._result = 0
    @property
    def separa(self):
        lista2 = []
        cont=0
        while(cont<len(self._entrada)):
            lista2.append(self._entrada[cont])
            cont+=1
        self._lista = lista2
        
    @property
    def junta(self):
        
        lista2 = []
        lista3 = deepcopy(self._lista)
        string = ""
        cont = 0
        for i in range(len(lista3)):
            if((lista3[i]!="-") and (lista3[i]!="*") and (lista3[i]!="+") and (lista3[i]!="/")):
                string+=lista3[i]
                
                
                
            if((lista3[i]=="-") or (lista3[i]=="*") or (lista3[i]=="+") or (lista3[i]=="/")):
               if(len(string)>0):
                   lista2.append(string)
               lista2.append(lista3[i])
               string = ""
               cont=i

               
        string=""
        for i in range(cont+1,len(lista3)):
               string+=lista3[i]
               if(i==len(lista3)-1):
                   lista2.append(string)
               
           
        self._lista = lista2
        #print(self._lista)
        
    @property
    def converte(self):
       
       
        lista2 = []
        
        
        
        if self._lista[0] == "-":
           
               lista2.insert(0,float(self._lista[1])*(-1))
               self._lista.pop(0)
               self._lista.pop(0)
            
            
        
        for i in self._lista:
            if(i!="-" and i!="+" and i!="/" and i!="*"):
                lista2.append(float(i))
            if(i=="-" or i=="+" or i=="/" or i=="*"):
                lista2.append((i))
        
        self._lista = lista2
        
        #print(self._lista)
            
    @property
    def calcula(self):
        
        result = 0
        listaRes = []
        result2 = 0
        cont = False
        lista3 = deepcopy(self._lista)
        index = []
        index2 = []
        c = 0
        conf = False
        listaDM = ["@" for x in range(1000)]
        for x in range(10):
            lista3.append("@")
        if "/" in self._lista or "*" in self._lista:
            if "-" in self._lista or "+" in self._lista:
               
               for x in range(len(self._lista)+10):
                   if(lista3[x]=="*" or lista3[x]=="/"):
                            listaDM[c]= lista3[x-1]
                            c+=1   
                            listaDM[c]= lista3[x]
                            c+=1   
                            listaDM[c] = lista3[x+1]
                            c+=1
                            if(lista3[x+2]=="*" or lista3[x+2]=="/"):
                                listaDM[c-1] = "@"
                                
               for i in range(listaDM.count("@")):
                   listaDM.remove("@")
                   listaDM.append("@")
               for i in range(listaDM.count("@")*10):
                   listaDM.append("@")
               tam = 0
               #print("O DMC",listaDM)
               while(tam<len(listaDM)):
                   if((listaDM[tam]!="*" and listaDM[tam]!="/") and (listaDM[tam+1]!="*" and listaDM[tam+1]!="/")):
                       listaRes.append(result2)
                       result2 = 0
                       conf = False
                       tam+=1
                   if((listaDM[tam]=="*") and conf):
                        result2*=listaDM[tam+1]
                   if((listaDM[tam]=="/") and conf):
                        result2/=listaDM[tam+1]
                        
                   if((listaDM[tam]=="*") and not conf):
                       result2 = listaDM[tam-1]*listaDM[tam+1]
                       conf = True
                   if((listaDM[tam]=="/") and not conf):
                       result2 = listaDM[tam-1]/listaDM[tam+1]
                       conf = True
                    
                   if(listaDM[tam]=="@"):
                       break
                   tam+=1
               conf = False
               for x in range(1,len(lista3),2):
                     if(lista3[x]=="*" or lista3[x]=="/") and not conf:
                         index.append(x)
                         conf = True
                     if(lista3[x] =="+" or lista3[x]=="-"):
                         conf = False

               #print("Lista 3 3",lista3)
               for x in range(len(lista3)):
                     if(lista3[x]=="*" or lista3[x]=="/"):
                         lista3[x] = "@"
                         lista3[x-1] = "@"
                         lista3[x+1] = "@"
               for x in index:
                   if( (x not in index2) and (x+2 not in index2) ):
                       index2.append(x)
                    
               #print("Lista 3 2",lista3)
               #print("Lista res",listaRes)
               #print("Index2", index2)
               for x in range(len(index2)):
                 
                  
                  lista3[index2[x]] = listaRes[x]

               for x in range(lista3.count("@")):
                   lista3.remove("@")
               #print("Lista 3",lista3)
              
               for x in range(len(lista3)):
                    if(cont and lista3[x]=="+"):
                        result +=lista3[x+1]

                    if(cont and lista3[x]=="-"):
                        result -=lista3[x+1]

                    if(not cont and lista3[x]=="-"):
                        result = lista3[x-1]-lista3[x+1]
                        cont = True

                    if(not cont and lista3[x]=="+"):
                        result =lista3[x-1]+lista3[x+1]
                        cont = True
                      
            else:
                for x in range(len(lista3)):
                    if(cont and lista3[x]=="*"):
                        result *=lista3[x+1]

                    if(cont and lista3[x]=="/"):
                        result /=lista3[x+1]

                    if(not cont and lista3[x]=="/"):
                        result =lista3[x-1]/lista3[x+1]
                        cont = True

                    if(not cont and lista3[x]=="*"):
                        result =lista3[x-1]*lista3[x+1]
                        cont = True


                    #pensar em um modo de eliminar todas as divisoes e multiplicações amanha
                   
        else:
             
             for x in range(len(lista3)):
                    if(cont and lista3[x]=="+"):
                        result +=lista3[x+1]

                    if(cont and lista3[x]=="-"):
                        result -=lista3[x+1]

                    if(not cont and lista3[x]=="-"):
                        result = lista3[x-1]-lista3[x+1]
                        cont = True

                    if(not cont and lista3[x]=="+"):
                        result =lista3[x-1]+lista3[x+1]
                        cont = True
                
                
                
            
        #print("Lista ORIGINAL:",self._lista)
        dec = str(result)
        verifica = ""
        posic = 0
        for x in range(len(dec)):
            if(dec[x]=="."):
                posic = x
        
        for x in range(posic+1,len(dec)):
            verifica+=dec[x]
        if(int(verifica)==0):
            self._result = int(result)
        else:
            self._result = result
        #print("Lista DM:",listaDM)
        #print("Lista Resultados div:",listaRes)
    @property
    def getresult(self):
        return self._result
        
    @property
    def limpa(self):
        self._entrada = ""
        self._lista.clear()
        self._result = 0
                    
       
            


      
     
      



                
        




        
            
        
        
            
                
    # expressao de teste 30/2*3/5*3*2+10+2+1+4+3/2*2*3/2


"""calc = calculadora("30/2*3/5*3*2+10+2+1+4+3/2*2*3/2")
calc.separa
calc.junta
calc.converte
calc.calcula
print(calc.getresult)"""






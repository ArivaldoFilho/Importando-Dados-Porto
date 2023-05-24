print('Os portos organizados delegados aos estados e aos municípios totalizam 18, os portos organizados administrados por empresas controladas pela União totalizam 15 e, por fim, os portos organizados concedidos a entes privados são 2.')
while True:
    print('São eles:PE, SC, MA, PB, SP, PR, RS, RO, AP, RJ, AM, ES, BA, AL, RN, CE, PA. ')
    print('Para finalizar digite (FIM)')
    estado=input('Escolha um estado para saber a porcentagem de portos nele presente:\n ').upper()

# validaçãO do estado 
    if estado!= 'MA' and estado!='PE' and estado!='SP'and estado!='SC' and estado!='PB'and estado!='RJ'and estado!='PR'and estado!='RS'and estado!='RO'and estado!='AP'and estado!='AM'and estado!='ES'and estado!='BA'and estado!='AL'and estado!='RN'and estado!='CE'and estado!='PA' and estado!='FIM': 
     print('Estado invalido! Digite novamente')
     estado=input('MA PE SP SC PB PR RS RO RJ AP AM ES BA AL RN CE PA:\n ').upper()

# Operação para descobrir a porcentagem de cada estado

# Estados que possuem apenas um porto
    if(estado=='MA'):
        resultado= 100/35  
    elif(estado=='PB'):
        resultado= 100/35 
    elif(estado=='RO'):
        resultado= 100/35        
    elif(estado=='AP'):
        resultado= 100/35        
    elif(estado=='AM'):
        resultado= 100/35        
    elif(estado=='AL'):
        resultado= 100/35        
    elif(estado=='CE'):
        resultado= 100/35             
# Estados que possuem dois portos    
    elif(estado== 'PE'):
        resultado= 200/35
    elif(estado== 'SP'):
        resultado= 200/35
    elif(estado== 'PR'):
        resultado= 200/35
    elif(estado== 'ES'):
        resultado= 200/35
    elif(estado== 'RN'):
         resultado= 200/35     

# Estados que possuem três portos       
    elif(estado== 'RS'):
        resultado= 300/35 
    elif(estado== 'BA'):
        resultado= 300/35  
    elif(estado== 'PA'):
        resultado= 300/35      

# Estados que possuem quatro portos 
    elif(estado== 'SC'):
        resultado= 400/35

# Estados que possuem cinco portos      
    elif(estado=='RJ'):
        resultado=500/35   

    elif (estado=='FIM'):
            print('Operação finalizada.')
            print('O estado com a maior porcentagem de portos é o RJ com 14''%'' e os que tem menos são:\n MA,PB,RO,AP,AM,AL,CE todos com 2''%''. Obrigado pela participação!')
            break      
       
     

# Exibição do resultado
    print( 'O estado',estado,'tem ',(int(resultado)),'%'' da quantidade de portos no Brasil')
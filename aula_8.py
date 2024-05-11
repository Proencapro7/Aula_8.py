quant_disciplinas  =  float(input('Quantidade de disciplinas> 1 | 2 | 3 >>'))     

if quant_disciplinas == 3:
            nota1 =  float(input('Nota1'))
            nota2 =  float(input('Nota2')) 
            nota3 =  float(input('Nota3')) 
            nota4 =  float(input('Nota4')) 
            nota5 =  float(input('Nota5')) 
            nota6 =  float(input('Nota6')) 
            nota7 =  float(input('Nota4')) 
            nota8 =  float(input('Nota5')) 
            nota9 =  float(input('Nota6')) 
            
            media =  (nota1 + nota2 +nota3 +nota4+ nota5 + nota6+nota7 + nota8 +nota9)//9
            if media >= 7:
                print('Passou de ano', media)
            elif media == 6:
                print('Recuperação', media)
            else: 
                print('reprovado', media )
elif quant_disciplinas == 2:             
                nota1 =  float(input('Nota1'))
                nota2 =  float(input('Nota2')) 
                nota3 =  float(input('Nota3')) 
                nota4 =  float(input('Nota4')) 
                nota5 =  float(input('Nota5')) 
                nota6 =  float(input('Nota6'))
                media = (nota1 + nota2 +nota3 +nota4+ nota5 + nota6)//6
                if media >= 7:
                    print('Passou de ano', media)
                elif media == 6:
                    print('Recuperação', media)
                else: 
                    print('reprovado', media)
                    elif quant_disciplinas == 1:
    if quant_disciplinas >0: 
        nota1 =  float(input('Nota1'))
        nota2 =  float(input('Nota2')) 
        nota3 =  float(input('Nota3'))  
        media = (nota1 + nota2 +nota3)//3 
        if media >= 7:
            print('Passou de ano', media)
        elif media == 6:
            print('Recuperação', media)
        else: 
            print('reprovado', media )
else: 
        print('Digite um valor valido')
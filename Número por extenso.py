def extenso(n):
    print('O número '+str(n)+' po extenso é: ')   
    q=str(n)
    y=''
    if n<10000:
        q='0'+str(n)        
    if n<1000:
        q='00'+str(n)        
    if n<100:
        q='000'+str(n)           
    tup=tuple(z)   
    Lista1 = {
        '0':'',
        '2':'Vinte e',
        '3':'Trinta e',
        '4':'Quarenta e',
        '5':'Cinquenta e',
        '6':'Sessenta e',
        '7':'Setenta e',
        '8':'Oitenta e',
        '9':'Noventa e',
        }
   Lista2={
        '10':'Dez',
        '11':'Onze',
        '12':'Doze',
        '13':'Treze',
        '14':'Quatorze',
        '15':'Quinze',
        '16':'Dezesseis' ,       
        '17':'Dezessete',
        '18':'Dezoito',
        '19':'Desenove',
        }
    Lista3 = {
        '0':'',
        '1':' mil ,',
        '2':' dois mil ,',
        '3':' três mil ,',  
        '4':' quatro mil ,',
        '5':' cinco mil ,',
        '6':' seis mil ,',       
        '7':' sete mil ,',
        '8':' oito mil ,',
        '9':' nove mil ,',
        }
    Lista4 = {
        '0':'',
        '1':' um',
        '2':' dois',
        '3':' três',  
        '4':' quatro',
        '5':' cinco',
        '6':' seis',       
        '7':' sete',
        '8':' oito',
        '9':' nove',
        }
    Lista5 = {
        '0':'',
        '1':' um',
        '2':' dois',
        '3':' três',  
        '4':' quatro',
        '5':' cinco',
        '6':' seis',       
        '7':' sete',
        '8':' oito',
        '9':' nove',
        }
    Lista6= {
        '0':'',
        '1':'cento e ',
        '2':'duzentos e ',
        '3':'trezentos e ',  
        '4':'quatrocentos e ',
        '5':'quinhentos e ',
        '6':'seiscentos e ',       
        '7':'setecentos e ',
        '8':'oitocentos e ',
        '9':'novecentos e ',
        }
    Lista7= {
        '0':'',        
        '2':'vinte e',
        '3':'trinta e',  
        '4':'quarenta e',
        '5':'cinquenta e',
        '6':'sessenta e',       
        '7':'setenta e',
        '8':'oitenta e',
        '9':'noventa e',
        }
    Lista8= {
        '0':'',        
        '2':'vinte',
        '3':'trinta',  
        '4':'quarente',
        '5':'cinquenta',
        '6':'sessenta',       
        '7':'setenta',
        '8':'oitenta',
        '9':'noventa',
        }
    if tup[0]=='1':     
        y+=Lista2[tup[0]+tup[1]]
        y+=' mil,'
        y+=Lista6[tup[2]]
        y+=Lista7[tup[3]]        
        y+=Lista5[tup[4]]
        return y
    if x<1000:
        y+=Lista1[tup[0]]
        y+=Lista3[tup[1]]
        y+=Lista6[tup[2]]
        y+=Lista8[tup[3]]
        y+=Lista4[tup[4]]
        return y
    else:
        y+=Lista1[tup[0]]
        y+=Lista3[tup[1]]
        y+=Lista6[tup[2]]
        y+=Lista7[tup[3]]
        y+=Lista4[tup[4]]
        return y

from ordenacaotopologica import *

#ENGENHARIA DA COMPUTAÇÃO
engenhariadacomputacao = Grafo([],[])
verticesengenhariadacomputacao = ['11', '12', '13', '14','15','16','17',#primeiro periodo
           '21','22','23','24','25','26','27',                          #segundo periodo
           '31','32','33','34','35','36',                               #terceiro periodo
           '41','42','43','44','45',                                    #quarto periodo
           '51','52','53','54','55',                                    #quinto periodo
           '61','62','63','64','65',                                    #sexto periodo
           '71','72','73','74','75',                                    #setimo periodo
           '81','82','83','84','85',                                    #oitavo periodo
           '91','92','93','94','95',                                    #nono periodo
           '101','102','103']                                           #decimo periodo
arestasengenhariadacomputacao = ['11-21','14-24','15-24','14-25','15-25','16-26',#segundo periodo
             '21-31','24-33','14-34','15-34','14-35','15-35','26-36',            #terceiro periodo
            '21-41','24-43','24-44','36-44','36-45',                             #quarto periodo
            '31-51','31-52','24-53','24-54','36-55','44-55',                     #quinto periodo
            '51-61','43-62','34-63','35-63','31-64','55-65',                     #sexto periodo
            '55-65','24-72','63-73','52-75','64-75',                             #setimo periodo
            '34-81','35-81','54-81','73-82','74-83','61-84','64-84','75-85',     #oitavo periodo
            '83-92','44-93','45-93','61-94','75-94',                             #nono periodo
            '92-103']                                                            #decimo periodo
for i in verticesengenhariadacomputacao:
    engenhariadacomputacao.adiciona_vertice(i)
for i in arestasengenhariadacomputacao:
    engenhariadacomputacao.adiciona_aresta(i)
#print(engenhariadacomputacao.kahn())


#TELEMATICA
telematica = Grafo([],[])
vericestelematica = ['11', '12', '13', '14','15','16','17',#primeiro periodo
            '21','22','23','24','25','26','27',            #segundo periodo
            '31','32','33','34','35','36','37',            #terceiro periodo
            '41','42','43','44','45','46','47',            #quarto periodo
            '51','52','53','54','55','56',                 #quinto periodo
            '61','62','63','64','65']                      #sexto periodo
arestastelematica = ['11-21','12-22','16-22','12-23','16-23','13-24','16-26',                       #segundo periodo
                     '21-31','26-32','22-33','23-33','26-33','25-34','25-35','21-36','24-36', #terceiro periodo
                    '31-41','31-42','32-43','32-44','33-44','33-45','21-46','34-46',                #quarto periodo
                    '41-51','41-52','44-53','44-54','37-55','41-55','44-55',                        #quinto periodo
                    '42-51','53-62']                                                                #sexto periodo
for i in vericestelematica:
    telematica.adiciona_vertice(i)
for i in arestastelematica:
    telematica.adiciona_aresta(i)
#print(telematica.kahn())


#CONSTRUCAO DE EDIFICIOS
contrucaoedificios = Grafo([],[])
verticeconstrucaoedificios = ['11','12','13','14','15','16','17','18',  #primeiro periodo
                              '21','22','23','24','25','26','27',       #segundo periodo
                              '31','32','33','34','35','36','37','38',  #terceiro periodo
                              '41','42','43','44','45','46','47',       #quarto periodo
                              '51','52','53','54','55','56','57',       #quinto periodo
                              '61','62','63','64','65','66','67','68',  #sexto periodo
                              '71']                                     #setimo periodo
arestasconstrucaoedificios = ['15-21','14-23','11-24','17-24','15-25','17-26','17-27',                                  #segundo periodo
                              '15-32','21-32','21-33','15-34','23-35','26-36','23-37','24-38',                          #terceiro periodo
                              '17-41','21-41','17-42','21-42','11-43','23-43','35-43','35-45','17-46','32-46','21-47',  #quarto periodo
                              '37-51','45-51','46-52','17-53','32-53','47-54','17-55','32-55','46-56','43-57',          #quinto periodo
                              '31-62','57-62','37-64','45-64','22-66','31-67','57-67',                                  #sexto periodo
                              '13-71','22-71']                                                                          #setiomo periodo
for i in verticeconstrucaoedificios:
    contrucaoedificios.adiciona_vertice(i)
for i in arestasconstrucaoedificios:
    contrucaoedificios.adiciona_aresta(i)
#print(contrucaoedificios.kahn())


#MATEMATICA
matematica = Grafo([],[])
vericematematica = ['11','12','13','14','15','16','17',
                    '21','22','23','24','25','26','27',
                    '31','32','33','34','35','36',
                    '41','42','43','44','45','46',
                    '51','52','53','54','55','56','57',
                    '61','62','63','64','65','66','67',
                    '71','72','73','74','75','76','77',
                    '81','82','83','84','85','86','87']
arestamatematica = ['11-21','11-22','13-22','16-26',
                    '21-31','22-32','12-34',
                    '21-41','23-41','23-42','32-42','36-43','34-44','27-45',
                    '33-51','12-52','32-53','44-54','44-55',
                    '51-61','52-62','32-63','54-64','46-65',
                    '42-71','22-72','41-73','42-73','64-74','65-75',
                    '62-81','75-82','32-83','74-84',
                    '44-57','57-67','67-77','77-87']
for i in vericematematica:
    matematica.adiciona_vertice(i)
for i in arestamatematica:
    matematica.adiciona_aresta(i)
#print(matematica.kahn())


#FISICA
fisica = Grafo([],[])
verticefisica = ['11','12','13','14','15','16','17',
                 '21','22','23','24','25','26','27',
                 '31','32','33','34','35','36','37',
                 '41','42','43','44','45','46',
                 '51','52','53','54','55','56','57',
                 '61','62','63','64','65','66','68',
                 '71','72','73','74','75','76',
                 '81','82','83','84','85','86']
arestafisica = ['11-21','12-21','11-22','12-22','12-23','12-14','14-24','15-25',
                '21-31','23-31','21-32','22-32','23-33',
                '31-41','31-42','32-42','33-45','31-46',
                '41-51','45-51','41-52','42-52','45-53','31-54','43-55',
                '51-61','51-62','52-62','21-63','53-63','51-64','56-66',
                '61-71','41-72','45-72','66-73','31-74','43-74',
                '65-81','74-82','73-83','54-84','71-84','16-85','25-85',
                '21-57','43-57','31-68','57-68','41-76','68-76','51-83','76-83']
for i in verticefisica:
    fisica.adiciona_vertice(i)
for i in arestafisica:
    fisica.adiciona_aresta(i)
#print(fisica.kahn())


#LETRAS
letras = Grafo([],[])
verticesletras = ['11','12','13','14','15','16','17',
                 '21','22','23','24','25','26','27',
                 '31','32','33','34','35','36','37',
                 '41','42','43','44','45','46','47',
                 '51','52','53','54','55','56','57',
                 '61','62','63','64','65','66','67','68',
                 '71','72','73','74','75','76','77','78',
                 '81','82','83','84','85','86','87','88']
arestasletras = ['11-21','11-22','12-23','12-25','17-26',
                 '21-31','21-32','21-33','24-34','25-35',
                 '31-41','33-42','25-43','25-44','36-44','23-46','35-46','37-47',
                 '31-51','35-52','13-53','45-54','35-55','22-56','37-57',
                 '31-61','31-62','35-63','54-64','37-67','54-68',
                 '31-71','31-72','31-73','64-74','35-75','45-76','27-77','53-77','64-78','68-78',
                 '17-83','74-84','77-87','74-88','78-88']
for i in verticesletras:
    letras.adiciona_vertice(i)
for i in arestasletras:
    letras.adiciona_aresta(i)
#print(letras.kahn())


# print(engenhariadacomputacao.kahn())
# print(telematica.kahn())
# print(contrucaoedificios.kahn())
# print(matematica.kahn())
# print(fisica.kahn())
# print(letras.kahn())

print(engenhariadacomputacao.dfs())
print(telematica.dfs())
print(contrucaoedificios.dfs())
print(matematica.dfs())
print(fisica.dfs())
print(letras.dfs())
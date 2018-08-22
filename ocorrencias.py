################################################################################
######################Universidade Presbiteriana Mackenzie######################
################################################################################
###########################Erick Fernando Doria Lopes###########################
###############################TIA : 31664822###################################
################################################################################
################################################################################

###############################################################################
####################################Import#####################################
                import matplotlib.pyplot as plt                         #######
                from wordcloud import WordCloud, STOPWORDS              #######
###############################################################################
###############################################################################

############################################################
######################open a .txt file######################
############################################################

file = open('nomes.txt')

occourrence = {}
Key = []
Label= []
text = ''''''

###########################################################
#############the words that should be rejected#############
###########################################################

rejectWord = ['de','e','a','do','para','da','o','ao','é','que','quem','como','onde','com','um','na','em','das','uma','ser','no','nó','dos','as','se','os','ou','sua','suas','seu','seus','não','pelo','pelos','assim','será','cujo','cuja','cujos','cujas','seja','meio','essa','esta','esse','este','hoje','por','enfim','maior','noutra','deste','à','deve','através','vamos','todas','modo','poder','nos','sem','são','entre','pela','nas','tem','bem','vai','nada','menor','alto','foi','pode','mal','mau','bem','bom','ano','em','dada','vez','mesma','mesmo',
              'DE','E','A','DO','PARA','DA','O','AO','É','QUE','QUEM','COMO','ONDE','COM','UM','NA','EM','DAS','UMA','SER','NO','NÓ','DOS','AS','SE','OS','OU','SUA','SUAS','SEU','SEUS','NÂO','PELO','PELOS','ASSIM','SERÁ','CUJO','CUJA','CUJOS','CUJAS','SEJA','MEIO','ESSA','ESTA','ESSE','ESTE','HOJE','POR','ENFIM','MAIOR','NOUTRA','DESTE','À','DEVE','ATRAVÉS','VAMOS','TODAS','MODO','PODER','NOS','SEM','SÃO','ENTRE','PELA','NAS','TEM','BEM','VAI','NADA','MENOR','ALTO','FOI','PODE','MAL','MAU','BEM','BOM','ANO','EM','DADA','VEZ','MESMA','MESMO',
              ')','(','–','-','.',',',':','?','!','@','#','$','%','¨','&','*',';',',','/','|','¹','²','³','£','¢',
              '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']

##########################################################
######Read all the file and ignore the rejected ones######
##########################################################

for word in file.read().split():
    if not(word in rejectWord):
       if not(word in occourrence):
           c.update({word:1})
           text += " " + word
       else:
           occourrence[word] += 1
           text += " " + word

###########################################################
####################close the .txt file####################
###########################################################
           
file.close()

##########################################################
##########sort the word least commom most commom##########
##########################################################

for item in sorted(occourrence, key = occourrence.get):
    Key.append(occourrence[item])
    Label.append(item)

##########################################################
##############Use the 25th most commom words##############
##########################################################
    
Key = Key[len(Key)-25:len(Key)]
Label = Label[len(Label)-25:len(Label)]

##########################################################
######plot the first image where we see two graphics######
##########################################################

plt.figure(1, figsize=(10, 5))

plt.subplot(131)
plt.plot(Key, Label, 'ro', label='ocrorrencia de cada palavra')
plt.grid(True)

plt.subplot(133)
plt.bar(Key, Label, label='ocrorrencia de cada palavra')
plt.grid(True)

############################################################
#####create the graphics going from -2 to 27 in a scale#####
############################################################

plt.axis([-1,27,-1,27])

plt.title("Palavras mais comuns nas proposas de governo dos presidentes") #title

plt.show()

############################################################
#####create the word cloud with all words that appeared#####
############################################################

wordcloud = WordCloud(relative_scaling = 1,
                      stopwords = set(STOPWORDS)).generate(text)

##########################################################
###############plot the word cloud of words###############
##########################################################

plt.imshow(wordcloud)

plt.axis("off")

plt.show()

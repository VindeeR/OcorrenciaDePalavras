################################################################################
##################### Universidade Presbiteriana Mackenzie #####################
################################################################################
########################## Erick Fernando Doria Lopes ##########################
############################## TIA : 31664822 ##################################
################################################################################
################################################################################

###############################################################################
################################### Import ####################################
import matplotlib.pyplot as plt                                         #######
from wordcloud import WordCloud, STOPWORDS                              #######
from pdfminer.pdfparser import PDFParser                                #######
from pdfminer.pdfdocument import PDFDocument                            #######
from pdfminer.pdfpage import PDFPage                                    #######
from pdfminer.pdfpage import PDFTextExtractionNotAllowed                #######
from pdfminer.pdfinterp import PDFResourceManager                       #######
from pdfminer.pdfinterp import PDFPageInterpreter                       #######
from pdfminer.pdfdevice import PDFDevice                                #######
from pdfminer.layout import LAParams                                    #######
from pdfminer.converter import PDFPageAggregator                        #######
import pdfminer                                                         #######
###############################################################################
###############################################################################


############################################################
##################### Open a .pdf file #####################
############################################################
file = open('ALVARO DIAS.pdf', 'rb')
parser = PDFParser(file)
document = PDFDocument(parser)

if not document.is_extractable:
    raise PDFTextExtractionNotAllowed

# Create a PDF resource manager object that stores shared resources.
rsrcmgr = PDFResourceManager()

# Create a PDF device object.
device = PDFDevice(rsrcmgr)

# BEGIN LAYOUT ANALYSIS
# Set parameters for analysis.
laparams = LAParams()

# Create a PDF page aggregator object.
device = PDFPageAggregator(rsrcmgr, laparams=laparams)

# Create a PDF interpreter object.
interpreter = PDFPageInterpreter(rsrcmgr, device)

#############################################################
######################## Declaretion ########################
#############################################################

occurrency = {}
Key = []
Label= []
verify = 0
text = ''''''

def parse_obj(lt_objs, textX , verify_old):

    verify = verify_old
    text = textX

###########################################################
############ The words that should be rejected ############
###########################################################

    rejectWord = ['de','e','a','do','para','da','o','ao','é','que','quem','como','onde','com','um','na','em','das','uma','ser','no','nó','dos','as','se','os','ou','sua','suas','seu','seus','não','pelo','pelos','assim','será','cujo','cuja','cujos','cujas','seja','meio','essa','esta','esse','este','hoje','por','enfim','maior','noutra','deste','à','deve','através','vamos','todas','modo','poder','nos','sem','são','entre','pela','nas','tem','bem','vai','nada','menor','alto','foi','pode','mal','mau','bem','bom','ano','em','dada','vez','mesma','mesmo','aos','que','iremos','mais',
                  'DE','E','A','DO','PARA','DA','O','AO','É','QUE','QUEM','COMO','ONDE','COM','UM','NA','EM','DAS','UMA','SER','NO','NÓ','DOS','AS','SE','OS','OU','SUA','SUAS','SEU','SEUS','NÂO','PELO','PELOS','ASSIM','SERÁ','CUJO','CUJA','CUJOS','CUJAS','SEJA','MEIO','ESSA','ESTA','ESSE','ESTE','HOJE','POR','ENFIM','MAIOR','NOUTRA','DESTE','À','DEVE','ATRAVÉS','VAMOS','TODAS','MODO','PODER','NOS','SEM','SÃO','ENTRE','PELA','NAS','TEM','BEM','VAI','NADA','MENOR','ALTO','FOI','PODE','MAL','MAU','BEM','BOM','ANO','EM','DADA','VEZ','MESMA','MESMO','AOS','QUE','IREMOS','MAIS',
                  ')','(','–','-','.',',',':','?','!','@','#','$','%','¨','&','*',';',',','/','|','¹','²','³','£','¢',
                  '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
    
###########################################################
################ Loop over the object list ################
###########################################################

    for obj in lt_objs:
        
##########################################################
##### Read all the file and ignore the rejected ones #####
##########################################################
        
        if isinstance(obj, pdfminer.layout.LTTextBoxHorizontal):
            for word in obj.get_text().split():
                if not(word in rejectWord):
                    if not(word in occurrency):
                        occurrency.update({word:1})
                        text += " " + word
                    else:
                        occurrency[word] += 1
                        text += " " + word

        elif isinstance(obj, pdfminer.layout.LTFigure):
            parse_obj(obj._objs, text, verify)

############################################################
#### Create the word cloud with all words that appeared ####
############################################################

    if(verify == 15):
        wordcloud = WordCloud(relative_scaling = 1,
                                  stopwords = set(STOPWORDS)).generate(text)

##########################################################
############## Plot the word cloud of words ##############
##########################################################

        plt.imshow(wordcloud)

        plt.axis("off")

        plt.show()

###########################################################
################### Loop over all pages ###################
###########################################################

for page in PDFPage.create_pages(document):

##########################################################
########### Read the page into a layout object ###########
##########################################################
  
    interpreter.process_page(page)
    layout = device.get_result()

###########################################################
############## Extract text from this object ##############
###########################################################

    verify += 1
    parse_obj(layout._objs, text, verify)

############################################################
###### Sort the word least commom to the most commom #######
############################################################

for item in sorted(occurrency, key = occurrency.get):
    Key.append(occurrency[item])
    Label.append(item)

##########################################################
############# Use the 25th most commom words #############
##########################################################
    
Key = Key[len(Key)-25:len(Key)]
Label = Label[len(Label)-25:len(Label)]

##########################################################
##### Plot the first image where we see two graphics #####
##########################################################

plt.figure(1, figsize=(10, 5))

plt.subplot(131)
plt.plot(Key, Label, 'ro', label='ocrorrencia de cada palavra')
plt.grid(True)

plt.subplot(133)
plt.bar(Key, Label, label='ocrorrencia de cada palavra')
plt.grid(True)

############################################################
#### Create the graphics going from -2 to 27 in a scale ####
############################################################

plt.title("Palavras mais comuns nas proposas de governo dos presidentes") #title

plt.show()

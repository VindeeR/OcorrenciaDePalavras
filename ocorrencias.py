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
file = open('file.pdf', 'rb')
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

###########################################################
####################### Declaretion #######################
###########################################################

occurrency = {}
Key = []
Label= []
verify = 0

def parse_obj(lt_objs, verify_old):
    
    text = ''''''
    verify = verify_old

###########################################################
############ The words that should be rejected ############
###########################################################

    rejectWord = ['de','da','do','o','ao','é','e','a','para','que','quem','como','onde','com','um','na','em','das','uma','ser','no','nó','dos','as','se','os','ou','sua','suas','seu','seus','não','pelo','pelos','assim','será','cujo','cuja','cujos','cujas','seja','meio','essa','esta','esse','este','por','enfim','deste','à','deve','através','nos','sem','são','nas','tem','foi','vez','mesma','mesmo','novo','contra','completa','modo','sempre','todas','novas','programa','zero','cofres','➢','seja,','aos','nossa','menos','mais','pela','maior','que,','forma','anos','milhões','às','disso,','fim','bem','diz','mas','tocante','assim,','estão','ano','nosso','sendo','leitos','apenas','•','n','sobre','serão','longo','outros','nossos','dar','voltar','i.','ii.','iii.','partir','cada','pelas','instituições','lógica','ainda','uso','isso,','conjunto','formas','processos','parte','iv.','luta','preciso','grupos','papel','espaços','pode','todo','inclusive','têm','período','devem','movimento','necessidades','demais','estrutura','anos,','2016,','todos','entre','quando','foram','precisa','terá','2017.','maiores','novos','duas','mão','externa','mil','ter','está','bilhões','estar','caminho','termos','buscar','número','números','total','vai','visando','sejam','também','ainda,',
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
                #if word.lower() == 'saúde,' or word.lower() == 'campo,':
                    #word = word[0:len(word)-1].lower()
                if not(word.lower() in rejectWord):
                    if not(word in occurrency):
                        occurrency.update({word.lower():1})
                        text += " " + word.lower()
                    else:
                        occurrency[word] += 1
                        text += " " + word.lower()
            

        elif isinstance(obj, pdfminer.layout.LTFigure):
            parse_obj(obj._objs, verify)

############################################################
#### Create the word cloud with all words that appeared ####
############################################################

    if(verify == 15): #the number must be the number of the page to be analyzed
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
    parse_obj(layout._objs, verify)

############################################################
###### Sort the word least commom to the most commom #######
############################################################

for item in sorted(occurrency, key = occurrency.get):
    Key.append(occurrency[item])
    Label.append(item)

##########################################################
############# Use the 25th most commom words #############
##########################################################

Key = Key[len(Key)-30:len(Key)]
#print(Key)
Label = Label[len(Label)-30:len(Label)]
#print(Label)

##########################################################
##### Plot the first image where we see two graphics #####
##########################################################

plt.figure(1, figsize=(10, 5))

plt.plot(Key, Label, 'ro', label='ocrorrencia de cada palavra')
plt.grid(True)

plt.title("")

plt.show()

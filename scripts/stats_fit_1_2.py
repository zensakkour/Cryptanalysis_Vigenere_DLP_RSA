import os
import sys

src_dir = os.path.dirname( __file__ )
src_dir = os.path.join( src_dir, '..','src')
sys.path.append( src_dir )

import fichier 
import cipher 
import csv
import timeit
text_path="../text"
DATA_path="../DATA"
path_stats = DATA_path+"/Dict_ngramm/stats_EN/"

#A scrypt to creat a file of type .csv with the stats produced by applying the algorithm Hill Climbing
#twice with 2 ngrammes and varying the variables NBITERGLOB and NBITERSTATIC  

########################################################################################################
def clear():
     os.system('cls' if os.name == 'nt' else 'clear')
########################################################################################################

def creer_stats_fit(text,cle_depart,fileNAME):
    #(text : string )
    #(cle_depart : string )legth = 26
    #(fileNAME : string )

    
    clear()
    key=""
    global_BORN_inf=1000
    global_BORN_sup=1200
    static_BORN_inf=500
    static_BORN_sup=600
    fichier.print_progress_bar(0,global_BORN_sup, "stats fit")
    with open(fileNAME, 'w+') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        dictionaire2=cipher.ngram(2,path_stats)
        dictionaire4=cipher.ngram(4,path_stats)
        static=static_BORN_inf
        glob=global_BORN_inf
        while glob<=global_BORN_sup:
            static=static_BORN_inf
            while static<=static_BORN_sup and static < glob:
                moyennelettres=0
                moyennelettres2=0
                moyennescore=0
                moyennescore2=0
                nb_iter=5
                start = timeit.default_timer()
                for i in range (0,nb_iter) :
                    key=cipher.hillClimbing(cipher.fitness1,text,dictionaire2,glob,static,cle_depart,cipher.comp1) # 1er algo avec 1er dictionaire
                    moyennelettres+=cipher.compare_cle(cle_de_cryptage,key)
                    key=cipher.hillClimbing(cipher.fitness1,text,dictionaire4,glob,static,key,cipher.comp1) # 2er algo avec 2er dictionaire
                    moyennelettres2+=cipher.compare_cle(cle_de_cryptage,key)
                    moyennescore+=cipher.fitness1(cipher.decipher(text,key),dictionaire2)
                    moyennescore2+=cipher.fitness1(cipher.decipher(text,key),dictionaire4)
                stop = timeit.default_timer()
                filewriter.writerow([str(glob),str(static),str(moyennelettres/nb_iter)+"/26",str(moyennelettres2/nb_iter)+"/26",str('{:.3f}'.format(moyennescore/nb_iter)),str('{:.3f}'.format(moyennescore2/nb_iter)),str('{:.3f}'.format((stop - start)/nb_iter))])
                static+=250
            fichier.print_progress_bar(glob-global_BORN_inf, global_BORN_sup,"stats fit")
            glob+=500 
    clear()
    return key

########################################################################################################

cle_de_cryptage="QASZDEFRGTHYJUKILOMPWXCVBN"

text=fichier.NETTOYER_lire_fichier(text_path+"/EN/txtCLAIRE_1500_EN.txt")
text=cipher.encipher(text,cle_de_cryptage)
creer_stats_fit(text,cipher.alphabet,DATA_path+"/stats_ngramm/stats_GEN/fit.csv")


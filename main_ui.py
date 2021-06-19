# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 12:28:59 2020

@author: HEENA
"""
# import os 
# os.chdir(r'C:\UNIVERSITY MATERIALS\PROGRAMMING CONCEPTS AND PRACTICE\Assignment1-04-DEC-2020\Submission_prep')

try:
    #importing modules from the files
    import similarity_module
    from load_dataset_module import strip_accents
    from similarity_module import equilidian_distance_n
    from similarity_module import cosine_simillarity_n
    from similarity_module import correlation
    from similarity_module import compute_jaccard_index
    from similarity_module import manhattan_distance
    #user input
    q1=int(input('Press 0: ARTIST COMPARISON and 1 : MUSIC COMPARISON  : '))
    while q1!='':
        if q1==0:
            name1=input('Please enter the name of FIRST ARTIST: ')
            name2=input('Please enter the name of SECOND ARTIST: ')
            #stripping accents/Special characters
            name1=strip_accents(name1)
            name2=strip_accents(name2)
            #load dataset 
            from load_dataset_module import  artist_features_matrix
            #artist data
            art1=artist_features_matrix(name1)
            art2=artist_features_matrix(name2)
            #optional feature
       
            if name1.lower().strip()==name2.lower().strip() : 
                art3=art1
            
            #Optional code       
            else:
                art3=art1+art2
        
        #song details        
        elif q1==1:
            name1=input('Please enter the ID of FIRST SONG: ')
            name2=input('Please enter the ID of SECOND SONG: ')
            #load data for song
            from load_dataset_module import music_features_matrix
            art1=music_features_matrix(name1)
            art2=music_features_matrix(name2)
            art3=art1+art2

        #calculate distances
        distances={1:equilidian_distance_n(art1,art2),2:cosine_simillarity_n(art1, art2),3:correlation(art1, art2),4:manhattan_distance(art1,art2),5:compute_jaccard_index(art1, art2)}
        #dictionary of metrices
        names={1:'EQUILIDIAN DISTANCE',2:'COSINE SIMILARITY',3:'PEASRSON CORRELATION',4:'MANHATTAN DISTANCE',5:'JACCARD INDEX'}
        ans=[]
        print('', sep='\n')
        print('WHICH SIMILARITY MATRIX YOU WANT TO USE, PLEASE ENTER NUMBERS FOLLOWED BY SPACE IN CASE OF MULTIPLE')
        print('1: EQUILIDIAN DISTANCE','2: COSINE SIMILARITY','3: PEASRSON CORRELATION','4: MANHATTAN DISTANCE','5: JACCARD INDEX',sep='\n')
                
        numList = list(int(num) for num in input("PLEASE ENTER YOUR CHOICE BETWEEN 1 TO 5: ").strip().split())[:5]
        # print list for user
        print('', sep='\n')
        
        print('THE DISTANCE CALCULATIONS ARE SHOWN BELOW')
        for i in numList:
            while i<=5:
                #get all distances
                print(names.get(i),':',round(distances.get(i),3))
                break
            while i>5:
                #input choice error
                print('Please enter a valid choice')
                break
        #Quit loop/application    
        ans2=int(input('Do you want to quit application? PRESS 1:YES  0:NO :'))
        if ans2==1:
            print('Thankyou for your time, Have a wonderful day ahead')
            break
        else:
            continue
except ValueError :
    print('PLEASE ENTER VALUES SPECIFIED IN THE OPTIONS')
except IndexError  :
    print('THE ARTIST NAME OR MUSIC NAME DOES NOT EXIST IN THE DATABASE')   
except NameError:
    print('PLEASE ENTER VALUES SPECIFIED IN THE OPTIONS')
except TypeError:
    print('PLEASE ENTER VALUES SPECIFIED IN THE OPTIONS')
except FileNotFoundError:
    print('Please MAke sure that the dataset file is in same location as program files')
    
    


# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 12:20:53 2020

@author: HEENA
"""
#split and ignore symbol
def splitstring(l, splitchar, ignorechar): 
    result = []
    string = ""
    ignore = False
    for c in l:
        if c == ignorechar:
            ignore = True if ignore == False else False
        elif c == splitchar and not ignore:
            result.append(string)
            string = ""
        else:
            string += c
    return result  

#Data loading
def load_dataset_module():
    # import os
        
    # os.chdir(r'C:\UNIVERSITY MATERIALS\PROGRAMMING CONCEPTS AND PRACTICE\Assignment1-04-DEC-2020\Data')
    file=open('data.csv','r',encoding="UTF-8")
    list1=[]
    
    while True:
        text=file.readline()
        #using function to split data by ,
        text2=splitstring(text, ',', '"')
        list1.append(text2)
        if text=='' or text==['']:
            break
    #define empty list for data storage
    acousticness=[]
    artists=[]
    danceability=[]
    energy=[]
    id1=[]
    liveness=[]
    loudness=[]
    name=[]
    popularity=[]
    speechiness=[]
    tempo=[]
    valence=[]
    instrumentalness=[]
    for i in range(1,len(list1)-1): 
        #getting the data from parsed data
        acousticness.append(list1[i][list1[0].index('acousticness')])
        artists.append(list1[i][list1[0].index('artists')])
        danceability.append(list1[i][list1[0].index('danceability')])
        energy.append(list1[i][list1[0].index('energy')])
        id1.append(list1[i][list1[0].index('id')])
        liveness.append(list1[i][list1[0].index('liveness')])
        loudness.append(list1[i][list1[0].index('loudness')])
        name.append(list1[i][list1[0].index('name')])
        popularity.append(list1[i][list1[0].index('popularity')])
        speechiness.append(list1[i][list1[0].index('speechiness')])
        tempo.append(list1[i][list1[0].index('tempo')])
        valence.append(list1[i][list1[0].index('valence')])
        instrumentalness.append(list1[i][list1[0].index('instrumentalness')])
        
        
        
        
    #creating list wilth all numarical data with artist and song id
    list2=[acousticness,artists,danceability,energy,id1,liveness,loudness,name,popularity,speechiness,tempo,valence,instrumentalness]

    return list2    
     
    file.close()
    
#Dictionary creation for artist   
def artist_dictionaries():
    
    #accesing list 2 for data
    list2=load_dataset_module()
    #dictionary name
    artist_features={}
    #getting data from list 2 for making artist dictionary
    for i in range(len(list2[1])):
        artist_features[i]={'artist':list2[1][i].lower().replace('[','').replace(']','').replace("'",'').split(','),'acousticness':float(list2[0][i]),'danceability':float(list2[2][i])\
                            ,'energy':float(list2[3][i]),'id1':list2[4][i],'liveness':float(list2[5][i]),'loudness':float(list2[6][i])\
                                ,'popularity':float(list2[8][i]),'speechiness':float(list2[9][i]),'tempo':float(list2[10][i]),'valence':float(list2[11][i]),'instrumentalness':float(list2[12][i]) }
    #return dictionary
    return artist_features

#music feature dictionary
def music_dictionaries():
    
    #accesing relevant data from list2
    list2=load_dataset_module() 
    #music dictionary creation
    music_features={} 
    for i in range(len(list2[1])):
        
        
        music_features[i]={'id':list2[4][i].strip(),'acousticness':float(list2[0][i]),'danceability':float(list2[2][i])\
                            ,'energy':float(list2[3][i]),'id1':list2[4][i],'liveness':float(list2[5][i]),'loudness':float(list2[6][i])\
                                ,'popularity':float(list2[8][i]),'speechiness':float(list2[9][i]),'tempo':float(list2[10][i]),'valence':float(list2[11][i]),'instrumentalness':float(list2[12][i]) }
     #return music dictionary
    return music_features

import unicodedata
#stripping accent from data while reading
def strip_accents(text):

    try:
        text = unicode(text, 'utf-8')
    except NameError: # unicode is a default on python 3 
        pass

    text = unicodedata.normalize('NFD', text)\
           .encode('ascii', 'ignore')\
           .decode("utf-8")

    return str(text)



artist_features=artist_dictionaries()
music_features=music_dictionaries()
#accepting artist name and output relevant features
def artist_features_matrix(name):
    list_acousticness=[]
    for i in range(len(artist_features)):
        #Multiple artist in same cell to create matrix
        if  len(artist_features[i].get('artist'))>1:
            for j in range(len(artist_features[i].get('artist'))):
                #strip accents from data
                count=strip_accents(artist_features[i].get('artist')[j].strip()).count(name.lower())
                #in case of multiple artist
                if count>0:

                    acousticness=artist_features[i].get('acousticness')
                    danceability=artist_features[i].get('danceability')
                    energy=artist_features[i].get('energy')
                    liveness=artist_features[i].get('liveness')
                    loudness=artist_features[i].get('loudness')
                    popularity=artist_features[i].get('popularity')
                    speechiness=artist_features[i].get('speechiness')
                    tempo=artist_features[i].get('tempo')
                    valence=artist_features[i].get('valence')
                    instrumentalness=artist_features[i].get('instrumentalness')
                    list1=[acousticness,danceability,energy,liveness,loudness,popularity,speechiness,tempo,valence,instrumentalness]
                    list_acousticness.append(list1)
         #in case of single artist           
        elif  len(artist_features[i].get('artist'))==1:     
            count=artist_features[i].get('artist').count(name.lower())
                
            if count>0:              
                ##storing relevant data
                acousticness=artist_features[i].get('acousticness')
                danceability=artist_features[i].get('danceability')
                energy=artist_features[i].get('energy')
                liveness=artist_features[i].get('liveness')
                loudness=artist_features[i].get('loudness')
                popularity=artist_features[i].get('popularity')
                speechiness=artist_features[i].get('speechiness')
                tempo=artist_features[i].get('tempo')
                valence=artist_features[i].get('valence')
                instrumentalness=artist_features[i].get('instrumentalness')
                list1=[acousticness,danceability,energy,liveness,loudness,popularity,speechiness,tempo,valence,instrumentalness]
                list_acousticness.append(list1)
                
    #return list
    return list_acousticness
#values from music directory
def music_features_matrix(name):
    #list for storing data
    music_List=[]
    for i in range(len(music_features)):
        #storing relevant data
        if music_features[i].get('id')==name:   
            acousticness=artist_features[i].get('acousticness')
            danceability=artist_features[i].get('danceability')
            energy=artist_features[i].get('energy')
            liveness=artist_features[i].get('liveness')
            loudness=artist_features[i].get('loudness')
            popularity=artist_features[i].get('popularity')
            speechiness=artist_features[i].get('speechiness')
            tempo=artist_features[i].get('tempo')
            valence=artist_features[i].get('valence')
            instrumentalness=artist_features[i].get('instrumentalness')            
            list1=[acousticness,danceability,energy,liveness,loudness,popularity,speechiness,tempo,valence,instrumentalness]
            music_List.append(list1)
    #returning list
    return music_List
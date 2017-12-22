temp_song = input("enter the lyrics of the song ")
song = ''

#iterating over temp_song to get a list song of all words and no punctuation mark
for char in temp_song:
    if char.isalpha() or char == ' ':
        song += char
song = song.split(' ')

def frequency_dictionary(song):
    """
    creates dictionary to map {word:frequency}
    :param song: a list containing words of the song
    :return: a dictionary-frequency_map
    """
    dict={}

    for word in song :
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    return dict

def word_occur_tupple(dict):
    """
    creates a tuple
    :param dict: frequency_dictionary(song)
    :return: a tuple (list,int) for (word_list, freq)
    """
    tup=()
    #forms a list of dict_values (i.e.freq) with no repeated element. Next line sorts the list in descending order.
    freq_list=list(set(dict.values()))
    freq_list.sort(reverse = True)
    for frequency in freq_list:
        # l is a list of words with no. of occurrence = frequency from freq_list
        l=[]
        for word in dict:
            if dict[word] == frequency:
                l.append(word)
        tup = tup + ((l,frequency),)
    return tup


min_freq=int(input("the printed words should have a min frequency of: "))

for i in range( len( word_occur_tupple( frequency_dictionary(song) ) ) ):
    if word_occur_tupple(frequency_dictionary(song))[i][1] >= min_freq:
        print (word_occur_tupple(frequency_dictionary(song))[i])

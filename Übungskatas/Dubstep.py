def song_decoder(song):
    replaced = song.replace("WUB", " ")
    replaced_list = replaced.split()
    actual_sentence = " ".join(replaced_list)
    return(actual_sentence)

song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")
'''
Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.
Add an optional parameter to make_album() that allows you to store the
number of tracks on an album. If the calling line includes a value for the number of tracks, add that value to the album’s dictionary. Make at least one new
function call that includes the number of tracks on an album.
'''


def make_album(artist_name, album_title, number_tracks=''):
    if number_tracks:
        album = {'Artist Name': artist_name.title(), 'Album_Title': album_title.title(), 'Number of tracks': number_tracks.title()}
    else:
        album = {'Artist Name': artist_name.title(), 'Album_Title': album_title.title()}
    return album


while True:
    print("\nadd albums: ")
    art_name = input('Artist Name: ')
    if art_name == 'q':
        break
    Alb_title = input('Album Name: ')
    if Alb_title == 'q':
        break
    else:
        muscian_info = make_album(art_name, Alb_title)
    print(muscian_info)


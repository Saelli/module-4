# Eleonora
# 15 October
# Create a collection of these authors and
# the year they kicked the bucket;
# print the collection in the following format:

# Charles Dickens died in 1870.

# Charles Dickens, 1870
# William Thackeray, 1863
# Anthony Trollope, 1882
# Gerard Manley Hopkins, 1889

authors = {
    "Charles Dickens": "1870",
    "Wilaliam Thackeray": "1863",
    "Anthony Trollope": "1882",
    "Gerard Manley Hopkins": "1889" 
} # close parantaces
for author in authors:
    #print("The author:" + author + "died in" + authors(author))
    print ("%s" % author + " died in " + "%d." % int(authors[author]))
    #conver data into integer

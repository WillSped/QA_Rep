newfile = open("teams.txt", "r")

outfile = ""

for line in range (0, 5):
    outfile = (input("Please pick a sports team: ")) + "\n"
else:
    newfile.read()

for line in range (0, 5, 3):
    outfile = (input("Please pick a sports team: ")) + "\n"
else:
    newfile.read()

newfile = open("teams.txt, "w")
newfile.write(outfile)
file.close()
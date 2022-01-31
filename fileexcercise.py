file = open("teams.txt", "r")
outfile = ""
outfile = file.readline()
for line in range (0, 5, ):
    outfile += file.readline()

file=open("teams.txt", "w")
file.write(outfile)
file.close()

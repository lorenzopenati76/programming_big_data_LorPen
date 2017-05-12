
def read_file(changes_file):
    # use strip to strip out spaces and trim the line.
### below: ? is data then a list of lines?
    data = [line.strip() for line in open(changes_file, 'r')]
    return data

def get_commits(data):
    sep = 72*'-'
    commits = []
    current_commit = None
    comment_line = None
    index = 0
    while index < len(data):
        try:
            # parse each of the commits and put them into a list of commits
            details = data[index + 1].split('|')
            comment_line = data.index('', index +1) 
            # the author with spaces at end removed.
            commit = {'revision': details[0].strip(),
                'author': details[1].strip(),
                'date': details[2].strip().split(' ')[0],
                'time': details[2].strip().split(' ')[1],
                'day': details[2].strip().split(' ')[3][1:4],                
                'number_of_lines': details[3].strip().split(' ')[1]
            }
            # add details to the list of commits.
            commits.append(commit)
##???? below: data.index finds the line where sep is and add 1 to that number to create the new index?
            index = data.index(sep, index + 1)
        except IndexError:
            break
    return commits

if __name__ == '__main__':
    # open the file - and read all of the lines.
    changes_file = "Data.txt"
    data = read_file(changes_file)
    commits = get_commits(data)

       
    #write file code
    
    text_file = open("Output.csv", "w")
    i=0
    while i < len(commits):
        print (i+1)
        print(commits[i]['author'])
        print(commits[i]['date'])
        print(commits[i]['time'])
        print(commits[i]['day'])
        text_file.write("%s, %s, %s, %s, %s\n" % (str(i+1), commits[i]['author'],(commits[i]['date']),(commits[i]['time']),(commits[i]['day'])))
        i = i+1

    text_file.close() 
        
        
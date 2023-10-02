def print_scores_v1( scores ):
    '''
    The first solution finds the minimum and maximum scores, and then
    counts each score in this range, only outputting the scores with
    non-zero counts.  This is short and easy to write, but it only
    works well when the scores are not widely distributed.  For
    example, if there were only two scores, 0 and 1,000,000, this
    would be a very slow solution.
    '''

    '''  Preliminary output.  Not necessary for the solution. '''
    print ('Min score', min(scores))
    print ('Max score', max(scores))
    print ('Length', len(scores))

    ''' Generate and print a count for each score '''
    print ('\nVersion 1 output:')
    for score in range(min(scores), max(scores)+1 ):
        count = scores.count(score)
        if count > 0:
            print ("%3d: %2d" %(score,count))


def print_scores_v2( scores ):
    '''
    The second solution is based on sorting.  In doing so, all values
    that are the same are adjacent to each other in the sorted list,
    making them much easier to count.  We start by making a copy of
    the list in case the user wanted to work with the original list.
    '''
    scores_c = scores[::]
    scores_c.sort()
    count = 1
    print ('\nVersion 2 output:')
    for i in range(1,len(scores_c)):
        if scores_c[i-1] == scores_c[i]:  # seeing same score as the previous
            count += 1
        else:
            ''' The current score is not the same as the previous, so
                output the previous along with its count. '''
            print ("%3d: %2d" %(scores_c[i-1],count))
            count = 1

    # Print count for last item in the list
    print ("%3d: %2d" %(scores_c[-1],count))



if __name__ == "__main__":
    '''  Read in the scores, storing them in a list '''
    in_file = open('scores.txt')
    scores = []
    for line in in_file:
        scores.append( int(line) )

    print_scores_v1(scores)
    print_scores_v2(scores)
    
        

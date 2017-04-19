#List of Functions Used in vmo5_tipanalysis.py.

from collections import defaultdict

def ElitePatternof4(thisyear, nextyear, users):
    '''Returns elite pattern in following list: 
    (1) elite this year | non-elite next year E.N.
    (2) elite this year | elite next year E.E.
    (3) non-elite this year | elite next year N.E.
    (4) non-elite this year | non-elite next year N.N.
    thisyear: unicode or string of year1
    nextyear: unicode or string of year2
    users: user list from Yelp Dataset'''
    
    patternlist = [0, 0, 0, 0] #EN, EE, NE, NN
    for eachuser in range(len(users)):
        elite = users[eachuser][u'elite']
        if elite[0] != u'None':
            if (thisyear in elite) and (nextyear not in elite):
                patternlist[0]+=1
            elif (thisyear in elite) and (nextyear in elite):
                patternlist[1]+=1
            elif (thisyear not in elite) and (nextyear in elite):
                patternlist[2]+=1
            else:
                patternlist[3]+=1 
    return patternlist

def UserPatternList(thisyear, nextyear, users):
    '''Returns lists of elite/non-elite user IDs in following order
    for a particular year: 
    (1) elite this year | non-elite next year E.N.
    (2) elite this year | elite next year E.E.
    (3) non-elite this year | elite next year N.E.
    (4) non-elite this year | non-elite next year N.N.
    thisyear: unicode or string of year1
    nextyear: unicode or string of year2
    users: user list from Yelp Dataset'''
    
    patternlist = [[], [], [], []] #EN, EE, NE, NN
    for eachuser in range(len(users)):
        elite = users[eachuser][u'elite']
        if elite[0] != u'None':
            if (thisyear in elite) and (nextyear not in elite):
                patternlist[0].append(users[eachuser][u'user_id'])
            elif (thisyear in elite) and (nextyear in elite):
                patternlist[1].append(users[eachuser][u'user_id'])
            elif (thisyear not in elite) and (nextyear in elite):
                patternlist[2].append(users[eachuser][u'user_id'])
            elif (thisyear not in elite) and (nextyear not in elite):
                patternlist[3].append(users[eachuser][u'user_id'])
    return patternlist

def groupTipsbyYear(tip):
    tyears = []
    selectyears = [u'2004', u'2005', u'2006', u'2007', u'2008', u'2009', u'2010', 
                   u'2011', u'2012', u'2013', u'2014', u'2015', u'2016', u'2017']
    for x in selectyears:
        xyear=[]
        for t in range(len(tip)):
            yeargiven = tip[t][u'date'][0:4]
            if x == yeargiven:
                xyear.append(tip[t][u'user_id'])
        tyears.append(xyear)
    return tyears

def getTipElites(tipyears, usergroup):
    '''Matching function between tips of a year and user ID list.
    Returns a list of tips coming from that group of users.'''
    grouptipcounts=[]
    tipyears=sorted(tipyears)
    usergroup=sorted(usergroup)
    for tips in tipyears:
        if tips in usergroup:
            grouptipcounts.append(tips)
    return grouptipcounts

def getAllUniqueCounts(tipelites_list):
    '''Returns dictionary of tip counts for how many unique tips a user gave.
    Dictionary in form results[year][user_ID].
    tipelites_list: list of matched tips for all years.'''
    results = defaultdict(dict)
    selectyears = [u'2009', u'2010', u'2011', u'2012', u'2013', u'2014', u'2015', u'2016', u'2017']
    for x in range(len(tipelites_list)):
        for ID in tipelites_list[x]:
            year = selectyears[x]
            if ID in results[year].keys():
                results[year][ID] +=1
            else:
                results[year][ID] = 1
    return results

def getParticularCount(dictionaryx, value):
    ''' Returns list of counts of users who gave VALUE number of tips.
    dictionaryx: of the form results[year][ID], created by getAllUniqueCounts().
    value: the number of tips given per year that you are interested in.'''
    tipcounts=[]
    selectyears = [u'2009', u'2010', u'2011', u'2012', u'2013', u'2014', u'2015', u'2016'] #u'2017
    for a in selectyears:
        count = 0
        for k in dictionaryx[a].keys():
            if dictionaryx[a][k] == value:
                count+=1
        tipcounts.append(count)
    return tipcounts

def getParticularPercentCount(dictionaryx, value):
    '''Returns list of percentages of users who gave VALUE number of tips.
    dictionaryx: of the form results[year][ID], created by getAllUniqueCounts().
    value: the number of tips given per year that you are interested in.'''
    percentcounts=[]
    selectyears = [u'2009', u'2010', u'2011', u'2012', u'2013', u'2014', u'2015', u'2016'] #u'2017
    for a in selectyears:
        count = 0
        length = len(dictionaryx[a].keys())
        for k in dictionaryx[a].keys():
            if dictionaryx[a][k] == value:
                count+=1
        percentcounts.append(round(count/float(length), 4))
    return percentcounts


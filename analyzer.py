import json
import os



with open("weeklyresults.json") as f:
    data = json.load(f)


    #teams_array = ['trevor']
    teams_array = ['trevor','tony','alex','tyler','dustin','dan','brian','jonny','ryan','kristen','rebecca','nick']


    for i in teams_array:
        
        win=0
        loss=0
        tie=0
        for week in data['scores']:
            team_score = 0
            for scores in data['scores'][week]:
                if i == scores.get("name"):
                    team_score = scores.get("score")
                    
        
            for scores in data['scores'][week]:
                if i != scores.get('name'):
                    if team_score > scores.get("score"):
                        win+=1
                    elif team_score == scores.get("score"):
                        tie+=1
                    else:
                        loss+=1

        print ("Team:%s || %s-%s-%s") % (i, win,tie,loss)

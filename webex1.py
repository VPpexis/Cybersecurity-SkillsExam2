from  webexteamssdk  importWebexTeamsAPI  api  = WebexTeamsAPI( access_token='M2JhMjdhZDAtNTM4Ny00OWUwLTgzYTMtMDgxMTk2YWM2Y2Y0MzEwMWIxZTQtMWZ l_PF84_8f055694-f72f-491c-943c-ff49c31d85fe') 

#getting a team's information 
teams = api.teams.list() 

for team in teams:     
    print(team)  
    if getattr(team, 'name') != 'Postman Pat':         
        create_team = api.teams.create('Postman Pat')         
        teamId = getattr(create_team, 'id')     
    else: teamId = team.id 
import http.client
import time
import json


def create_goals_table(data):
    data_table = "NAME,NATIONALITY,TEAM,APPEARENCES,GOALS\n"

    for i in range(0,len(data['response'])):
        data_table = data_table+data['response'][i]['player']['name']+","+data['response'][i]['player']['nationality']+","+data['response'][i]['statistics'][0]['team']['name']+","+str(data['response'][i]['statistics'][0]['games']['appearences'])+","+str(data['response'][i]['statistics'][0]['goals']['total'])
        data_table = data_table+"\n"


    goals_table = open("goals_table.csv", "w")
    goals_table.write(data_table)


def create_assists_table(data):
    data_table = "NAME,NATIONALITY,TEAM,APPEARENCES,ASSISTS\n"

    for i in range(0,len(data['response'])):
        data_table = data_table+data['response'][i]['player']['name']+","+data['response'][i]['player']['nationality']+","+data['response'][i]['statistics'][0]['team']['name']+","+str(data['response'][i]['statistics'][0]['games']['appearences'])+","+str(data['response'][i]['statistics'][0]['goals']['assists'])
        data_table = data_table+"\n"


    assists_table = open("assists_table.csv", "w")
    assists_table.write(data_table)


conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")


headers = {
    'x-rapidapi-key': "56df8881a7msh727e042787c9a19p1d659fjsnff012d9fc00d",
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com"
}


menu1 = '''
______________________
    Digite o número da liga a ser consultada:
    1 - UEFA Champions League
    2 - Premier League (ING)
    3 - La Liga (ESP)
    4 - Bundesliga (ALE)
    5 - Serie A (ITA)
    6 - Ligue 1 (FRA)
    7 - Liga Portugal (POR)
    8 - Eredivise (HOL)
    9 - Copa Libertadores
    10 - Brasileirão (BRA)
    11 - Primera División (ARG)

'''

menu2 = '''
______________________
    Digite o número de início da temporada (de 2010 em diante):

'''

while True:

    valid_option = False
    league = int(input(menu1))

    if league == 1:
        id = 2
        valid_option = True

    elif league == 2:
        id = 39
        valid_option = True

    elif league == 3:
        id = 140
        valid_option = True

    elif league == 4:
        id = 78
        valid_option = True

    elif league == 5:
        id = 135
        valid_option = True

    elif league == 6:
        id = 61
        valid_option = True

    elif league == 7:
        id = 94
        valid_option = True

    elif league == 8:
        id = 88
        valid_option = True

    elif league == 9:
        id = 13
        valid_option = True

    elif league == 10:
        id = 71
        valid_option = True

    elif league == 11:
        id = 128
        valid_option = True

    else:
        print("Erro: Selecione uma das opções fornecidas.")

    if valid_option == True:
        
        while True:

            valid_option2 = True
            season = int(input(menu2))

            if season != 2010 and season != 2011 and season != 2012 and season != 2013 and season != 2014 and season != 2015 and season != 2016 and season != 2017 and season != 2018 and season != 2019 and season != 2020 and season != 2021 and season != 2022 and season != 2023:
                print("Erro: Digite um ano de 2010 a 2023.")
                valid_option2 = False

            if valid_option2 == True:
                conn.request("GET", f"/v3/players/topscorers?league={id}&season={season}", headers=headers)

                scorers_res = conn.getresponse()
                scorers_data = scorers_res.read()

                scorers_data_json = scorers_data.decode("utf-8")
                goals_data = json.loads(scorers_data_json)
                create_goals_table(goals_data)

                time.sleep(1)

                conn.request("GET", f"/v3/players/topassists?league={id}&season={season}", headers=headers)

                assists_res = conn.getresponse()
                assists_data = assists_res.read()

                assists_data_json = assists_data.decode("utf-8")
                assists_data = json.loads(assists_data_json)
                create_assists_table(assists_data)

                print("Tabelas criadas com sucesso!") 

            break

    break

    

        


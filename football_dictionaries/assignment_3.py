def players_by_country_and_position(squads_list):
    final_answer_dict = {}
    for user in squads_list:
        country = user[6]
        final_answer_dict.setdefault(country, {})
        position = user[1]
        final_answer_dict[country].setdefault(position, [])
        user_dict = {
            'number': user[0],
            'position': user[1],
            'name': user[2],
            'date_of_birth': user[3],
            'caps': user[4],
            'club': user[5],
            'country': user[6],
            'club_country': user[7],
            'year': user[8]
        }
        final_answer_dict[country][position].append(user_dict)
    return final_answer_dict
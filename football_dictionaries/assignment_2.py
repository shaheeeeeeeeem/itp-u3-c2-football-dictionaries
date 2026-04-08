def players_by_position(squads_list):
    final_dict_answer = {}
    for user in squads_list:
        position = user[1]
        final_dict_answer.setdefault(position, [])
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
        final_dict_answer[position].append(user_dict)
    return final_dict_answer

def substitute(player_in, player_out, players_off_field: list, players_on_field: list, no_of_substituted_players, max_substitutions):
    if no_of_substituted_players < max_substitutions:
        if player_out in players_on_field and player_in in players_off_field:
            players_off_field.remove(player_in)
            players_on_field.remove(player_out)
            players_on_field.append(player_in)
            players_off_field.append(player_out)
            no_of_substituted_players += 1
            print(f'A intrat {player_in} si a iesit {player_out}')
            print(f'Mai ai {max_substitutions - no_of_substituted_players} schimbari')
        else:
            print('Nu se poate efectua schimbarea')
    else:
        print('Nu mai ai schimbari disponibile')

    return players_on_field, players_off_field, no_of_substituted_players

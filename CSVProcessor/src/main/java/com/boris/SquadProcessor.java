package com.boris;

import com.boris.model.Club;
import com.boris.model.Country;
import com.boris.model.Player;
import com.boris.model.Team;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class SquadProcessor {

    public static final int PLAYER_JERSEY_NUMBER = 3;
    public static final int PLAYER_POSITION = 4;
    public static final int PLAYER_NAME = 5;
    public static final int CLUB_NAME = 6;
    public static final int CLUB_COUNTRY = 7;

    @Autowired
    private CountryRepository countryRepository;

    @Autowired
    private TeamRepository teamRepository;

    @Autowired
    private ClubRepository clubRepository;

    @Autowired
    private PlayerRepository playerRepository;

    public String parseLine(String line) {

        if(!line.startsWith("#")){ //skipp commented lines
            String[] splitLine = line.split(",");

            String jerseyNumber = splitLine[PLAYER_JERSEY_NUMBER];
            String playerPosition = splitLine[PLAYER_POSITION];
            String playerName = splitLine[PLAYER_NAME];
            String clubName = splitLine[CLUB_NAME];
            String countryName = splitLine[CLUB_COUNTRY];

            Country country = null;

            if(!countryRepository.existsByName(countryName)){
                country = new Country();
                country.setName(countryName);
                countryRepository.save(country);
            } else {
                country = countryRepository.findByName(countryName);
            }

            Club club = null;

            if(clubRepository.existsByName(clubName)){
                club = new Club();
                club.setName(clubName);
            } else {
                club = clubRepository.findByName(clubName);
            }

            Team team = new Team();
            team.setCountry(country);
            teamRepository.save(team);

            Player player = new Player();
            player.setName(playerName);
            player.setTeam(team);
            player.setClub(club);
            player.setPosition(playerPosition);
            player.setJerseyNumber(jerseyNumber);

            playerRepository.save(player);
        }
        return "";
    }

}

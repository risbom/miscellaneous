package com.boris;

import com.boris.model.Club;
import com.boris.model.Country;
import com.boris.model.Player;
import org.springframework.data.repository.CrudRepository;

// This will be AUTO IMPLEMENTED by Spring into a Bean called userRepository
// CRUD refers Create, Read, Update, Delete

public interface PlayerRepository extends CrudRepository<Player, Integer> {

    boolean existsByName(String name);

    Player findByName(String name);

}
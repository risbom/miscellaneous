package com.boris;

import com.boris.model.Club;
import com.boris.model.Country;
import org.springframework.data.repository.CrudRepository;

// This will be AUTO IMPLEMENTED by Spring into a Bean called userRepository
// CRUD refers Create, Read, Update, Delete

public interface ClubRepository extends CrudRepository<Club, Integer> {

    boolean existsByName(String name);

    Club findByName(String name);

}
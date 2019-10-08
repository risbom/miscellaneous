package com.boris;

import com.boris.model.Country;
import com.boris.model.Team;
import org.springframework.data.repository.CrudRepository;

// This will be AUTO IMPLEMENTED by Spring into a Bean called userRepository
// CRUD refers Create, Read, Update, Delete

public interface TeamRepository extends CrudRepository<Team, Integer> {

}
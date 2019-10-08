package com.boris;

import com.boris.model.Country;
import org.springframework.data.repository.CrudRepository;

// This will be AUTO IMPLEMENTED by Spring into a Bean called userRepository
// CRUD refers Create, Read, Update, Delete

public interface CountryRepository extends CrudRepository<Country, Integer> {

    boolean existsByName(String name);

    Country findByName(String name);

}
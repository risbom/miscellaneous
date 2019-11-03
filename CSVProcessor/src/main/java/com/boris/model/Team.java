package com.boris.model;

import org.hibernate.annotations.Type;

import javax.persistence.*;

@Entity
public class Team {

    @Id
    @GeneratedValue(strategy= GenerationType.AUTO)
    private Integer id;

    @ManyToOne( cascade = {CascadeType.PERSIST, CascadeType.MERGE} )
    @JoinColumn(name="country_id")
    private Country country;

    //private Group group;

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public Country getCountry() {
        return country;
    }

    public void setCountry(Country country) {
        this.country = country;
    }

    //public Group getGroup() {
    //    return group;
    //}

    //public void setGroup(Group group) {
    //    this.group = group;
    //}
}

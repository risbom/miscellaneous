package com.boris;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.io.Resource;
import org.springframework.core.io.ResourceLoader;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import java.io.IOException;

@Controller
@RequestMapping(path="/read")
public class MyController {

    @Autowired
    private CSVReader csvReader;

    @Autowired
    private ResourceLoader resourceLoader;

    @GetMapping(path="/trigger")
    public @ResponseBody
    String trigger () {
        try {
            Resource resource = resourceLoader.getResource("classpath:1954_2014_Squads.csv");
            csvReader.read(resource.getFile().getAbsolutePath());
        } catch (IOException e) {
            e.printStackTrace();
        }
        return "Done";
    }

}

package com.boris;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

@Component
public class CSVReader {

    @Autowired
    private SquadProcessor squadProcessor;

    public void read(String fileName) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File(fileName));
        while (scanner.hasNext()) {
            squadProcessor.parseLine(scanner.nextLine());
        }
        scanner.close();
    }
}

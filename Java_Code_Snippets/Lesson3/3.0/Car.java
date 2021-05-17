package com.digitalcrafts.java.lesson3;

public class Car {
    private String vin;
    private int year;
    private String make;
    private String model;
    private String owner;
    private double currentMileage;
    private int numberOfPassengers;

    // The setVin() method allows us to define the vin property
    void setVin(String newVin){
        this.vin = newVin;
    }
    // the getVin() method allows us to retrieve the vin property
    String getVin(){
        return this.vin;
    }
}

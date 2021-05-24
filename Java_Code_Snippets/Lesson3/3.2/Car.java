package com.digitalcrafts.java.lesson3;

public class Car {
    private String vin;
    private int year;
    private String make;
    private String model;
    private String owner;
    private double currentMileage;
    private int numberOfPassengers;


    void setVin(String newVin){
        this.vin = newVin;
    }

    String getVin(){
        return this.vin;
    }

}

interface Vehicle {
    String getType();
}

class Car implements Vehicle {
    @Override
    public String getType() {
        return "Car";
    }
}

class Bike implements Vehicle {
    @Override
    public String getType() {
        return "Bike";
    }
}

class Truck implements Vehicle {
    @Override
    public String getType() {
        return "Truck";
    }
}

interface VehicleFactory {
    Vehicle createVehicle();
}

class CarFactory implements VehicleFactory {
    // Write your code here
    @Override
    public Vehicle createVehicle(){
        return new Car();
    }

}

class BikeFactory implements VehicleFactory {
    // Write your code here
    @Override
    public Vehicle createVehicle(){
        return new Bike();
    }
}

class TruckFactory implements VehicleFactory {
    // Write your code here
    @Override
    public Vehicle createVehicle(){
        return new Truck();
    }
}

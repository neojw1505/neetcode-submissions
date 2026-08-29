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

abstract class VehicleFactory {
    abstract Vehicle createVehicle();
}

class CarFactory extends VehicleFactory {
    // Write your code here
    @Override
    Vehicle createVehicle(){
        return new Car();
    }

}

class BikeFactory extends VehicleFactory {
    // Write your code here
    @Override
    Vehicle createVehicle(){
        return new Bike();
    }
}

class TruckFactory extends VehicleFactory {
    // Write your code here
    @Override
    Vehicle createVehicle(){
        return new Truck();
    }
}

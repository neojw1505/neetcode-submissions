class SquareHole {
    private double sideLength;

    public SquareHole(double sideLength) {
        this.sideLength = sideLength;
    }

    public boolean canFit(Square square) {
        return this.sideLength >= square.getSideLength();
    }
}

class Square {
    private double sideLength;

    public Square() {}

    public Square(double sideLength) {
        this.sideLength = sideLength;
    }

    public double getSideLength() {
        return this.sideLength;
    }
}

class Circle {
    private double radius;

    public Circle(double radius) {
        this.radius = radius;
    }

    public double getRadius() {
        return this.radius;
    }
}

class CircleToSquareAdapter extends Square {
    private Circle circle;

    public CircleToSquareAdapter(Circle circle) {
      // Write your code here
      this.circle = circle;
    }

    @Override
    public double getSideLength() {
      // Write your code here
      return 2 * this.circle.getRadius();
    }
}

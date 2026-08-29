class Order {
    private String contents;
    private boolean takeOut;

    public Order(String contents, boolean takeOut) {
        this.contents = contents;
        this.takeOut = takeOut;
    }

    public String getOrder() {
        return contents;
    }

    public boolean isTakeOut() {
        return takeOut;
    }
}

class Cashier {
    public Order takeOrder(String contents, boolean takeOut) {
        return new Order(contents, takeOut);
    }
}

class Food {
  private String contents;

  public Food(String order) {
    this.contents = order;
  }

  public String getFood() {
    return contents;
  }
}

class Chef {
    public Food prepareFood(Order order) {
        return new Food(order.getOrder());
    }
}

class PackagedFood extends Food {
    public PackagedFood(Food food) {
        super(food.getFood() + " in a bag");
    }
}

class KitchenStaff {
    public PackagedFood packageOrder(Food food) {
        return new PackagedFood(food);
    }
}

class DriveThruFacade {
    private Cashier cashier = new Cashier();
    private Chef chef = new Chef();
    private KitchenStaff kitchenStaff = new KitchenStaff();

    public Food takeOrder(String orderContents, boolean takeOut) {
        // Implement method here
        Order order = cashier.takeOrder(orderContents, takeOut);
        Food food = chef.prepareFood(order);

        if (order.isTakeOut()) {
            return kitchenStaff.packageOrder(food);
        }

        return food;
    }
}

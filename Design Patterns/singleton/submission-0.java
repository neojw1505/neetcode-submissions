static class Singleton {
    private static Singleton uniqueInstance = null;
    private String value = null;

    public static Singleton getInstance() {
        if (uniqueInstance == null) {
            uniqueInstance = new Singleton();
        }
        return uniqueInstance;
    }   

    // Getters
    public String getValue() {
        return this.value;
    }

    // Setter
    public void setValue(String value) {
        this.value = value;
    }
    
}
